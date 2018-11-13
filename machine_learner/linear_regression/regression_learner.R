library(readr)
library(ggplot2)
library(class)
library(gmodels)
library(descr)
library(reshape2)
library(boot)
library(RColorBrewer)
library(xtable)
library(regclass)
library(pROC)
library(MASS)

panel.hist <- function(x, ...)
{
  usr <- par("usr"); on.exit(par(usr))
  par(usr = c(usr[1:2], 0, 1.5) )
  h <- hist(x, plot = FALSE)
  breaks <- h$breaks; nB <- length(breaks)
  y <- h$counts; y <- y/max(y)
  rect(breaks[-nB], 0, breaks[-1], y, col = "cyan", ...)
}

F606W <- read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F606W-2018-10-19.csv")
good_data <- read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/deep_sky-2018-10-19.csv")

hubble_test <- data.frame(F606W)
hubble_test2 <- data.frame(good_data)
pairs(hubble_test, pch = 1, cex = 0.3, diag.panel=panel.hist)
cor(hubble_test)
pairs(hubble_test_cleaned2, pch = 1, cex = 0.3, diag.panel=panel.hist)
cor(hubble_test_cleaned2)
hubble_test_cleaned2 <- subset(hubble_test2, hubble_test2$background_abmag > 75 & hubble_test2$background_abmag != "Inf")


file_used = hubble_test_cleaned2

# Training and test data sets (not brilliant with this data set due to doubles, small size)
shuffled = sample(nrow(file_used))
training = file_used[shuffled[1:(length(shuffled)*0.8)],]
testing = file_used[shuffled[(length(shuffled)*0.8+1):length(shuffled)],]

data_hubble = data.frame(x = training$sun_alt, y = training$background_abmag)
ggplot(aes(x , y), data = data_hubble) +
  geom_point(cex = 2, pch = 20) +
  geom_smooth()+
  ylab("background") +
  xlab("sunangle") +
  ggtitle("background as a function of sunangle")

df1_train <-data.frame(x = training$sun_alt , y = training$background_abmag)
df2_test <-data.frame(x = testing$sun_alt , y = testing$background_abmag)

ggplot(df1_train, aes(x,y))+ geom_point(aes(color="Training Data"), pch = 20)+
  geom_point(data=df2_test, aes(color="Testing Data"), pch = 18)+
  labs(color="Split Dataset")+
  ylab("Background")+
  xlab("Sun Altitude")+
  ggtitle("Background as a function of sun altitude \n with training and test data")

# Find best polynomial fit 
mse_calc<- function(sm) 
  mean(sm$residuals^2)
order <- 1:10
mse_test <- c()
mse_train <- c()
for(n in order){
  fit <- lm(background_abmag ~ poly(sun_alt, n, raw=TRUE), data = training)
  mse_train[n] <- mse_calc(summary(fit))
  prediciton_test <- predict(fit, newdata = testing)
  mse_test[n] <- mean((testing$background_abmag - prediciton_test)^2)
}

mse_data <- data.frame(x = order, y = mse_train)
mse2_data <- data.frame(x = order, y = mse_test)

ggplot(aes(x , y), data = mse_data) +
  geom_line(aes(color="Training Data"), pch = 20, lty = 5)+
  geom_line(data=mse2_data, aes(color="Training + Testing Data"), pch = 18, lty = 5)+
  labs(color="Model")+
  ylab("Mean Standard Error") +
  xlab("Polynomial Order") +
  ggtitle("MSE as a function of polynomial order")

ggplot(data_hubble, aes(x , y)) + 
  geom_point(pch = 20, cex = 2) + 
  stat_smooth(method = "lm", formula = y ~ poly(x,6), alpha = 0.001, colour="blue", cex = 0.5)+
  stat_smooth(method = "lm", formula = y ~ poly(x,10), alpha = 0.001, colour="green", cex = 0.5)+
  stat_smooth(method = "lm", formula = y ~ poly(x,9), alpha = 0.001, colour="red", cex = 0.5)+
  ylab("Background")+
  xlab("Sunangle")+
  ggtitle("Comparing Polynomials")

# Check it works with different seeds for training and testing data sets 
iters <- 1:500
best_order_train <- c()
best_order_test <- c()
for (m in iters){
  set.seed(m)
  shuffled = sample(nrow(file_used))
  training = file_used[shuffled[1:(length(shuffled)*0.8)],]
  testing = file_used[shuffled[(length(shuffled)*0.8+1):length(shuffled)],]
  order <- 1:10
  mse_train2 <- c()
  mse_test2 <- c()
  for(n in order){
    fit <- lm(background_abmag ~ poly(sun_alt, n, raw=TRUE), data = training)
    mse_train2[n] <- mse_calc(summary(fit))
    prediciton_test <- predict(fit, newdata = testing)
    mse_test2[n] <- mean((testing$background_abmag - prediciton_test)^2)
  }
  index_train <- match(min(mse_train2),mse_train2)
  best_order_train[m] <- order[index_train]
  index_test <- match(min(mse_test2),mse_test2)
  best_order_test[m] <- order[index_test]
}

qplot(best_order_train, geom="histogram", xlab = 'Order', ylab = 'Counts', main = 'Best order using only training data') 
qplot(best_order_test, geom="histogram", xlab = 'Order', ylab = 'Counts', main = 'Best order using test and training data', binwidth = 0.5)

# Same thing with 10 fold cross validation 
iters2 <- 1:100
best_order_glm <- c()
error <- c()
for (m in iters2){
  set.seed(m)
  shuffled = sample(nrow(file_used))
  training = file_used[shuffled[1:(length(shuffled)*0.8)],]
  testing = file_used[shuffled[(length(shuffled)*0.8+1):length(shuffled)],]
  for (i in 1:10){
    glm.fit=glm(background_abmag ~ poly(sun_alt, i, raw=TRUE), data = training)
    error[i]=cv.glm(training,glm.fit,K=5)$delta[1]
  }
  index_glm <- match(min(error),error)
  best_order_glm[m] <- order[index_glm]
}

qplot(best_order_glm, geom="histogram", xlab = 'Order', ylab = 'Counts', main = 'Best order using 5 fold Cross Validation', binwidth = 0.5)


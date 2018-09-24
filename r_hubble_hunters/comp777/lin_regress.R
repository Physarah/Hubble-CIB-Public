library(readr)
library(ggplot2)
library(class)
library(gmodels)
library(descr)
library(reshape2)
library(boot)
library(RColorBrewer)
library(xtable)
install.packages("regclass")
library(regclass)
install.packages("pROC")
library(pROC)

SN2005CZ <- read.csv("/Users/Physarah/Desktop/ASTRO/Hubble-CIB/r_hubble_hunters/data/SN2005CZ.csv")
hubble_test <- data.frame(SN2005CZ$MDRIZSKY,
                          SN2005CZ$EXPTIME,
                          SN2005CZ$Central.Wavelength,
                          SN2005CZ$SUNANGLE,
                          SN2005CZ$PHOTBW,
                          SN2005CZ$PHOTPLAM)

names(hubble_test) <- c("background", 
                        "exptime", 
                        "wavelength", 
                        "sunangle", 
                        "filter_bw", 
                        "pivot_wave")

# Basic overview 
pairs(hubble_test) 
cor(hubble_test)

# Training and test data sets (not brilliant with this data set due to doubles, small size)
shuffled = sample(nrow(hubble_test))
training = hubble_test[shuffled[1:(length(shuffled)*0.8)],]
testing = hubble_test[shuffled[(length(shuffled)*0.8+1):length(shuffled)],]

data_hubble = data.frame(x = training$sunangle, y = training$background)
ggplot(aes(x , y), data = data_hubble) +
  geom_point(cex = 2, pch = 20) +
  geom_smooth()+
  ylab("background") +
  xlab("sunangle") +
  ggtitle("background as a function of sunangle")

df1_train <-data.frame(x = training$sunangle , y = training$background)
df2_test <-data.frame(x = testing$sunangle , y = testing$background)

ggplot(df1_train, aes(x,y))+ geom_point(aes(color="Training Data"), pch = 20)+
  geom_point(data=df2_test, aes(color="Testing Data"), pch = 18)+
  labs(color="Split Dataset")+
  ylab("Background")+
  xlab("Sunangle")+
  ggtitle("background as a function of sunangle with training and test data")

# Find best polynomial fit 
mse_calc<- function(sm) 
  mean(sm$residuals^2)
order <- 1:10
mse_test <- c()
mse_train <- c()
for(n in order){
  fit <- lm(background ~ poly(sunangle, n, raw=TRUE), data = training)
  mse_train[n] <- mse_calc(summary(fit))
  prediciton_test <- predict(fit, newdata = testing)
  mse_test[n] <- mean((testing$background - prediciton_test)^2)
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
  stat_smooth(method = "lm", formula = y ~ poly(x,1), alpha = 0.001, colour="blue", cex = 0.5)+
  stat_smooth(method = "lm", formula = y ~ poly(x,2), alpha = 0.001, colour="green", cex = 0.5)+
  stat_smooth(method = "lm", formula = y ~ poly(x,3), alpha = 0.001, colour="red", cex = 0.5)+
  ylab("Background")+
  xlab("Sunangle")+
  ggtitle("Comparing Polynomials")

# Check it works with different seeds for training and testing data sets 
iters <- 1:500
best_order_train <- c()
best_order_test <- c()
for (m in iters){
  set.seed(m)
  shuffled = sample(nrow(hubble_test))
  training = hubble_test[shuffled[1:(length(shuffled)*0.8)],]
  testing = hubble_test[shuffled[(length(shuffled)*0.8+1):length(shuffled)],]
  order <- 1:10
  mse_train2 <- c()
  mse_test2 <- c()
  for(n in order){
    fit <- lm(background ~ poly(sunangle, n, raw=TRUE), data = training)
    mse_train2[n] <- mse_calc(summary(fit))
    prediciton_test <- predict(fit, newdata = testing)
    mse_test2[n] <- mean((testing$background - prediciton_test)^2)
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
  shuffled = sample(nrow(hubble_test))
  training = hubble_test[shuffled[1:(length(shuffled)*0.8)],]
  testing = hubble_test[shuffled[(length(shuffled)*0.8+1):length(shuffled)],]
  for (i in 1:10){
    glm.fit=glm(background ~ poly(sunangle, i, raw=TRUE), data = training)
    error[i]=cv.glm(training,glm.fit,K=5)$delta[1]
  }
  index_glm <- match(min(error),error)
  best_order_glm[m] <- order[index_glm]
}

# Clear over fitting here (poor sample size) 
qplot(best_order_glm, geom="histogram", xlab = 'Order', ylab = 'Counts', main = 'Best order using 5 fold Cross Validation', binwidth = 0.5)

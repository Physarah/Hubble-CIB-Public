library(readr)
library(ggplot2)
library(MASS)
library(class)
library(gmodels)
library(descr)

deep_sky <- read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/deep_sky-2018-10-19.csv")
deep_sky_cleaned <- subset(deep_sky, deep_sky$background_abmag != "Inf")

# Using 1 variable 

set.seed(2)
shuffled = sample(nrow(deep_sky_cleaned))
training = deep_sky_cleaned[shuffled[1:(length(shuffled)*0.7)],]
testing = deep_sky_cleaned[shuffled[(length(shuffled)*0.7+1):length(shuffled)],]

high_background_labels <- ifelse(training$background_abmag > 79 , "yes", "no")

set.seed(4)
k_values_e <- 1:100
acc_e <- c()
for(n in k_values_e){
  shine_prediciton <- knn(train = data.frame(training$sun_alt), test = data.frame(testing$sun_alt),
                         cl = high_background_labels, k = n)
  
  acc_e[n] <- mean(shine_prediciton==high_background_labels)
}

results_e <- data.frame(x = k_values_e, y = acc_e*100)
ggplot(aes(x , y), data = results_e) +  
  geom_point() +
  geom_line(col = 'red', lty = 5) +
  xlab("K Value") +
  ylab("Accuracy (%)") +
  ggtitle("Accuracy of the model as a function K on 1 variable")
max(acc_e)

# Using both variables 

set.seed(2)
shuffled = sample(nrow(deep_sky_cleaned))
training = deep_sky_cleaned[shuffled[1:(length(shuffled)*0.7)],]
testing = deep_sky_cleaned[shuffled[(length(shuffled)*0.7+1):length(shuffled)],]

high_shine_labels <- ifelse(training$background_abmag > 79 , "yes", "no")

set.seed(1)
k_values <- 1:100
mse_knn <- c()
acc <- c()
for(n in k_values){
  shine_prediciton <- knn(train = data.frame(training[1:3]), test = data.frame(testing[1:3]),
                         cl = high_shine_labels, k = n)
  
  acc[n] <- mean(shine_prediciton==high_shine_labels)
  mse_knn[n] <- mean((shine_prediciton - high_shine_labels)^2)
}
results <- data.frame(x = k_values, y = acc*100)
ggplot(aes(x , y), data = results) +  
  geom_point() + 
  geom_line(col = 'red', lty = 5) +
  xlab("K Value") +
  ylab("Accuracy (%)") +
  ggtitle("Accuracy of the model as a function K for both variables")
max(acc)


library(readr)
library(ggplot2)

F606W <- read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F606W-2018-10-19.csv")
F606W_cleaned <- subset(F606W, F606W$background_abmag != "Inf")
high_shine <- ifelse(F606W_cleaned$background_abmag > 79, "yes", "no")

new_hubble <- data.frame(F606W_cleaned, high_shine)

set.seed(333)
samples <- sample(2, nrow(new_hubble), replace = TRUE, prob = c(0.67,0.33))
new_hubble_training <- new_hubble[samples == 1, 3]
length(new_hubble_training)

predictor_high_background <- subset(new_hubble, high_shine == "yes")
new_hubble_test <- predictor_high_background[samples == 2, 1:3]
length(new_hubble_test)

hubble_trainLabels <- predictor_high_background[samples == 1, 3]
hubble_testLabels <- predictor_high_background[samples == 2, 3]

k_values <- 1:50
acc <- c()
for(n in k_values){
  hubble_prediction <- knn(train = new_hubble_training, test = new_hubble_test,
                           cl = hubble_trainLabels, k = n)
  
  acc[n] <- mean(hubble_prediction==hubble_testLabels)

}

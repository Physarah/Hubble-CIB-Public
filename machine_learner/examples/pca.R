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

# Not sure if these are the variables I really want... 
SN2005CZ <- read.csv("/Users/Physarah/Desktop/ASTRO/Hubble-CIB/r_hubble_hunters/data/SN2005CZ.csv")
hubble <- data.frame(SN2005CZ$MDRIZSKY,
                          SN2005CZ$EXPTIME,
                          SN2005CZ$Central.Wavelength,
                          SN2005CZ$SUNANGLE,
                          SN2005CZ$PHOTBW,
                          SN2005CZ$PHOTPLAM)

names(hubble) <- c("background", 
                        "exptime", 
                        "wavelength", 
                        "sunangle", 
                        "filter_bw", 
                        "pivot_wave")

set.seed(1)
shuffled = sample(nrow(hubble_test))
hubble_Train = hubble[shuffled[1:(length(shuffled)*0.6)],]
hubble_Test = hubble[shuffled[(length(shuffled)*0.6+1):length(shuffled)],]

apply(hubble_Train, 2, mean)
apply(hubble_Test, 2, var) # Hunge spread in variance... scaling

pca_training <- prcomp(hubble_Train, center = TRUE, scale = TRUE) # Checking
pca_training$center
pca_training$scale
pca_training$rotation
pca_training$sdev
biplot(pca_training,  scale = 0)

pca_training_var = pca_training$sdev^2
principle_var = pca_training$sdev^2/sum(pca_training_var)
print(principle_var) # First component is 95% of variance.. 

component = c(1:6)
component_data <- data.frame(x = component, y = principle_var)
ggplot(aes(x , y), data = component_data) +  
  geom_line() +
  geom_point(size=5, colour="white") + 
  geom_point(size=2, pch = 1) + 
  theme_classic() +
  theme(panel.background = element_rect(colour = "black")) +
  ylab("Percentage of Varience in the Data") +
  xlab("Principle Component") +
  ggtitle("Scree plot of the Proportion of Variance Explained")

cumlative_data <- data.frame(y = cumsum(principle_var), x = component)
ggplot(aes(x , y), data = cumlative_data) +  
  geom_line() +
  geom_point(size=5, colour="white") + 
  geom_point(size=2, pch = 1) + 
  theme_classic() +
  theme(panel.background = element_rect(colour = "black")) +
  ylab("Cumulative Proportion of Variance") +
  xlab("Principle Component") +
  ggtitle("Scree plot of the Cumulative Proportion of Variance Explained")


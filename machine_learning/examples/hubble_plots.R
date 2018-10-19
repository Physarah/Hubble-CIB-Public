library(readr)
library(ggplot2)
library(MASS)
library(class)
library(gmodels)
library(descr)
library(reshape2)
library(boot)
library(RColorBrewer)
library(xtable)

hubble_1 <- read.csv("/Users/Physarah/Desktop/ASTRO/Hubble-CIB/r_hubble_hunters/data/F814W.csv")
SN2005CZ <- read.csv("/Users/Physarah/Desktop/ASTRO/Hubble-CIB/r_hubble_hunters/data/SN2005CZ.csvv")
View(hubble_1)
View(SN2005CZ)

log_mdriz = log(hubble_1$MDRIZSKY, 10)
exp <- subset(hubble_1, hubble_1$EXPTIME > 20 & hubble_1$MDRIZSKY < 1000 & hubble_1$MDRIZSKY > 0)
#qplot(exp$EXPTIME, exp$MDRIZSKY)
sun <- hubble_1$SUNANGLE[66095:66150]
med <- hubble_1$MDRIZSKY[66095:66150]
qplot(hubble_1$SUNANGLE[66095:66150],hubble_1$MDRIZSKY[66095:66150])
fit <- lm(sun~med)
qplot(fit)

scatter.smooth(x=sun, y=med, 
               xlab = "Sun Angle",
               ylab = "Background (MDRIZSKY)",
               main="Background variation over a few orbits",
               ylim  = c(0,150),
               pch = 3)  # scatterplot


scatter.smooth(y=SN2005CZ$MDRIZSKY, x=SN2005CZ$PHOTBW, 
               ylab = "Background",
               xlab = "Bandwidth",
               main="Background variation over a few orbits",
               pch = 3)  # scatterplot

scatter.smooth(y=SN2005CZ$MDRIZSKY, x=SN2005CZ$SUNANGLE, 
               ylab = "Background",
               xlab = "Sun angle",
               main="Background variation over a few orbits",
               pch = 3)  # scatterplot
message('We find the error rate for using all predictors to be ', error_rate2)
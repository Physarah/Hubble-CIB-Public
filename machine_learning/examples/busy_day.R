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

#Clearly there is something wrong with using straight background counts.... the situation looks VERY different when you 
#calibrate this with zeropoint data
panel.hist <- function(x, ...)
{
  usr <- par("usr"); on.exit(par(usr))
  par(usr = c(usr[1:2], 0, 1.5) )
  h <- hist(x, plot = FALSE)
  breaks <- h$breaks; nB <- length(breaks)
  y <- h$counts; y <- y/max(y)
  rect(breaks[-nB], 0, breaks[-1], y, col = "cyan", ...)
}

hubble_data  <- read.csv("/Users/Physarah/Desktop/Busy_Day/F435W.csv")
hubble_test <- data.frame(hubble_data$MDRIZSKY,
                          hubble_data$SUN_ALT,
                          hubble_data$SUNANGLE,
                          hubble_data$EXPTIME)
deep_field_data <- read.csv("/Users/Physarah/Desktop/Busy_Day/deep_field.csv")
deep_field <- data.frame(hubble_data$MDRIZSKY,
                          hubble_data$SUN_ALT,
                          hubble_data$SUNANGLE,
                          hubble_data$EXPTIME,
                         hubble_data$PHOTPLAM,
                         hubble_data$PHOTFLAM)

galaxy_1732526 <- hubble_test[18181:18196,]
deep_orbit1 <- deep_field[5489:5622,]

deep_orbit_clean <- subset(deep_orbit1, deep_orbit1$hubble_data.MDRIZSKY < 100)
ABZeros <- - 2.5*log10(deep_orbit_clean$hubble_data.PHOTFLAM) - 5*log10(deep_orbit_clean$hubble_data.PHOTPLAM)
somethings <- deep_orbit_clean$hubble_data.MDRIZSKY + ABZeros
pairs(deep_orbit_clean)
cor(deep_orbit_clean)

pairs(deep_orbit_clean, pch = 1, cex = 0.3, diag.panel=panel.hist)

current_y <- somethings
current_x <- deep_orbit_clean$hubble_data.SUN_ALT

scatter.smooth(x=current_x, y=current_y, 
               xlab = "Sun Angle",
               ylab = "Background (MDRIZSKY)",
               main="Background variation over a few orbits",
               pch = 3)

data_hubble = data.frame(x = current_x, y = current_y)
ggplot(aes(x , y), data = data_hubble) +
  geom_point(cex = 2, pch = 20) +
  geom_smooth()+
  ylab("MDRIZSKY") +
  xlab("SUNANGLE") +
  ggtitle("Earth Shine")







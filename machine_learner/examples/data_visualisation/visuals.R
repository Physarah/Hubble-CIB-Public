library(ggplot2)
F606W <- read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F606W-2018-10-19.csv")
pairs(F606W, pch = 20, main = "COSMOS F606W All Orbits")

F814W <- read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F815-2018-10-19.csv")
pairs(F814W, pch = 20, main = "COSMOS F814W All Orbits")

F435W <- read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F435W-2018-10-19.csv")
pairs(F435W, pch = 20, main = "COSMOS F435W All Orbits")

deep_sky <- read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/deep_sky-2018-10-19.csv")
pairs(deep_sky, pch = 20, main = "HUDF All Orbits")

F606W_orbit1 <- F606W[240:280, ]
F814W_orbit1 <- F814W[23:60, ]
background_orbit1 <- deep_sky[100:300, ]

ggplot(F606W_orbit1 , aes(y=background_abmag, x=sun_alt )) + 
  labs(title="COSMOS F606W 1 Orbits", 
       x="Sun Altitude (deg)", 
       y="Background (mag AB)")+
  geom_jitter(shape = 3, size = 0.5, width = 0.50)

ggplot(deep_sky , aes(y=background_abmag, x=sun_alt )) + 
  labs(title="COSMOS F606W 1 Orbits", 
       x="Sun Altitude (deg)", 
       y="Background (mag AB)")+
  geom_jitter(shape = 3, size = 0.5, width = 0.50)

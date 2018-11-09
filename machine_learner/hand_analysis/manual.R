library(readr)
library(ggplot2)
library(MASS)
library(class)
library(gmodels)
library(descr)

raw_file_cosmo_435 <- read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F435W-2018-10-19.csv")
raw_file_cosmo_606 <- read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F606W-2018-10-19.csv")
raw_file_cosmos_815 = read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F815-2018-10-19.csv")


deep_sky <- read.csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/deep_sky-2018-10-19.csv")
deep_sky_cleaned <- subset(deep_sky, deep_sky$background_abmag != "Inf")

deep <- subset(deep_sky_cleaned, deep_sky_cleaned$background_abmag > 78)
deep_back <- deep$background_abmag[100:300]
deep_alt <- deep$sun_alt[100:300]

F815W_dark <- raw_file_cosmos_815$background_abmag[23:60]
F815W_alt <- raw_file_cosmos_815$sun_alt[23:60]
F606W_dark <- raw_file_cosmo_606$background_abmag[240:280] 
F606W_alt <- raw_file_cosmo_606$sun_alt[240:280] 
F435 <- raw_file_cosmo_435

scatter.smooth(y = F815W_dark, x=F815W_alt, main="Dist ~ Speed")
scatter.smooth(y = F606W_dark, x=F606W_alt, main="Dist ~ Speed")


import matplotlib.pyplot as plt
import pandas as pd

F606W_comp = "yes"
all_points = "no"
filter_comp = "no"

raw_file_cosmo_435 = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F435W-2018-10-19.csv")
raw_file_cosmo_606 = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F606W-2018-10-19.csv")
raw_file_deep_field = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/deep_sky-2018-10-19.csv")
raw_file_good_data = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/good_data-2018-10-19.csv")
raw_file_cosmos_815 = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F815-2018-10-19.csv")

background_cosmo_435 = raw_file_cosmo_435["background_abmag"]
sun_alt_cosmo_435 = raw_file_cosmo_435["sun_alt"]
sun_angle_cosmo_435 = raw_file_cosmo_435["sun_angle"]
#plt.scatter(sun_alt_cosmo_435,background_cosmo_435,2)

background_cosmo_606 = raw_file_cosmo_606["background_abmag"]
sun_alt_cosmo_606 = raw_file_cosmo_606["sun_alt"]
sun_angle_cosmo_606 = raw_file_cosmo_606["sun_angle"]
#plt.scatter(sun_alt_cosmo_606,background_cosmo_606,2)

background_deep = raw_file_deep_field["background_abmag"][100:300]
sun_alt_deep = raw_file_deep_field["sun_alt"][100:300]
sun_angle_deep = raw_file_deep_field["sun_angle"][100:300]
#plt.scatter(sun_alt_deep,background_deep,2)

background_good = raw_file_good_data["background_abmag"]
sun_alt_good = raw_file_good_data["sun_alt"]
sun_angle_good = raw_file_good_data["sun_angle"]
#plt.scatter(sun_alt_good,background_good,2)

background_cosmo_815 = raw_file_cosmos_815["background_abmag"][23:60]
sun_alt_cosmo_815 = raw_file_cosmos_815["sun_alt"][23:60]
sun_angle_cosmo_815 = raw_file_cosmos_815["sun_angle"][23:60]
#plt.scatter(sun_alt_cosmo_815,background_cosmo_815,2)
#plt.ylim(79.54, 79.64)

if F606W_comp == "yes":
    plt.scatter(sun_alt_cosmo_606,background_cosmo_606,7, marker = "*", label = "Cosmos F606W")
    plt.scatter(sun_alt_deep,background_deep,7, marker = "+", label = "Hubble Deep F606W")
    plt.legend()
    plt.xlabel("Sun Altitude (deg)")
    plt.ylabel("Background (ABmag)")
    plt.title("Earthshine variation over 2 fields \n F606W filter over multiple orbits")
    plt.show()
    
    plt.scatter(sun_angle_cosmo_606,background_cosmo_606,7, marker = "*", label = "Cosmos F606W")
    plt.scatter(sun_angle_deep,background_deep,7, marker = "+", label = "Hubble Deep F606W")
    plt.legend()
    plt.xlabel("Sun Angle (deg)")
    plt.ylabel("Background (ABmag)")
    plt.title("Earthshine variation over 2 fields \n F606W filter over multiple orbits")
    plt.show()
    
if all_points == "yes":    
    plt.scatter(sun_alt_good,background_good,2)
    plt.xlabel("Sun Altitude (deg)")
    plt.ylabel("Background (ABmag)")
    plt.title("Earthshine variation multiple fields, multiple orbits, multiple filters")

if filter_comp == "yes":
    plt.scatter(sun_alt_cosmo_435,background_cosmo_435,10, marker = "*", label = "F435W")
    plt.scatter(sun_alt_cosmo_606[240:280],background_cosmo_606[240:280],10,marker = "x", label = "F606W")
    plt.scatter(sun_alt_cosmo_815,background_cosmo_815,10, marker = ".",label = "F814W")
    plt.legend(loc = "right")
    plt.xlabel("Sun Altitude (deg)")
    plt.ylabel("Background (ABmag)")
    plt.title("Earth shine contribution from cosmos fields \n Filter comparison")
    
    
import matplotlib.pyplot as plt

raw_file_cosmo_435 = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F435W-2018-10-19.csv")
raw_file_cosmo_606 = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F606W-2018-10-19.csv")
raw_file_deep_field = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/deep_sky-2018-10-19.csv")
raw_file_good_data = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/good_data-2018-10-19.csv")
raw_file_cosmos_815 = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F815-2018-10-19.csv")

background_cosmo = raw_file_cosmo_435["background_abmag"]
sun_alt_cosmo = raw_file_cosmo_435["sun_alt"]
sun_angle_cosmo = raw_file_cosmo_435["sun_angle"]

background_cosmo_606 = raw_file_cosmo_606["background_abmag"]
sun_alt_cosmo_606 = raw_file_cosmo_606["sun_alt"]
sun_angle_cosmo_606 = raw_file_cosmo_606["sun_angle"]

background_deep = raw_file_deep_field["background_abmag"]
sun_alt_deep = raw_file_deep_field["sun_alt"]
sun_angle_deep = raw_file_deep_field["sun_angle"]

background_good = raw_file_good_data["background_abmag"]
sun_alt_good = raw_file_good_data["sun_alt"]
sun_angle_good = raw_file_good_data["sun_angle"]

background_cosmo_815 = raw_file_cosmos_815["background_abmag"]
sun_alt_cosmo_815 = raw_file_cosmos_815["sun_alt"]
sun_angle_cosmo_815 = raw_file_cosmos_815["sun_angle"]

#plt.scatter(sun_alt_cosmo_606,background_cosmo_606,2)
#plt.scatter(sun_alt_cosmo,background_cosmo,2)
#plt.scatter(sun_alt_deep,background_deep,2)
#plt.scatter(sun_alt_good,background_good,2)
#plt.scatter(sun_alt_cosmo_815,background_cosmo_815,2)




import matplotlib.pyplot as plt

raw_file_cosmo = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F435W-2018-10-19.csv")
raw_file_cosmo_606 = pd.read_csv("/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv/cosmos_field_F606W-2018-10-19.csv")

background_cosmo = raw_file_cosmo["background_abmag"]
sun_alt_cosmo = raw_file_cosmo["sun_alt"]
sun_angle_cosmo = raw_file_cosmo["sun_angle"]

background_cosmo_606 = raw_file_cosmo_606["background_abmag"]
sun_alt_cosmo_606 = raw_file_cosmo_606["sun_alt"]
sun_angle_cosmo_606 = raw_file_cosmo_606["sun_angle"]

plt.scatter(sun_alt_cosmo_606,background_cosmo_606)
plt.scatter(sun_alt_cosmo,background_cosmo)



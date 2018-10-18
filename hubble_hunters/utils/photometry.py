import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os as oos
import datetime as dt

home_path = "/Users/Physarah/Desktop/Hubble-CIB/"
data_directory = home_path + "hubble_hunters/data/star_view_raw/"
raw_file = pd.read_csv(data_directory + "good_data.csv")

target_name = raw_file["Target Name"]
RA_V1 = raw_file["RA V1 Axis"]
DEC_V1 = raw_file["Dec V1 Axis"]
date_time = raw_file["DATE-OBS"]
exposure = raw_file["EXPTIME"]
sun_alt = raw_file["SUN_ALT"]
sun_angle = raw_file["SUNANGLE"]
background = raw_file["MDRIZSKY"]
filter_type1 = raw_file["FILTER1"]
filter_type2 = raw_file["FILTER2"]
phot_lam = raw_file["PHOTPLAM"]
phot_mode = raw_file["PHOTMODE"]
phot_flam = raw_file["PHOTFLAM"]
phot_zpt = raw_file["PHOTZPT"]
phot_bw = raw_file["PHOTBW"]
start_time = raw_file["Data Start Time"]
end_time = raw_file["Data End Time"]

pandas_data = list(zip(target_name, RA_V1, DEC_V1, 
                                 exposure, sun_alt, sun_angle,
                                 background, filter_type1, filter_type2, phot_lam, 
                                 phot_mode, phot_flam, phot_zpt, 
                                 phot_bw, start_time, end_time))

master_data_frame = pd.DataFrame(data = pandas_data, columns = ['target', 
                                                               'ra_v1', 
                                                               'dec_v1', 
                                                               'exp',
                                                               'sun_alt',
                                                               'sun_angle',
                                                               'background',
                                                               'filter1',
                                                               'filter2',
                                                               'photplam',
                                                               'photmode',
                                                               'photflam',
                                                               'photzpt',
                                                               'photbw',
                                                               'start',
                                                               'end'])

master_data_frame['phot_flag_1'] = np.where(master_data_frame['photplam'] > 0, 1, -1)
master_data_frame['phot_flag_2'] = np.where(master_data_frame['photflam'] > 0, 1, -1)


master_data_frame = master_data_frame.drop(master_data_frame[master_data_frame['phot_flag_1']==-1].index)
master_data_frame = master_data_frame.drop(master_data_frame[master_data_frame['phot_flag_2']==-1].index)

zero_point_init = -2.5 * np.log10(master_data_frame['photplam']) - 5 * np.log10(master_data_frame['photflam']) - 2.408

counts = np.arange(0,6460)
ABmag_background = []
for i in counts:
    background = -2.5*np.log10(float(master_data_frame['background'].iloc[i])) + float(zero_point_init.iloc[i])
    ABmag_background = np.append(ABmag_background, background)
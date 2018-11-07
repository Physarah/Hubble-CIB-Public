import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os as oos
import datetime as dt
import re
import datetime

def calibrate_hubble(file_input, file_name,
                     any_bool = "yes",
                     bias_bool = "yes",
                     dark_bool = "yes",
                     none_bool = "yes",
                     nope_bool = "yes" ):

    """
    A function to clean and calibrate the data from starview. It removes bias, darks, none type values etc.
    The function also performs the photometric calibrations of background counts in instrumental magnitudes
    to physical fluxes.

    Args:
        file_input (str): which file you want to use
        file_name (str): what you want to call it
        any_bool (str): "yes" or "no" gets rid of random data points
        bias_bool (str): "yes" or "no" gets rid of bias frames
        dark_bool (str): "yes" or "no" gets rid of dark frames
        none_bool (str): "yes" or "no" gets rid of none type values
        nope_boon (str): "yes" or "no" gets rid of Nan values
    """

    home_path = "/Users/Physarah/Desktop/Hubble-CIB/"
    data_directory = home_path + "hubble_hunters/data/star_view_raw/"
    raw_file = pd.read_csv(data_directory + file_input +".csv")
    save_path = "/Users/Physarah/Desktop/Hubble-CIB/hubble_hunters/data/calibrated_csv"

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

    if any_bool == "yes":

        master_data_frame = master_data_frame[(master_data_frame.target != 'ANY')]

    if bias_bool == "yes":
        master_data_frame = master_data_frame[(master_data_frame.target != 'BIAS')]

    if dark_bool == "yes":
        master_data_frame = master_data_frame[(master_data_frame.target != 'DARK')]

    if none_bool == "yes":
        master_data_frame = master_data_frame[(master_data_frame.background != None)]

    if nope_bool == "yes":
        master_data_frame = master_data_frame[(master_data_frame.background != ' ')]

    zero_point_init = -2.5 * np.log10(master_data_frame['photplam']) - 5 * np.log10(master_data_frame['photflam']) - 2.408

    counts = np.arange(0,len(zero_point_init))
    ABmag_background = []
    for i in counts:
        something = master_data_frame['background'].iloc[i]
        background = -2.5*np.log10(float(something)) + float(zero_point_init.iloc[i])
        ABmag_background = np.append(ABmag_background, background)

    final_data = (ABmag_background, master_data_frame['sun_alt'], master_data_frame['sun_angle'])
    final_col_names = ('background_abmag','sun_alt', 'sun_angle')
    date_created = str(datetime.datetime.now())
    export_csv(data = final_data, col_names = final_col_names, fname =  file_name + "-" + date_created[0:10] + ".csv", save_path = save_path)

import matplotlib.pyplot as plt

def conditional_search(variable, condition):
    """
    A function with searches the starview output for specific features

    Args:
        variable (str): what feature are you looking for? e.g. background, filter data_type
        condition (str): what specific subset of the feature you are looking for, e.g. filter[F435W]

    Example:
        master_data_frame['filter2'][i] == 'F435W'

    Returns:
        backs_filt (int): the raw background
        alts_filt (int): sun altitude
        angs_filt (int): sun angle
    """
    backs_filt = []
    alts_filt = []
    angs_filt = []
    intext_filtered = []
    for i in index:
        if master_data_frame[variable][i] == condition:
            backs = ABmag_background[i]
            alts = master_data_frame['sun_alt'][i]
            angs = master_data_frame['sun_angle'][i]
            backs_filt = np.append(backs_filt,backs)
            alts_filt = np.append(alts_filt, alts)
            angs_filt = np.append(angs_filt, angs)
            intext_filtered = np.append(intext_filtered, i)

    return(backs_filt, alts_filt, angs_filt)

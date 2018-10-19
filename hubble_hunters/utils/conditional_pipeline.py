import matplotlib.pyplot as plt

index = np.arange(0,4732)

backs_filt = []
alts_filt = []
intext_filtered = []

for i in index:
    if master_data_frame['filter2'][i] == 'F435W':
        backs = ABmag_background[i]
        alts = master_data_frame['sun_alt'][i]
        backs_filt = np.append(backs_filt,backs)
        alts_filt = np.append(alts_filt, alts)
        intext_filtered = np.append(intext_filtered, i)
        
plt.scatter(alts_filt,backs_filt,2)

def conditional_search(variable, condition):
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
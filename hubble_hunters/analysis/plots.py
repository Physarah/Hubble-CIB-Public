import matplotlib.pyplot as plt

CDF_SOUTH_GOODS = [3345,3493]
HDF_NORTH_GOODS_1 = [2805,3104]
HDF_NORTH_GOODS_2 = [2805,3004]
HDF_NORTH_GOODS_3 = [3291,3320]
NGC_4736_deep_sky = [3941,3960]

start1, end1 = date_time_maker(start_time, end_time)    
diff_HDF_NORTH_GOODS_1 = start1[HDF_NORTH_GOODS_1[0]]-start1[HDF_NORTH_GOODS_1[1]]
filter_HDF_NORTH_GOODS_1 = master_data_frame['filter'][HDF_NORTH_GOODS_1[1]]


#plt.scatter(master_data_frame['sun_angle'][2805:3104], ABmag_background[2805:3104], s= 2)
    
plt.scatter(master_data_frame['sun_alt'][3941:3960], ABmag_background[3941:3960], s= 2)
plt.ylim(78.2,78.8)


#plt.scatter(master_data_frame['sun_alt'][CDF_SOUTH_GOODS[0]:CDF_SOUTH_GOODS[1]], ABmag_background[CDF_SOUTH_GOODS[0]:CDF_SOUTH_GOODS[1]], s= 2)
#plt.xlim(0,70)
#plt.ylim(79.8,79.95)


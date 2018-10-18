import matplotlib.pyplot as plt

# Southern Hemisphere
# Spring(10) - Oct 
# Summer(1) - Jan
# Autumn(4) - Aprl 
# Winter(7) - July

HDF_NORTH_GOODS_1 = [2805,3104] # Autumn observation 

HDF_NORTH_GOODS_2 = [2805,3004] # Winter observation 

HDF_NORTH_GOODS_3 = [3291,3320] # Spring observation 

NGC_4736_deep_sky = [3941,3960] # Winter observation 

CDF_SOUTH_GOODS = [3345,3493] # Autumn observation 

start1, end1 = date_time_maker(start_time, end_time) 
   
diff_HDF_NORTH_GOODS_1 = start1[HDF_NORTH_GOODS_1[0]]-start1[HDF_NORTH_GOODS_1[1]]
filter1_HDF_NORTH_GOODS_1 = master_data_frame['filter1'][HDF_NORTH_GOODS_1[1]]
filter2_HDF_NORTH_GOODS_1 = master_data_frame['filter2'][HDF_NORTH_GOODS_1[1]]
print(filter1_HDF_NORTH_GOODS_1,filter2_HDF_NORTH_GOODS_1)

diff_HDF_NORTH_GOODS_2 = start1[HDF_NORTH_GOODS_2[0]]-start1[HDF_NORTH_GOODS_2[1]]
filter1_HDF_NORTH_GOODS_2 = master_data_frame['filter1'][HDF_NORTH_GOODS_2[1]]
filter2_HDF_NORTH_GOODS_2 = master_data_frame['filter2'][HDF_NORTH_GOODS_2[1]]
print(filter1_HDF_NORTH_GOODS_2,filter2_HDF_NORTH_GOODS_2)

diff_HDF_NORTH_GOODS_3 = start1[HDF_NORTH_GOODS_3[0]]-start1[HDF_NORTH_GOODS_3[1]]
filter1_HDF_NORTH_GOODS_3 = master_data_frame['filter1'][HDF_NORTH_GOODS_3[1]]
filter2_HDF_NORTH_GOODS_3 = master_data_frame['filter2'][HDF_NORTH_GOODS_3[1]]
print(filter1_HDF_NORTH_GOODS_3,filter2_HDF_NORTH_GOODS_3)

diff_NGC_4736_deep_sky = start1[NGC_4736_deep_sky[0]]-start1[NGC_4736_deep_sky[1]]
filter1_NGC_4736_deep_sky = master_data_frame['filter1'][NGC_4736_deep_sky[1]]
filter2_NGC_4736_deep_sky = master_data_frame['filter2'][NGC_4736_deep_sky[1]]
print(filter1_NGC_4736_deep_sky,filter2_NGC_4736_deep_sky)

diff_CDF_SOUTH_GOODS = start1[CDF_SOUTH_GOODS[0]]-start1[CDF_SOUTH_GOODS[1]]
filter1_CDF_SOUTH_GOODS = master_data_frame['filter1'][CDF_SOUTH_GOODS[1]]
filter2_CDF_SOUTH_GOODS = master_data_frame['filter2'][CDF_SOUTH_GOODS[1]]
print(filter1_CDF_SOUTH_GOODS,filter2_CDF_SOUTH_GOODS)

# Very good one !!!

plt.scatter(master_data_frame['sun_alt'], ABmag_background, s= 2)
plt.ylim(73.5,71)
plt.xlim(-75,25)

plt.scatter(master_data_frame['sun_angle'], ABmag_background, s= 2)
plt.ylim(73,71)
plt.xlim(118,135)


#plt.scatter(master_data_frame['sun_angle'][2805:3104], ABmag_background[2805:3104], s= 2)
    
plt.scatter(master_data_frame['sun_alt'][3941:3960], ABmag_background[3941:3960], s= 2)
plt.ylim(78.2,78.8)


#plt.scatter(master_data_frame['sun_alt'][CDF_SOUTH_GOODS[0]:CDF_SOUTH_GOODS[1]], ABmag_background[CDF_SOUTH_GOODS[0]:CDF_SOUTH_GOODS[1]], s= 2)
#plt.xlim(0,70)
#plt.ylim(79.8,79.95)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

home_path = "/Users/Physarah/Desktop/Hubble-CIB/"
data_directory = home_path + "hubble_hunters/data/star_view_raw/"
raw_file = pd.read_csv(data_directory + "good_data.csv")

start_time = raw_file["Data Start Time"]
end_time = raw_file["Data End Time"]

def date_time_maker(start_time, end_time):
    start_hour = []
    for i in start_time:
        start = int(i[11:13])
        start_hour = np.append(start_hour, start)
    start_hour_int = start_hour.astype(np.int64)
        
    start_min = []
    for i in start_time:
        start = int(i[14:16])
        start_min = np.append(start_min, start)    
    start_min_int = start_min.astype(np.int64)
    
    start_sec = []
    for i in start_time:
        start = int(i[17:19])
        start_sec = np.append(start_sec, start)
    start_sec_int = start_sec.astype(np.int64)
    
    length_start = len(start_hour)
    iter_obj_start = np.arange(0,length_start)
    start_time_object = []
    for i in iter_obj_start:
        start_time_object_iters = dt.time(start_hour_int[i], start_min_int[i], start_sec_int[i])
        start_time_object = np.append(start_time_object,start_time_object_iters)
         
    end_hour = []
    for i in end_time:
        end = i[11:13]
        end_hour = np.append(end_hour, end)    
    end_hour_int = end_hour.astype(np.int64)
        
    end_min = []
    for i in end_time:
        end = i[14:16]
        end_min = np.append(end_min, end)
    end_min_int = end_min.astype(np.int64)
         
    end_sec = []
    for i in end_time:
        end = i[17:19]
        end_sec = np.append(end_sec, end) 
    end_sec_int = end_sec.astype(np.int64)
    
    length_end = len(end_hour)
    iter_obj_end = np.arange(0,length_end)
    end_time_object = []
    for i in iter_obj_end:
        end_time_object_iters = dt.time(end_hour_int[i], end_min_int[i], end_sec_int[i])
        end_time_object = np.append(end_time_object,end_time_object_iters)
        
    start_year = []
    for i in start_time:
        start = int(i[0:4])
        start_year = np.append(start_year, start)
    start_year_int = start_year.astype(np.int64)    
        
    start_month = []
    for i in start_time:
        start = int(i[5:7])
        start_month = np.append(start_month, start)
    start_month_int = start_month.astype(np.int64) 
    
    start_day = []
    for i in start_time:
        start = int(i[8:10])
        start_day = np.append(start_day, start)
    start_day_int = start_day.astype(np.int64)
    
    length_start_date = len(start_hour)
    iter_obj_start_date = np.arange(0,length_start_date)
    start_date_object = []
    for i in iter_obj_start_date:
        start_date_object_iters = dt.date(start_year_int[i], start_month_int[i], start_day_int[i])
        start_date_object = np.append(start_date_object,start_date_object_iters)
         
    end_year = []
    for i in end_time:
        end = int(i[0:4])
        end_year = np.append(end_year, end)
    end_year_int = end_year.astype(np.int64) 
    
    end_month = []
    for i in end_time:
        end = int(i[5:7])
        end_month = np.append(end_month, end)
    end_month_int = end_month.astype(np.int64) 
    
    end_day = []
    for i in end_time:
        end = int(i[8:10])
        end_day = np.append(end_day, end)
    end_day_int = end_day.astype(np.int64)  
    
    length_end_date = len(end_year)
    iter_obj_end_date = np.arange(0,length_end_date)
    end_date_object = []
    for i in iter_obj_end_date:
        end_date_object_iters = dt.date(end_year_int[i], end_month_int[i], end_day_int[i])
        end_date_object = np.append(end_date_object,end_date_object_iters)  
        
    start_combined = []
    for i in iter_obj_end_date:
        start_new = dt.datetime.combine(start_date_object[i], start_time_object[i])
        start_combined = np.append(start_combined,start_new)
        
    end_combined = []
    for i in iter_obj_end_date:
        end_new = dt.datetime.combine(end_date_object[i], end_time_object[i])
        end_combined = np.append(end_combined,end_new)  
        
    return(start_combined,end_combined)    
    
start1, end1 = date_time_maker(start_time, end_time)    
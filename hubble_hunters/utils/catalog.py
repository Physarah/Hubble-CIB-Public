import csv
import os as oos
from itertools import zip_longest

def export_csv(data, col_names, fname, save_path):
    """
    Used to export any data you want to process in R or any other external program into a 
    friendly csv file even just for visualisation 
    """
    export_data = zip_longest(*data, fillvalue = '')
    completeName = oos.path.join(save_path, fname)
    with open(completeName, 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow((col_names))
        wr.writerows(export_data)
    myfile.close()
    return(print("File created successfully")) 
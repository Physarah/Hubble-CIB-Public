# Hubble-CIB
Code related to feasibility simulations and analysis of HST data and extracting the CIB (Cosmic Infrared Background).

## COMP777 Component 

The following contains instructions on running the machine learning aspect of this project. For the purpose of marking for the COMP777, cleaned and sorted data has already been uploaded to the pipeline for analysis via the machine learner. Because of permission issues, the marker does not have access to the Instrumentation Science Hubble data base through which the data reduction pipeline downloads it's data. So pre-downloaded, raw files as well as cleaned csv's have been uploaded to the pipeline for use in running this code. 

### The data reduction pipeline Hubble Hunters 

As it stands, the data reduction pipeline must be run by hand. Although I wanted to have the code running cohesively as an installed package, because I decided to pursue a machine learning aspect as well I didn't have time to fully automate it. 

## How to run the pipeline 

### Step 1 

Because the package is not complete yet for download (and when this happens all of these functions will talk to each other and won't need to be run) the marker will have to run all of the functions by hand before using the pipeline.

Start by locating the utils folder. This contains all of the major functions of the pipeline. Then locate ``` archive_search.py```. Run this script once and the pipeline will download raw data straight from the Hubble Legacy Archive. This IS NOT USED ANYMORE but is a good example of what the pipeline can do. The function doctrings are provided below. 

```
def url_retrieve(url, filename):
    """
    A function to use URL's to retrieve information from the Space Telescope Science Institute

    Args:
        url (str): a url for the data base being used
        filename (str): the name of the file storing retrieved data
    """
```

```
def basic_search(ra, dec, instrument, search_rad):
    """
    Basic search for a given field and instrument in the archive

    Args:
        ra (int): Right Ascension of the field
        dec (int): Declination of the field
        instrument (str): Which Hubble camera you'd like to use
        search_rad (int): How large the cone search should be in degrees
    """
```

### Step 2

Now locate the ``` catalog.py ``` script, and run the whole thing once. This will load the csv parser.

```
def export_csv(data, col_names, fname, save_path):
    """
    Used to export any data you want to process in R or any other external program into a
    friendly csv file even just for visualisation

    Args:
        data (str): a pandas data frame of the data you wish to save
        col_names (str): the column names of the data you are saving
        fname (str): the file name to save to
        save_path (str): where you'd like to save the information
    """
``` 

### Step 3 

Locate the file ```conditinal_pipeline.py``` and run this once to load the conditional search function as shown below. 
   
```
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
```

### Step 4 

Now locate the file ```photometry.py	```. This file will calibrate the data from hubble into proper AB magnitudes and physical fluxes from instrumental magnitudes, and clean the data from bias and darks etc. 

To run this you will need to change the directory  `home_path = "/Users/Physarah/Desktop/Hubble-CIB/"` to where ever you have saved the Hubble-CIB folder downloaded directly from GitHub

```
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
```

###Step 5 

Finally, locate the `time_date.py` file and run this once. Your data is now calibrated and ready to go. If this didn't work, don't worry. The data is already cleaned and ready to be used in the machine learner located in the `calibrated_csv` folder from previous runnings of the pipeline. 

```
def date_time_maker(start_time, end_time):
    """
    A function that takes the field exposure start and end times out of the the csv and
    into a form that can be manipulated

    Args:
        start_time (str): the time and date of the start of the exposure
        end_time (str): the time and date of the end of an exposure

    Returns:
        start_combined: a time + date object for the start of an observation
        end_combined: a time + date object for the end of an observation    
    """
```

## How to run the machine leaner 

The machine learner operates separately from the pipeline and is performed in R. Open up R studio and locate in the package `Hubble_CIB/machine_learner/knn/knn_learner.R`. Change the first part of the object deep sky by setting it to where you have saved Hubble-CIB i.e. `deep_sky <- read.csv("/Users/Physarah/Desktop/Hubble-CIB` 
You can now go ahead and run this part of the code line by line without an issue.

Now locate `Hubble_CIB/machine_learner/linear_regression/regression_learner.R` and as above change the directories. Similarly, this should run without a glitch provided the directories are set properly. 

### That's all folks !!!






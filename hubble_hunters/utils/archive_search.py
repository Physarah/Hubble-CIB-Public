import urllib
import requests
import contextlib
import io
from astropy.coordinates import SkyCoord

def url_retrieve(url, filename):
    with contextlib.closing(requests.get(url, stream=True)) as r:
        r.raise_for_status()
        with io.open(filename, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=8 * 1024):
                fd.write(chunk)
    return filename, r.headers

def basic_search(ra, dec, instrument, search_rad):
    ra_dec = SkyCoord(ra, dec, frame='icrs', unit='deg')
    const_name = SkyCoord.get_constellation(ra_dec)
    url = "https://archive.stsci.edu/"+instrument+"/search.php?RA="+str(ra)+"&DEC="+str(dec)+"&radius="+str(search_rad)+".&max_records=1000&outputformat=CSV&action=Search"
    filename = "/Users/Physarah/Desktop/ASTRO/Hubble-CIB/hubble_hunters/data/archive_out_raw/"+const_name+"_"+instrument+"_"+str(ra)+"_"+str(dec)+".txt"
    url_retrieve(url,filename)

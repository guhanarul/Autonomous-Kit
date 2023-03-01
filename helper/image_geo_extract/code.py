from exif import Image
import csv
from csv import writer
import os
from os import listdir
import pathlib
import pandas as pd

def decimal_coords(coords, ref):
 decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
 if ref =="S" or ref =="W":
     decimal_degrees = -decimal_degrees
 return decimal_degrees
def image_coords(path):
    with open(path,'rb') as src:
        img=Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref))
            return coords
        except AttributeError:
            return 'No Coordinates'
    else:
        return "this image doesn't contain geotag"

#print(image_coords(path))
folder_name="images"
for images in os.listdir(folder_name):
    if(images.endswith(".jpg")):
        with open('geo.csv','a') as c_obj:
                writer(c_obj).writerow([pathlib.Path(images),image_coords(f"images/{pathlib.Path(images)}")])

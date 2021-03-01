import os
import fnmatch

INPUT_FOLDER="SFMAPS"
OUTPUT_FOLDER= "wgs84"

def findRasters (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield file

for shapefile in findRasters(INPUT_FOLDER, '*.shp'):
    newFile = shapefile[:-4]
    inShape = INPUT_FOLDER + '/' + shapefile	
    outShape = OUTPUT_FOLDER +'/' + newFile + '_wgs84.shp'
    cmd = 'ogr2ogr -t_srs EPSG:4326 %s %s' % (outShape, inShape)
    os.system(cmd)

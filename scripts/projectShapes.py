import os
import fnmatch

INPUT_FOLDER="."
OUTPUT_FOLDER= "wgs84"
if not os.path.exists('wgs84'):
    os.makedirs('wgs84')

def findRasters (path, filter):
    for root, dirs, files in os.walk('.'):
        for file in fnmatch.filter(files, filter):
            yield file
        break


for shapefile in findRasters(INPUT_FOLDER, '*.shp'):
    newFile = shapefile[:-4]
    inShape = INPUT_FOLDER + '/' + shapefile	
    outShape = OUTPUT_FOLDER +'/' + newFile + '_wgs84.shp'
    cmd = 'ogr2ogr -t_srs EPSG:4326 %s %s' % (outShape, inShape)
    os.system(cmd)

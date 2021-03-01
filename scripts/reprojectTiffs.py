import os
import fnmatch

INPUT_FOLDER="SFMAPS"
OUTPUT_FOLDER= "wgs84"

def findRasters (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield file

for raster in findRasters(INPUT_FOLDER, '*.tif'):
    newFile = raster[:-4]
    inRaster = INPUT_FOLDER + '/' + raster
    outRaster = OUTPUT_FOLDER +'/' + newFile + '_wgs84.tif'
    cmd = 'gdalwarp -t_srs EPSG:4326 -te xmin ymin xmax ymax -dstalpha -overwrite %s %s' % (inRaster, outRaster)
    os.system(cmd)

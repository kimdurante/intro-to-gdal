import os
import fnmatch

CLIP= "sf_94109.geojson"
INPUT_FOLDER="SFMAPS"
OUTPUT_FOLDER= "clipped"

def findRasters (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield file

for raster in findRasters(INPUT_FOLDER, '*.tif'):
    inRaster = INPUT_FOLDER + '/' + raster
    outRaster = OUTPUT_FOLDER + '/clip_' + raster
    cmd = 'gdalwarp -q -cutline %s -crop_to_cutline -dstalpha -overwrite %s %s' % (CLIP, inRaster, outRaster)
    os.system(cmd)

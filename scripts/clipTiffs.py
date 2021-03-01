import os
import fnmatch

CLIP= "sf_94109.geojson"
INPUT_FOLDER="."
OUTPUT_FOLDER= "clipped"
if not os.path.exists('clipped'):
    os.makedirs('clipped')

def findRasters (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield file
        break
for raster in findRasters(INPUT_FOLDER, '*.tif'):
    newFile = raster[:-4]
    inRaster = INPUT_FOLDER + '/' + raster
    outRaster = OUTPUT_FOLDER +'/' + newFile + '_clipped.tif'
    cmd = 'gdalwarp -q -cutline %s -crop_to_cutline -dstalpha -overwrite %s %s' % (CLIP, inRaster, outRaster)
    os.system(cmd)

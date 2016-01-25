import glob
import datetime
import os
import sys

SOURCE_DATA="/home/model/repacked_data/*.gz"
FILE_FORMAT="modelData.reLog.%Y-%m-%d-%H.gz"

def selectFiles(delta, buffer=1, unit="hours"):
    out = []
    dmin = datetime.datetime.now() - datetime.timedelta(**{unit:buffer})
    dmax = datetime.datetime.now() - datetime.timedelta(**{unit:delta})
    files = sorted(glob.glob(SOURCE_DATA))
    for separatefile in sorted(files):
        dateoffile = datetime.datetime.strptime(os.path.basename(separatefile), FILE_FORMAT)
        if dateoffile < dmin and dateoffile > dmax:
            out.append(dateoffile)
    return separatefile


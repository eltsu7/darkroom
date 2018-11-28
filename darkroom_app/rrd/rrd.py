import rrdtool
import time
import os
import datetime
import serial
import glob

rrd_file_suffix = "_sensor.rrd"
default_width = '600'
default_height = '300'

def update(sensor, value):
    rrd_file = str(sensor)+rrd_file_suffix
    if os.path.isfile(rrd_file):
        print("RRD file found!")
    else:
        rrdtool.create(
            rrd_file,
            "--start", "now",
            "--step", "30",
            "RRA:AVERAGE:0.1:360:1000",
            "RRA:AVERAGE:0.1:180:1000",
            "RRA:AVERAGE:0.1:60:1000",
            "RRA:AVERAGE:0.1:30:1000",
            "RRA:AVERAGE:0.1:1:2880",
            "DS:light:GAUGE:4:0:1024")

    rrdtool.update(rrd_file, 'N:'+str(value))

if __name__ == '__main__':
    graph_duration_seconds = 60*60*24

    for data in glob.glob('*.rrd'):
        filename = data[:-4]+'.png'
        rrdtool.graph(filename,
                    '--imgformat', 'PNG',
                    '--width', default_width,
                    '--height', default_height,
                    '--start', "-"+str(graph_duration_seconds),
                    '--end', "-1",
                    '--vertical-label', 'Luminance',
                    '--title', 'Darkrooms\'s light level for last day',
                    'DEF:Luminance='+str(data)+':light:AVERAGE',          
                    'LINE2:Luminance#35962b:Luminance',
                    )
import os
import subprocess
import shutil
import sys

paths = sys.argv[1:]
pngs = []

# clean up
shutil.rmtree('.\input')
os.makedirs('.\input')

# get all files
for path in paths:
    if os.path.isdir(path):
        for (root, dirs, files) in os.walk(path):
            for file in files:
                if file[-3:] == 'png':
                    pngs.append(file)

    if os.path.isfile(path):
        if path[-3:] == 'png':
            pngs.append(path)

print('{0} png files found\n'.format(len(pngs)))

# copy files to input dir
for png in pngs:
    shutil.copy(png, '.\input')

# convert icons
subprocess.call('.\png2ico.exe -i .\input -o .\output -s 16 32bpp -s 32 32pp -s 48 32bpp  -s 96 32bpp -s 128 32bpp -s 512 32bpp')

# open output directory
os.startfile('.\output')
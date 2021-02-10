#!/bin/bash
#
# script to generate the CCU addon package.

# generate tempdir
mkdir -p tmp/
rm -rf tmp/*

# copy all relevant stuff
cp -a update_script tmp/
cp -a VERSION tmp/
cp -a www tmp/
cp -a rc.d tmp/
cp -a profile.d tmp/
cp -a licenses tmp/



# *** arm based binarys (armv7l) *** 
mkdir tmp/arm
# copy python3.9
cp -a arm/python3.9 tmp/arm/


###############################################################

# generate archive
cd tmp
tar --owner=root --group=root --exclude=.DS_Store -czvf ../PythonCCU-$(cat ../VERSION).tar.gz *
cd ..
rm -rf tmp


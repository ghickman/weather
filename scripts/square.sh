#!/bin/bash
#specify lon+lat, NE corner and SW corner.  1-3 decimal places, please

INPUT=-
E=$1
N=$2
W=$3
S=$4
for d in $E $N $W $S ; do
if echo "$d"|grep -qv -e '-\?[0-9]\{1,3\}\.[0-9]\{1,3\}$' ; then
        echo "$d not a lon/lat reading"
        exit -1
fi
done
E=$(echo $E|sed 's_\.[0-9]$_\00_;s_\.[0-9][0-9]$_\00_;s_\.__')
N=$(echo $N|sed 's_\.[0-9]$_\00_;s_\.[0-9][0-9]$_\00_;s_\.__')
W=$(echo $W|sed 's_\.[0-9]$_\00_;s_\.[0-9][0-9]$_\00_;s_\.__')
S=$(echo $S|sed 's_\.[0-9]$_\00_;s_\.[0-9][0-9]$_\00_;s_\.__')

echo "bounding box $E $N $W $S"

grep -v "^register" $INPUT | while read line; do

LON=$(echo $line | cut -d, -f14|sed 's_\.[0-9]$_\00_;s_\.[0-9][0-9]$_\00_;s_\.__')
LAT=$(echo $line | cut -d, -f15|sed 's_\.[0-9]$_\00_;s_\.[0-9][0-9]$_\00_;s_\.__')
if [ $LAT -le $N -a $LAT -ge $S -a $LON -ge $E -a $LON -le $W ] ; then
        echo $line
fi
done

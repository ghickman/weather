#!/bin/bash
#specify start and end ISO8601 dates (no time on the end)

INPUT=-
FROM=$1
if echo "$FROM"|grep -qv "^[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}$" ; then
        echo "$FROM not an ISO8601 date"
        exit -1
fi
FROM=$(echo $1|tr -d "-")
TO=$2
if echo "$TO"|grep -qv "^[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}$" ; then
        echo "$FROM not an ISO8601 date"
        exit -1
fi
TO=$(echo $2|tr -d "-")
grep -q "^register" $INPUT | while read line; do

START=$(echo $line | cut -d, -f4|tr -d "-")
if [ $FROM -le $START -a $TO -ge $START ] ; then
        echo $line
fi
done

#! /bin/bash

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/mapr/lib

python ./viewer/myflask.py &

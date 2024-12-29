#!/bin/bash

# Define the execution path for the LHM.

export HSTREAMING=/opt/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar

# Actual program is here

yarn jar $HSTREAMING   -files pymapper.py,pyreducer.py   -mapper pymapper.py   -reducer pyreducer.py   -input /user/hands-on/books-input   -output /user/hands-on/books-output

#!/bin/bash
find ./videos -name *.mp4 | sed 's:\ :\\\ :g'| sed 's/^/file /' > fl.txt; ./ffmpeg -f concat -i fl.txt -c copy output.mp4; rm fl.txt

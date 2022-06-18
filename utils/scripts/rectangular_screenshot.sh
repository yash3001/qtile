#!/bin/bash

TIME=$(date -R | grep ..:..:.. -o)
scrot -q 100 -sf "%Y-%m-%d_${TIME}.png" -e 'mv $f ~/Pictures/Screenshots/'

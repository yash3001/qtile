#!/bin/bash

amixer -qD pulse set Master 1+ toggle && pkill -RTMIN+11 dwmblocks

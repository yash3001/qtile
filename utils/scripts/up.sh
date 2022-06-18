#!/bin/bash

amixer -q set Master 5%+ && pkill -RTMIN+11 dwmblocks

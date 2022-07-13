#!/bin/bash

pacman_updates=$(checkupdates | wc -l)
aur_updates=$(checkupdates-aur | wc -l)
total=$((pacman_updates + aur_updates))
echo -n $total

#!/usr/bin/zsh

ans=$(echo -e "no\nyes" | dmenu -c -h 40 -l 2 -p "Do you want suspend?")

if [[ ($ans == "yes") ]]
then
    systemctl suspend
fi
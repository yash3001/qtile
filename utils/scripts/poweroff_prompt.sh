#!/usr/bin/zsh

ans=$(echo -e "no\nyes" | dmenu -c -h 40 -l 2 -p "Do you want to go?")

if [[ ($ans == "yes") ]]
then
    systemctl poweroff
fi
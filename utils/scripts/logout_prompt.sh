#!/usr/bin/zsh

ans=$(echo -e "no\nyes" | dmenu -c -h 40 -p "Do you want to logout?")

if [[ ($ans == "yes") ]]
then
    wm=$(wmctrl -m | awk 'NR==1{print $2, $3, $4, $5}')
    wm=$(sed 's/[ ]*$//' <<<"$wm")
    killall $wm
fi
#!/bin/sh

choice=$(echo -e "logout\nshutdown\nrestart" | dmenu -c -h 40 -l 3)

if [[ ($choice == "logout") ]]
then
    ans=$(echo -e "no\nyes" | dmenu -c -h 40 -p "Do you want to logout")
    
    if [[ ($ans == "yes") ]]
    then
        killall dwm
    fi
fi

if [[ ($choice == "shutdown") ]]
then
    ans=$(echo -e "no\nyes" | dmenu -c -h 40 -p "Do you want to shutdown")
    
    if [[ ($ans == "yes") ]]
    then
        poweroff
    fi
fi

if [[ ($choice == "restart") ]]
then
    ans=$(echo -e "no\nyes" | dmenu -c -h 40 -p "Do you want to reboot")
    
    if [[ ($ans == "yes") ]]
    then
        reboot
    fi
fi

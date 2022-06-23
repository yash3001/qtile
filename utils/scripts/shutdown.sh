#!/usr/bin/zsh

choice=$(echo -e "Logout\nShutdown\nRestart" | dmenu -c -h 40 -l 3)

if [[ ($choice == "Logout") ]]
then
    ans=$(echo -e "no\nyes" | dmenu -c -h 40 -p "Do you want to logout?")
    
    if [[ ($ans == "yes") ]]
    then
        wm=$(wmctrl -m | awk 'NR==1{print $2, $3, $4, $5}')
        wm=$(sed 's/[ ]*$//' <<<"$wm")
        killall $wm
    fi
fi

if [[ ($choice == "Shutdown") ]]
then
    # ans=$(echo -e "No\nYes" | dmenu -c -h 40 -p "Do you want to shutdown")
    ans=$(echo -e "no\nyes" | dmenu -c -h 40 -p "Do you want to go?")
    
    if [[ ($ans == "yes") ]]
    then
        poweroff
    fi
fi

if [[ ($choice == "Restart") ]]
then
    ans=$(echo -e "no\nyes" | dmenu -c -h 40 -p "Do you want to reboot?")
    
    if [[ ($ans == "yes") ]]
    then
        reboot
    fi
fi

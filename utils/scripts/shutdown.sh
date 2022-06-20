#!/usr/bin/zsh

choice=$(echo -e "Logout\nShutdown\nRestart" | dmenu -c -h 40 -l 3)

if [[ ($choice == "Logout") ]]
then
    ans=$(echo -e "No\nYes" | dmenu -c -h 40 -p "Do you want to logout")
    
    if [[ ($ans == "Yes") ]]
    then
        wm=$(wmctrl -m | awk 'NR==1{print $2, $3, $4, $5}')
        wm=$(sed 's/[ ]*$//' <<<"$wm")
        killall $wm
    fi
fi

if [[ ($choice == "Shutdown") ]]
then
    ans=$(echo -e "No\nYes" | dmenu -c -h 40 -p "Do you want to shutdown")
    
    if [[ ($ans == "Yes") ]]
    then
        poweroff
    fi
fi

if [[ ($choice == "Restart") ]]
then
    ans=$(echo -e "No\nYes" | dmenu -c -h 40 -p "Do you want to reboot")
    
    if [[ ($ans == "Yes") ]]
    then
        reboot
    fi
fi

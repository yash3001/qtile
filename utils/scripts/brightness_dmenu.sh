#!/usr/bin/zsh

while [ true ]
do
    choice=$(echo -e "Increase 1%\nDecrease 1%\nExit" | dmenu -c -h 40 -l 3 -p "Brightness:")

    if [[ ($choice == "Increase 1%") ]]
    then
        brightnessctl s 1%+
    fi

    if [[ ($choice == "Decrease 1%") ]]
    then
        brightnessctl s 1%-
    fi

    if [[ ($choice == "Exit") ]]
    then
        break
    fi

    if [[ ($choice == "") ]]
    then
        break
    fi
done
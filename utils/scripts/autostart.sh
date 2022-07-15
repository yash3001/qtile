#!/usr/bin/zsh

# Compositor
compton --config ~/.config/compton/compton.conf &

# Conky
killall conky &> /dev/null
conky -c ~/.config/qtile/apps/conky/time.lua &
conky -c ~/.config/qtile/apps/conky/sysinfo.lua &

# Start lxsession for theme
lxsession &

# Set Wallpaper
nitrogen --restore &

# Start the notification daemon
twmnd &

# Start clipmenu daemon
clipmenud &

# Start xfce4 power manager
xfce4-power-manager &

# For reverse scrolling and tap to touch
xinput set-prop 'ELAN1203:00 04F3:307A Touchpad' 'libinput Tapping Enabled' 1 &
xinput set-prop 'ELAN1203:00 04F3:307A Touchpad' 'libinput Natural Scrolling Enabled' 1 &

#!/usr/bin/zsh

if ! pgrep -x cmus ; then
  st -e cmus
else
  cmus-remote -n
fi

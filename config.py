# ------------------------------------------------------
# ---------------------- Imports -----------------------
# ------------------------------------------------------

import os
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Match, Screen
from libqtile.config import EzKey as Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal




# ------------------------------------------------------
# ------------------ Global Variables ------------------
# ------------------------------------------------------

mod = "mod4"
terminal = guess_terminal()

shutdown = os.path.join(os.path.dirname(__file__), "utils/scripts/shutdown.sh")
screenshot = os.path.join(os.path.dirname(__file__), "utils/scripts/screenshot.sh")
rectangular_screenshot = os.path.join(os.path.dirname(__file__), "utils/scripts/rectangular_screenshot.sh")
volume_up = os.path.join(os.path.dirname(__file__), "utils/scripts/vol_up.sh")
volume_down = os.path.join(os.path.dirname(__file__), "utils/scripts/vol_down.sh")
volume_toggle_mute = os.path.join(os.path.dirname(__file__), "utils/scripts/vol_mute.sh")
clipmenu = os.path.join(os.path.dirname(__file__), "utils/scripts/clipmenu.sh")


# ------------------------------------------------------
# -------------------- Key Bindings --------------------
# ------------------------------------------------------

keys = [
    # Switch between windows (Move Focus)
    Key(
        "M-h",
        lazy.layout.left(),
        desc="Move focus to left"
    ),
    Key(
        "M-<Left>",
        lazy.layout.left(),
        desc="Move focus to left"
    ),
    Key(
        "M-l",
        lazy.layout.right(),
        desc="Move focus to right"
    ),
    Key(
        "M-<Right>",
        lazy.layout.right(),
        desc="Move focus to right"
    ),
    Key(
        "M-j",
        lazy.layout.down(),
        desc="Move focus down"
    ),
    Key(
        "M-<Down>",
        lazy.layout.down(),
        desc="Move focus down"
    ),
    Key(
        "M-k", 
        lazy.layout.up(),
        desc="Move focus up"
    ),
    Key(
        "M-<Up>",
        lazy.layout.up(),
        desc="Move focus up"
    ),
    Key(
        "M-S-<space>",
        lazy.layout.next(),
        desc="Move window focus to other window"
    ),

    # Move windows between left/right columns or move up/down in current stack.
    Key(
        "M-S-h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    Key(
        "M-S-<Left>",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    Key(
        "M-S-l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),
    Key(
        "M-S-<Right>",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),
    Key(
        "M-S-j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),
    Key(
        "M-S-<Down>",
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),
    Key(
        "M-S-k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),
    Key(
        "M-S-<Up>",
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),

    # Grow windows. If current window is on the edge of screen and direction will be to screen edge - window would shrink.
    Key(
        "A-C-h",
        lazy.layout.grow_left(),
        lazy.layout.decrease_ratio(),
        desc="Grow window to the left"
    ),
    Key(
        "A-C-<Left>",
        lazy.layout.grow_left(),
        lazy.layout.decrease_ratio(),
        desc="Grow window to the left"
    ),
    Key(
        "A-C-l",
        lazy.layout.grow_right(),
        lazy.layout.increase_ratio(),
        desc="Grow window to the right"
    ),
    Key(
        "A-C-<Right>",
        lazy.layout.grow_right(),
        lazy.layout.increase_ratio(),
        desc="Grow window to the right"
    ),
    Key(
        "A-C-j",
        lazy.layout.grow_down(),
        lazy.layout.increase_ratio(),
        desc="Grow window down"
    ),
    Key(
        "A-C-<Down>",
        lazy.layout.grow_down(),
        lazy.layout.increase_ratio(),
        desc="Grow window down"
    ),
    Key(
        "A-C-k",
        lazy.layout.grow_up(),
        lazy.layout.decrease_ratio(),
        desc="Grow window up"
    ),
    Key(
        "A-C-<Up>",
        lazy.layout.grow_up(),
        lazy.layout.decrease_ratio(),
        desc="Grow window up"
    ),
    Key(
        "A-C-<Return>",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
    ),
    

    Key(
        "M-S-<Return>",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"
    ),

    # Launching Applications
    Key(
        "M-<Return>",
        lazy.spawn(terminal),
        desc="Launch terminal"
    ),
    Key(
        "M-A-b",
        lazy.spawn("firefox"),
        desc="Launch Firefox"
    ),
    Key(
        "M-A-c",
        lazy.spawn("code"),
        desc="Launch VsCode"
    ),
    Key(
        "M-A-d",
        lazy.spawn("discord"),
        desc="Launch Discord"
    ),
    Key(
        "M-A-s",
        lazy.spawn("spotify"),
        desc="Launch Spotify"
    ),
    Key(
        "M-S-l",
        lazy.spawn("i3lock-fancy"),
        desc="Launch i3lock-fancy"
    ),
    Key(
        "M-A-c",
        lazy.spawn(clipmenu),
        desc="Launch clipmenu"
    ),
    Key(
        "M-A-x",
        lazy.spawn("dmenu_run -h 40 -c -l 10"),
        desc="Launch Dmenu"
    ),
    Key(
        "M-S-s",
        lazy.spawn(shutdown),
        desc="Launch shutdown menu"
    ),
    
    
    # Toggle between different layouts
    Key(
        "M-<space>",
        lazy.next_layout(),
        desc="Toggle between layouts"
    ),

    # Toggle between recent groups
    Key(
        "M-<Tab>",
        lazy.screen.toggle_group(),
        desc="Toggle between groups"
    ),
    
    # Kill window
    Key(
        "M-q",
        lazy.window.kill(),
        desc="Kill focused window"
    ),
    
    # Reload/Shutdown Qtile
    Key(
        "M-A-r",
        lazy.reload_config(),
        desc="Reload the config"
    ),
    Key(
        "M-A-q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
    ),
    
    # Spawn cmd launcher
    Key(
        "M-r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"
    ),

    # Scripts that i wrote
]



# ------------------------------------------------------
# ----------------------- Groups -----------------------
# ------------------------------------------------------

groups = [
    Group("1", matches=[Match(wm_class=["Firefox"])]),
    Group("2"),
    Group("3", matches=[Match(wm_class=["Code"])]),
    Group("4", matches=[Match(wm_class=["org.gnome.Nautilus"])]),
    Group("5", matches=[Match(wm_class=["discord"])]),
    Group("6"),
    Group("7"),
    Group("8"),
    Group("9"),
    Group("10")
]

# allow mod4+1 through mod4+0 to bind to groups;
# MOD4 + [index(1-0)] : Switch to Group [index(1-0)]
# MOD4 + Shift + [index(1-0)] : Move focused window to Group [index(1-0)]
# from libqtile.dgroups import simple_key_binder
# dgroups_key_binder = simple_key_binder("mod3")

for i in range(len(groups)):
    ind = i+1
    if ind == 10:
        ind = 0

    keys.extend(
        [
            # mod4 + index of group = switch to group
            Key(
                "M-" + str(ind), 
                lazy.group[groups[i].name].toscreen(), 
                desc="Switch to group {}".format(groups[i].name),
            ),

            # mod4 + shift + index of group = switch to & move focused window to group
            Key(
                "M-S-" + str(ind),
                lazy.window.togroup(groups[i].name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(groups[i].name),
            ),

            # mod1 + alt + shift + index of group = move focused window to group
            Key(
                "M-S-A-" + str(ind), 
                lazy.window.togroup(groups[i].name),
                desc="move focused window to group {}".format(groups[i].name)
            ),
        ]
    )



# ------------------------------------------------------
# ---------------------- Layouts -----------------------
# ------------------------------------------------------

layouts = [
    layout.Columns(
        border_focus='#0000ff',         # Border colour(s) for the focused window.
        border_focus_stack='#0000ff',   # Border colour(s) for the focused window in stacked columns.
        border_normal='#000000',        # Border colour(s) for un-focused windows.
        border_normal_stack='#000000',  # Border colour(s) for un-focused windows in stacked columns.
        border_on_single=True,          # Draw a border when there is one only window.
        border_width=1,                 # Border width.
        fair=False,                     # Add new windows to the column with least windows.
        grow_amount=10,                 # Amount by which to grow a window/column.
        insert_position=0,              # Position relative to the current window where new ones are inserted (0 means right above the current window, 1 means right after).
        margin=[5,5,5,5],               # Margin of the layout (int or list of ints [N E S W]).
        margin_on_single=[5,5,5,5],     # Margin when only one window. (int or list of ints [N E S W]).
        num_columns=2,                  # Preferred number of columns.
        split=True,                     # New columns presentation mode.
        wrap_focus_columns=True,        # Wrap the screen when moving focus across columns.
        wrap_focus_rows=True,           # Wrap the screen when moving focus across rows.
        wrap_focus_stacks=True          # Wrap the screen when moving focus across stacked.
    ),

    layout.Max(),

    layout.Tile(
        add_after_last=False,           # Add new clients after all the others. If this is True, it overrides add_on_top.
        add_on_top=True,                # Add new clients before all the others, potentially pushing other windows into slave stack.
        border_focus='#0000ff',         # Border colour(s) for the focused window.
        border_normal='#000000',        # Border colour(s) for the unfocused window.
        border_on_single=True,          # Whether to draw border if there is only one window.
        border_width=1,                 # Border width.
        expand=True,                    # Expand the master windows to the full screen width if no slaves are present.
        margin=[5,5,5,5],               # Margin of the layout (int or list of ints [N E S W])
        margin_on_single=True,          # Whether to draw margin if there is only one window.
        master_length=1,                # Amount of windows displayed in the master stack. Surplus windows will be moved to the slave stack.
        master_match=None,              # A Match object defining which window(s) should be kept masters (single or a list of Match-objects).
        max_ratio=0.85,                 # Maximum width of master windows.
        mn_ratio=0.15,                  # Minimum width of master windows.
        ratio=0.5,                      # Width-percentage of screen size reserved for master windows.
        ratio_increment=0.01,           # By which amount to change ratio when cmd_decrease_ratio or cmd_increase_ratio are called.
        shift_windows=True              # Allow to shift windows within the layout. If False, the layout will be rotated instead.
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]



# ------------------------------------------------------
# ---------------------- Widgets -----------------------
# ------------------------------------------------------

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]




# ------------------------------------------------------
# ------------------- Mouse Bindings -------------------
# ------------------------------------------------------
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]




# ------------------------------------------------------
# ------------------------ Misc ------------------------
# ------------------------------------------------------

dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
# wmname = "LG3D"
wmname = "qtile"

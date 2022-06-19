# ------------------------------------------------------
# ---------------------- Imports -----------------------
# ------------------------------------------------------

import os
import subprocess
from libqtile import bar, layout, widget, hook
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
brightness_up = os.path.join(os.path.dirname(__file__), "utils/scripts/brightness_up.sh")
brightness_down = os.path.join(os.path.dirname(__file__), "utils/scripts/brightness_down.sh")
volume_up = os.path.join(os.path.dirname(__file__), "utils/scripts/volume_up.sh")
volume_down = os.path.join(os.path.dirname(__file__), "utils/scripts/volume_down.sh")
volume_mute = os.path.join(os.path.dirname(__file__), "utils/scripts/volume_mute.sh")
clipmenu = os.path.join(os.path.dirname(__file__), "utils/scripts/clipmenu.sh")
autostart = os.path.join(os.path.dirname(__file__), "utils/scripts/autostart.sh")



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
        "M-A-v",
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
    Key(
        "M-S-p",
        lazy.spawn(screenshot),
        desc="Take Fullscreen Screenshot"
    ),
    Key(
        "M-S-C-p",
        lazy.spawn(rectangular_screenshot),
        desc="Take Fullscreen Screenshot"
    ),
    Key(
        "<XF86MonBrightnessUp>",
        lazy.spawn(brightness_up),
        desc="Increase Brightness"
    ),
    Key(
        "<XF86MonBrightnessDown>",
        lazy.spawn(brightness_down),
        desc="Decrease Brightness"
    ),
    Key(
        "<XF86AudioRaiseVolume>",
        lazy.spawn(volume_up),
        desc="Increase Volume"
    ),
    Key(
        "<XF86AudioLowerVolume>",
        lazy.spawn(volume_down),
        desc="Decrease Volume"
    ),
    Key(
        "<XF86AudioMute>",
        lazy.spawn(volume_mute),
        desc="Toogle Mute Volume"
    ),
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

    # layout.Stack(
    #     autosplit=False,                # Auto split all new stacks.
    #     border_focus='#0000ff',         # Border colour(s) for the focused window.
    #     border_normal='#000000',        # Border colour(s) for un-focused windows.
    #     border_width=1,                 # Border width.
    #     fair=False,                     # Add new windows to the stacks in a round robin way.
    #     margin=0,                       # Margin of the layout (int or list of ints [N E S W]).
    #     num_stacks=2,                   # Number of stacks.
    # ),

    # layout.Bsp(
    #     border_focus='#881111',         # Border colour(s) for the focused window.
    #     border_normal='#220000',        # Border colour(s) for un-focused windows.
    #     border_on_single=False,         # Draw border when there is only one window.
    #     border_width=2,                 # Border width.
    #     fair=True,                      # New clients are inserted in the shortest branch.
    #     grow_amount=10,                 # Amount by which to grow a window/column.
    #     lower_right=True,               # New client occupies lower or right subspace.
    #     margin=0,                       # Margin of the layout (int or list of ints [N E S W]).
    #     margin_on_single=None,          # Margin when there is only one window (int or list of ints [N E S W], 'None' to use 'margin' value).
    #     ratio=1.6,                      # Width/height ratio that defines the partition direction.
    # ),

    # layout.Matrix(
    #     border_focus='#0000ff',         # Border colour(s) for the focused window.
    #     border_normal='#000000',        # Border colour(s) for un-focused windows.
    #     border_width=1,                 # Border width.
    #     columns=2,                      # Number of columns.
    #     margin=0,                       # Margin of the layout (int or list of ints [N E S W]).
    # ),

    # layout.MonadTall(
    #     align=0,                        # Which side master plane will be placed (one of MonadTall._left or MonadTall._right).
    #     border_focus='#ff0000',         # Border colour(s) for the focused window.
    #     border_normal='#000000',        # Border colour(s) for un-focused windows.
    #     border_width=2,                 # Border width.
    #     change_ratio=0.05,              # Resize ratio.
    #     change_size=20,                 # Resize change in pixels.
    #     margin=0,                       # Margin of the layout.
    #     max_ratio=0.75,                 # The percent of the screen-space the master pane should occupy at maximum.
    #     min_ratio=0.25,                 # The percent of the screen-space the master pane should occupy at minimum.
    #     min_secondary_size=85,          # Minimum size in pixel for a secondary pane window.
    #     new_client_position='after_current' # Place new windows: after_current - after the active window. before_current - before the active window, top - at the top of the stack, bottom - at the bottom of the stack.
    #     ratio=0.5,                      # The percent of the screen-space the master pane should occupy by default.
    #     single_border_width=None,       # Border width for single window.
    #     single_margin=None,             # Margin size for single window.
    # ),

    # layout.MonadWide(
    #     align=0,                        # Which side master plane will be placed (one of MonadTall._left or MonadTall._right).
    #     border_focus='#ff0000',         # Border colour(s) for the focused window.
    #     border_normal='#000000',        # Border colour(s) for un-focused windows.
    #     border_width=2,                 # Border width.
    #     change_ratio=0.05,              # Resize ratio.
    #     change_size=20,                 # Resize change in pixels.
    #     margin=0,                       # Margin of the layout.
    #     max_ratio=0.75,                 # The percent of the screen-space the master pane should occupy at maximum.
    #     min_ratio=0.25,                 # The percent of the screen-space the master pane should occupy at minimum.
    #     min_secondary_size=85,          # Minimum size in pixel for a secondary pane window.
    #     new_client_position='after_current', # Place new windows: after_current - after the active window. before_current - before the active window, top - at the top of the stack, bottom - at the bottom of the stack.
    #     ratio=0.5,                      # The percent of the screen-space the master pane should occupy by default.
    #     single_border_width=None,       # Border width for single window.
    #     single_margin=None,             # Margin size for single window.
    # ),

    # layout.RatioTile(
    #     border_focus='#0000ff',         # Border colour(s) for the focused window.
    #     border_normal='#000000',        # Border colour(s) for un-focused windows.
    #     border_width=1,                 # Border width.
    #     fancy=False,                    # Use a different method to calculate window sizes.
    #     margin=0,                       # Margin of the layout (int or list of ints [N E S W]).
    #     ratio=1.618,                    # Ratio of the tiles.
    #     ratio_increment=0.1             # Amount to increment per ratio increment.
    # ),

    # layout.TreeTab(
    #     active_bg='000080',             # Background color of active tab.
    #     active_fg='ffffff',             # Foreground color of active tab.
    #     bg_color='000000',              # Background color of tabs.
    #     border_width=2,                 # Width of the border.
    #     font='sans',                    # Font.
    #     fontshadow=None,                # font shadow color, default is None (no shadow).
    #     fontsize=14,                    # Font pixel size.
    #     inactive_bg='606060',           # Background color of inactive tab.
    #     inactive_fg='ffffff',           # Foreground color of inactive tab.
    #     level_shift=8,                  # Shift for children tabs.
    #     margin_left=6,                  # Left margin of tab panel.
    #     margin_y=6,                     # Vertical margin of tab panel.
    #     padding_left=6,                 # Left padding for tabs.
    #     padding_x=6,                    # Left padding for tab label.
    #     padding_y=2,                    # Top padding for tab label.
    #     panel_width=150,                # Width of the left panel.
    #     place_right=False,              # Place the tab panel on the right side.
    #     previous_on_rm=False,           # Focus previous window on close instead of first.
    #     section_bottom=6,               # Bottom margin of section.
    #     section_fg='ffffff',            # Color of section label.
    #     section_fontsize=11,            # Font pixel size of section label.
    #     section_left=4,                 # Left margin of section label.
    #     section_padding=4,              # Bottom of margin section label.
    #     section_top=4,                  # Top margin of section label.
    #     sections=['Default'],           # Foreground color of inactive tab.
    #     urgent_bg='ff0000',             # Background color of urgent tab.
    #     urgent_fg='ffffff',             # Foreground color of urgent tab.
    #     vspace=2,                       # Space between tabs.
    # ),

    # layout.VerticalTile(
    #     border_focus='#FF0000',         # Border color(s) for the focused window.
    #     border_normal='#FFFFFF',        # Border color(s) for un-focused windows.
    #     border_width=1,                 # Border width.
    #     margin=0,                       # Border margin (int or list of ints [N E S W]).
    # ),

    # layout.Zoomy(
    #     columnwidth=150,                # Width of the right column.
    #     margin=0,                       # Margin of the layout (int or list of ints [N E S W]).
    #     property_big='1.0',             # Property value to set on normal window (X11 only).
    #     property_name='ZOOM',           # Property to set on zoomed window (X11 only).
    #     property_small='0.1',           # Property value to set on zoomed window (X11 only).
    # ),

    # layout.Floating(
    #     border_focus='#0000ff',         # Border colour(s) for the focused window.
    #     border_normal='#000000',        # Border colour(s) for un-focused windows.
    #     border_width=1,                 # Border width.
    #     fullscreen_border_width=0,      # Border width for fullscreen.
    #     max_border_width=0,             # Border width for maximize.
    # ),

    # layout.MonadThreeCol(
    #     align=0,                        # Which side master plane will be placed (one of MonadTall._left or MonadTall._right).
    #     border_focus='#ff0000',         # Border colour(s) for the focused window.
    #     border_normal='#000000',        # Border colour(s) for un-focused windows.
    #     border_width=2,                 # Border width.
    #     change_ratio=0.05,              # Resize ratio.
    #     change_size=20,                 # Resize change in pixels.
    #     main_centered=True,             # Place the main pane at the center of the screen.
    #     margin=0,                       # Margin of the layout.
    #     max_ratio=0.75,                 # The percent of the screen-space the master pane should occupy at maximum.
    #     min_ratio=0.25,                 # The percent of the screen-space the master pane should occupy at minimum.
    #     min_secondary_size=85,          # Minimum size in pixel for a secondary pane window.
    #     new_client_position='top',      # Place new windows: after_current - after the active window. before_current - before the active window, top - at the top of the stack, bottom - at the bottom of the stack.
    #     ratio=0.5,                      # The percent of the screen-space the master pane should occupy by default.
    #     single_border_width=None,       # Border width for single window.
    #     single_margin=None,             # Margin size for single window.
    # ),

    # layout.Slice(
    #     match=None,                     # Match-object describing which window(s) to move to the slice.
    #     side='left',                    # Position of the slice (left, right, top, bottom).
    #     width=256,                      # Slice width.
    # ),

    # layout.Spiral(
    #     border_focus='#0000ff',         # Border colour(s) for the focused window.
    #     border_normal='#000000',        # Border colour(s) for un-focused windows.
    #     border_width=1,                 # Border width.
    #     clockwise=True,                 # Direction of spiral
    #     main_pane='left',               # Location of biggest window 'top', 'bottom', 'left', 'right'
    #     main_pane_ratio=None,           # Ratio for biggest window or 'None' to use same ratio for all windows.
    #     margin=0,                       # Margin of the layout (int or list of ints [N E S W])
    #     new_client_position='top',      # Place new windows: 'after_current' - after the active window, 'before_current' - before the active window, 'top' - in the main pane, 'bottom '- at the bottom of the stack. NB windows that are added too low in the stack may be hidden if there is no remaining space in the spiral.
    #     ratio=0.6180469715698392,       # Ratio of the tiles
    #     ratio_increment=0.1,            # Amount to increment per ratio increment
    # ),
]



# ------------------------------------------------------
# ---------------------- Widgets -----------------------
# ------------------------------------------------------

widget_defaults = dict(
    font="sans",
    fontsize=15,
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
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                # widget.QuickExit(),
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

@hook.subscribe.startup_once
def start_once():
    subprocess.call(autostart)


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

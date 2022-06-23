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
from libqtile.backend.x11 import xkeysyms
from qtile_extras import widget as extra_widget




# ------------------------------------------------------
# ------------------ Global Variables ------------------
# ------------------------------------------------------

mod = "mod4"
terminal = guess_terminal()

shutdown_menu = os.path.join(os.path.dirname(__file__), "utils/scripts/shutdown.sh")
logout_prompt = os.path.join(os.path.dirname(__file__), "utils/scripts/logout_prompt.sh")
poweroff_prompt = os.path.join(os.path.dirname(__file__), "utils/scripts/poweroff_prompt.sh")
suspend_prompt = os.path.join(os.path.dirname(__file__), "utils/scripts/suspend_prompt.sh")
wifi_prompt = os.path.join(os.path.dirname(__file__), "utils/scripts/network_manager_dmenu.py")
screenshot = os.path.join(os.path.dirname(__file__), "utils/scripts/screenshot.sh")
rectangular_screenshot = os.path.join(os.path.dirname(__file__), "utils/scripts/rectangular_screenshot.sh")
brightness_up = os.path.join(os.path.dirname(__file__), "utils/scripts/brightness_up.sh")
brightness_down = os.path.join(os.path.dirname(__file__), "utils/scripts/brightness_down.sh")
volume_up = os.path.join(os.path.dirname(__file__), "utils/scripts/volume_up.sh")
volume_down = os.path.join(os.path.dirname(__file__), "utils/scripts/volume_down.sh")
volume_mute = os.path.join(os.path.dirname(__file__), "utils/scripts/volume_mute.sh")
clipmenu = os.path.join(os.path.dirname(__file__), "utils/scripts/clipmenu.sh")
autostart = os.path.join(os.path.dirname(__file__), "utils/scripts/autostart.sh")

arch_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/arch-icons/arch_light.png")
layout_icon_dir = os.path.join(os.path.dirname(__file__), "utils/icons/layout-icons/dark")
brightness_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/brightness-icons/brightness_light_bold.png")
volume_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/volume-icons/volume_light_bold.png")
bluetooth_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/bluetooth-icons/bluetooth_light_bold.png")
cpu_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/cpu-icons/cpu_dark_bold.png")
memory_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/memory-icons/memory_dark_bold.png")
temperature_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/temperature-icons/terperature_dark_bold.png")
network_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/network-icons/network_light_bold.png")
wifi_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/network-icons/wifi_light_bold.png")
battery_icon_dir = os.path.join(os.path.dirname(__file__), "utils/icons/battery-icons/dark")
clock_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/clock-icons/clock_light_bold.png")
poweroff_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/poweroff-icons/poweroff_dark_bold.png")
logout_icon_path = os.path.join(os.path.dirname(__file__), "utils/icons/logout-icons/logout_dark_bold.png")

# colors = {
#     "black": ['#2C3E50', '#34495E'],
#     'purple': ['#8E44AD', '#9B59B6'],
#     'blue': ['#2980B9', '#3498DB'],
#     'green': ['#27AE60', '#2ECC71'],
#     'cyan': ['#16A085', '#1ABC9C'],
#     'yellow': ['#F39C12', '#F1C40F'],
#     'orange': ['#D35400', '#E67E22'],
#     'red': ['#C0392B', '#E74C3C'],
#     'white': ['#BDC3C7', '#ECF0F1'],
#     'grey': ['#7F8C8D', '#95A5A6']
# }

colors = {
    "black": ['#2C3E50', '#264653'],
    'purple': ['#8E44AD', '#9B59B6'],
    'blue': ['#2980B9', '#3498DB'],
    'green': ['#27AE60', '#2ECC71'],
    'cyan': ['#16A085', '#1ABC9C'],
    'yellow': ['#F39C12', '#F1C40F'],
    'orange': ['#D35400', '#E67E22'],
    'red': ['#C0392B', '#E74C3C'],
    'white': ['#BDC3C7', '#ECF0F1'],
    'grey': ['#2A9D8F', '#56c3b7']
}



# ------------------------------------------------------
# -------------------- Key Bindings --------------------
# ------------------------------------------------------

keys = [
    # Switch between windows (Move Focus)
    Key(
        "M-h",
        lazy.layout.left(),
        lazy.layout.down().when(layout='max'),
        desc="Move focus to left"
    ),
    Key(
        "M-<Left>",
        lazy.layout.left(),
        lazy.layout.down().when(layout='max'),
        desc="Move focus to left"
    ),
    Key(
        "M-l",
        lazy.layout.right(),
        lazy.layout.up().when(layout='max'),
        desc="Move focus to right"
    ),
    Key(
        "M-<Right>",
        lazy.layout.right(),
        lazy.layout.up().when(layout='max'),
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
        lazy.spawn("dmenu_run -h 40 -c -l 10 -p 'Apps:'"),
        desc="Launch Dmenu"
    ),
    Key(
        "M-S-s",
        lazy.spawn(shutdown_menu),
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

    Key(
        "M-b",
        lazy.hide_show_bar(),
        desc="Toogle bar visibility"
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
    Group("1", label=""), #matches=[Match(wm_class=["Code"])]),
    Group("2", label=""), #matches=[Match(wm_class=["firefox"])]),
    Group("3", label=""), #matches=[Match(wm_class=["discord"])]),
    Group("4", label=""), #matches=[Match(wm_class=["org.gnome.Nautilus"])]),
    Group("5", label=""), #matches=[Match(wm_class=["spotify"])]),
    Group("6", label=""),
    Group("7", label=""),
    Group("8", label=""),
    Group("9", label=""),
    Group("10", label="")
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

            # mod4 + shift + index of group = move focused window to group
            Key(
                "M-S-" + str(ind),
                lazy.window.togroup(groups[i].name),
                desc="move focused window to group {}".format(groups[i].name)
            ),

            # mod1 + alt + shift + index of group = go and move focused window to group
            Key(
                "M-S-A-" + str(ind), 
                lazy.window.togroup(groups[i].name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(groups[i].name),
            ),
        ]
    )



# ------------------------------------------------------
# ---------------------- Layouts -----------------------
# ------------------------------------------------------

layouts = [
    layout.Columns(
        border_focus=colors['grey'][1], # Border colour(s) for the focused window.
        border_focus_stack=colors['grey'][1], # Border colour(s) for the focused window in stacked columns.
        border_normal=colors['black'][1], # Border colour(s) for un-focused windows.
        border_normal_stack=colors['black'][1], # Border colour(s) for un-focused windows in stacked columns.
        border_on_single=True,          # Draw a border when there is one only window.
        border_width=2,                 # Border width.
        fair=False,                     # Add new windows to the column with least windows.
        grow_amount=10,                 # Amount by which to grow a window/column.
        insert_position=0,              # Position relative to the current window where new ones are inserted (0 means right above the current window, 1 means right after).
        margin=[6,6,6,6],               # Margin of the layout (int or list of ints [N E S W]).
        margin_on_single=[6,6,6,6],     # Margin when only one window. (int or list of ints [N E S W]).
        num_columns=2,                  # Preferred number of columns.
        split=True,                     # New columns presentation mode.
        wrap_focus_columns=False,       # Wrap the screen when moving focus across columns.
        wrap_focus_rows=False,          # Wrap the screen when moving focus across rows.
        wrap_focus_stacks=False         # Wrap the screen when moving focus across stacked.
    ),

    layout.Max(),

    # layout.Tile(
    #     add_after_last=False,           # Add new clients after all the others. If this is True, it overrides add_on_top.
    #     add_on_top=True,                # Add new clients before all the others, potentially pushing other windows into slave stack.
    #     border_focus='#0000ff',         # Border colour(s) for the focused window.
    #     border_normal='#000000',        # Border colour(s) for the unfocused window.
    #     border_on_single=True,          # Whether to draw border if there is only one window.
    #     border_width=1,                 # Border width.
    #     expand=True,                    # Expand the master windows to the full screen width if no slaves are present.
    #     margin=[5,5,5,5],               # Margin of the layout (int or list of ints [N E S W])
    #     margin_on_single=True,          # Whether to draw margin if there is only one window.
    #     master_length=1,                # Amount of windows displayed in the master stack. Surplus windows will be moved to the slave stack.
    #     master_match=None,              # A Match object defining which window(s) should be kept masters (single or a list of Match-objects).
    #     max_ratio=0.85,                 # Maximum width of master windows.
    #     mn_ratio=0.15,                  # Minimum width of master windows.
    #     ratio=0.5,                      # Width-percentage of screen size reserved for master windows.
    #     ratio_increment=0.01,           # By which amount to change ratio when cmd_decrease_ratio or cmd_increase_ratio are called.
    #     shift_windows=True              # Allow to shift windows within the layout. If False, the layout will be rotated instead.
    # ),

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
    #     new_client_position='after_current', # Place new windows: after_current - after the active window. before_current - before the active window, top - at the top of the stack, bottom - at the bottom of the stack.
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
# ---------------------- Top Bar -----------------------
# ------------------------------------------------------

widget_list = [

    # widget.TextBox(
    #     text=" ",                       # Text to be displayed.
    #     # width=None,                   # Width of the textbox.
    #     background=None,                # Widget background color.
    #     fmt='{}',                       # How to format the text.
    #     font='sans',                    # Text font.
    #     fontshadow=None,                # Font shadow color, default is None(no shadow).
    #     fontsize=None,                  # Font pixel size. Calculated if None.
    #     foreground='#ffffff',           # Foreground colour.
    #     markup=True,                    # Whether or not to use pango markup.
    #     max_chars=0,                    # Maximum number of characters to display in widget.
    #     mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    #     padding=None,                   # Padding left and right. Calculated if None.
    # ),

    # widget.TextBox(
    #     text="",                       # Text to be displayed.
    #     # width=None,                     # Width of the textbox.
    #     background=None,                # Widget background color.
    #     fmt='{}',                       # How to format the text.
    #     font='meslolgs',                # Text font.
    #     fontshadow=None,                # Font shadow color, default is None(no shadow).
    #     fontsize=24,                    # Font pixel size. Calculated if None.
    #     foreground=colors['cyan'][1],   # Foreground colour.
    #     markup=True,                    # Whether or not to use pango markup.
    #     max_chars=0,                    # Maximum number of characters to display in widget.
    #     mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    #     padding=0,                      # Padding left and right. Calculated if None.
    # ),

    widget.Spacer(
        length=5,                       # Length of the spacer
        background=colors['black'][1],  # Widget background color
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    ),

    widget.Image(
        background=colors['black'][1],  # Widget background color
        filename=arch_icon_path,        # Image filename. Can contain '~'
        margin=3,                       # Margin inside the box
        margin_x=0,                     # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1": lazy.spawn('firefox --new-window "https://wiki.archlinux.org/" '),
            "Button3": lazy.spawn('firefox --new-window "https://cp-algorithms.web.app/"'),
        },
        rotate=0.0,                     # rotate the image in degrees counter-clockwise
        scale=True,                     # Enable/Disable image scaling
    ),


    widget.TextBox(
        text="",                       # Text to be displayed.
        # width=None,                     # Width of the textbox.
        background=colors['grey'][1],   # Widget background color.
        fmt='{}',                       # How to format the text.
        font='meslolgs',                # Text font.
        fontshadow=None,                # Font shadow color, default is None(no shadow).
        fontsize=24,                    # Font pixel size. Calculated if None.
        foreground=colors['black'][1],  # Foreground colour.
        markup=True,                    # Whether or not to use pango markup.
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=0,                      # Padding left and right. Calculated if None.
    ),

    widget.CurrentLayoutIcon(
        background=colors["grey"][1],   # Widget background color
        custom_icon_paths=[layout_icon_dir], # List of folders where to search icons beforeusing built-in icons or icons in ~/.icons dir. This can also be used to providemissing icons for custom layouts. Defaults to empty list.
        fmt='{}',                       # How to format the text
        font='JetBrainsMono Nerd Font', # Default font
        fontshadow=None,                # font shadow color, default is None(no shadow)
        fontsize=14,                    # Font size. Calculated if None.
        foreground='#000000',           # Foreground colour
        markup=True,                    # Whether or not to use pango markup
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=8,                      # Padding. Calculated if None.
        scale=0.75,                     # Scale factor relative to the bar height. Defaults to 1
    ),

    # widget.CurrentLayout(
    #     background=colors["grey"][1],   # Widget background color
    #     fmt='{}',                       # How to format the text
    #     font='JetBransMono Nerd Font',  # Default font
    #     fontshadow=None,                # font shadow color, default is None(no shadow)
    #     fontsize=16,                    # Font size. Calculated if None.
    #     foreground='#000000',           # Foreground colour
    #     markup=True,                    # Whether or not to use pango markup
    #     max_chars=0,                    # Maximum number of characters to display in widget.
    #     mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    #     padding=3,                      # Padding. Calculated if None.
    # ),

    # widget.WindowCount(
    #     background=colors["grey"][1],   # Widget background color
    #     fmt='{}',                       # How to format the text
    #     font='JetBrainsMono Nerd Font', # Text font
    #     fontshadow=None,                # font shadow color, default is None(no shadow)
    #     fontsize=16,                    # Font pixel size. Calculated if None.
    #     foreground='#000000',           # Foreground colour.
    #     markup=True,                    # Whether or not to use pango markup
    #     max_chars=0,                    # Maximum number of characters to display in widget.
    #     mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    #     padding=None,                   # Padding left and right. Calculated if None.
    #     show_zero=True,                 # Show window count when no windows
    #     text_format='{num}',            # Format for message
    # ),

    widget.TextBox(
        text="",                       # Text to be displayed.
        # width=None,                     # Width of the textbox.
        background=colors['black'][1],  # Widget background color.
        fmt='{}',                       # How to format the text.
        font='meslolgs',                # Text font.
        fontshadow=None,                # Font shadow color, default is None(no shadow).
        fontsize=24,                    # Font pixel size. Calculated if None.
        foreground=colors['grey'][1],   # Foreground colour.
        markup=True,                    # Whether or not to use pango markup.
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=0,                      # Padding left and right. Calculated if None.
    ),

    widget.GroupBox(
        active='ffffff',                # Active group font colour.
        background=colors["black"][1],  # Widget background color
        block_highlight_text_color=None,# Selected group font colour.
        borderwidth=3,                  # Current group border width.
        center_aligned=True,            # center-aligned group box.
        disable_drag=True,              # Disable dragging and dropping of group names on widget.
        fmt='{}',                       # How to format the text.
        font='JetBrainsMono Nerd Font', # Text font.
        fontshadow=None,                # font shadow color, default is None(no shadow).
        fontsize=16,                    # Font size. Calculated if None.
        foreground='#ffffff',           # Foreground color.
        hide_unused=True,               # Hide groups that have no windows and that are not displayed on any screen.
        highlight_color=[colors["black"][1], colors["black"][1]], # Active group highlight color when using 'line' highlight method.
        highlight_method="line",        # Method of highlighting ('border', 'block', 'text', or 'line') Uses *_border color settings.
        inactive='#ffffff',             # Inactive group font colour
        invert_mouse_wheel=False,       # Whether to invert mouse wheel group movement
        margin=3,                       # Margin inside the box
        margin_x=None,                  # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        markup=True,                    # Whether or not to use pango markup
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        other_current_screen_border='#ffffff', # Border or line colour for group on other screen when focused.
        other_screen_border='#ffffff',  # Border or line colour for group on other screen when unfocused.
        padding=3,                      # Padding. Calculated if None.
        padding_x=None,                 # X Padding. Overrides 'padding' if set.
        padding_y=None,                 # Y Padding. Overrides 'padding' if set.
        rounded=True,                   # To round or not to round box borders
        spacing=5,                      # Spacing between groups(if set to None, will be equal to margin_x)
        this_current_screen_border=colors["green"][1], # Border or line colour for group on this screen when focused.
        this_screen_border='#215578',   # Border or line colour for group on this screen when unfocused.
        urgent_alert_method='border',   # Method for alerting you of WM urgent hints (one of 'border', 'text', 'block', or 'line')
        urgent_border='#FF0000',        # Urgent border or line color
        urgent_text='#FF0000',          # Urgent group font color
        use_mouse_wheel=True,           # Whether to use mouse wheel events
        visible_groups=None,            # Groups that will be visible. If set to None or [], all groups will be visible.Visible groups are identified by name not by their displayed label.
    ),

    widget.TextBox(
        text="",                       # Text to be displayed.
        # width=None,                     # Width of the textbox.
        # background=colors["grey"][1],   # Widget background color.
        background=None,                # Widget background color.
        fmt='{}',                       # How to format the text.
        font='meslolgs',                # Text font.
        fontshadow=None,                # Font shadow color, default is None(no shadow).
        fontsize=24,                    # Font pixel size. Calculated if None.
        foreground=colors['black'][1],  # Foreground colour.
        markup=True,                    # Whether or not to use pango markup.
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=0,                      # Padding left and right. Calculated if None.
    ),

    widget.WindowName(
        # background=colors["grey"][0],   # Widget background color
        background=None,                # Widget background color
        empty_group_string=' ',         # string to display when no windows are focused on current group
        fmt='{}',                       # How to format the text
        font='JetBrainsMono Nerd Font', # Text font.
        fontshadow=None,                # font shadow color, default is None(no shadow)
        fontsize=16,                    # Font size. Calculated if None.
        for_current_screen=False,       # instead of this bars screen use currently active screen
        foreground='#ffffff',           # Foreground colour
        format='{state}{name}',         # format of the text
        markup=True,                    # Whether or not to use pango markup
        max_chars=40,                   # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=20,                     # Padding. Calculated if None.
        parse_text=None,                # Function to parse and modify window names. e.g. function in config that removes excess strings from window name: def my_func(text) for string in [" - Chromium", " - Firefox"]: text = text.replace(string, "") return textthen set option parse_text=my_func
    ),
    
    widget.TextBox(
        text="",                       # Text to be displayed.
        # width=None,                     # Width of the textbox.
        # background=colors["grey"][1],   # Widget background color.
        background=None,                # Widget background color.
        fmt='{}',                       # How to format the text.
        font='meslolgs',                # Text font.
        fontshadow=None,                # Font shadow color, default is None(no shadow).
        fontsize=24,                    # Font pixel size. Calculated if None.
        foreground=colors['black'][1],  # Foreground colour.
        markup=True,                    # Whether or not to use pango markup.
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=0,                      # Padding left and right. Calculated if None.
    ),

    widget.Spacer(
        length=5,                       # Length of the spacer
        background=colors['black'][1],  # Widget background color
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    ),

    widget.Image(
        background=colors['black'][1],  # Widget background color
        filename=brightness_icon_path,  # Image filename. Can contain '~'
        margin=3,                       # Margin inside the box
        margin_x=None,                  # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        rotate=0.0,                     # rotate the image in degrees counter-clockwise
        scale=True,                     # Enable/Disable image scaling
    ),

    widget.Backlight(
        background=colors['black'][1],  # Widget background color
        backlight_name='intel_backlight', # ACPI name of a backlight device
        brightness_file='brightness',   # Name of file with the current brightness in /sys/class/backlight/backlight_name
        change_command='xbacklight -set {0}', # Execute command to change value
        fmt='{}  ',                     # How to format the text
        font='JetBrainsMono Nerd Font', # Default font
        fontshadow=None,                # font shadow color, default is None(no shadow)
        fontsize=16,                    # Font size. Calculated if None.
        foreground='#ffffff',           # Foreground colour
        format='{percent:2.0%}',        # Display format
        markup=True,                    # Whether or not to use pango markup
        max_brightness_file='max_brightness', # Name of file with the maximum brightness in /sys/class/backlight/backlight_name
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=3,                      # Padding. Calculated if None.
        step=10,                        # Percent of backlight every scroll changed
        update_interval=0.1,            # The delay in seconds between updates
    ),

    widget.Image(
        background=colors['black'][1],  # Widget background color
        filename=volume_icon_path,      # Image filename. Can contain '~'
        margin=3,                       # Margin inside the box
        margin_x=None,                  # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1":lazy.spawn('amixer -qD pulse set Master 1+ toggle'),
            "Button3":lazy.spawn('amixer -qD pulse set Master 1+ toggle'),
        },
        rotate=0.0,                     # rotate the image in degrees counter-clockwise
        scale=True,                     # Enable/Disable image scaling
    ),

    widget.Volume(
        background=colors["black"][1],  # Widget background color
        cardid=None,                    # Card Id
        channel='Master',               # Channel
        device='default',               # Device Name
        emoji=False,                    # Use emoji to display volume states, only if theme_path is not set.The specified font needs to contain the correct unicode characters.
        fmt='{} ',                      # How to format the text
        font='JetBrainsMono Nerd Font', # Default font
        fontshadow=None,                # font shadow color, default is None(no shadow)
        fontsize=16,                    # Font size. Calculated if None.
        foreground='#ffffff',           # Foreground colour
        get_volume_command=None,        # Command to get the current volume
        markup=True,                    # Whether or not to use pango markup
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1":lazy.spawn('amixer -qD pulse set Master 1+ toggle'),
            "Button3":lazy.spawn('amixer -qD pulse set Master 1+ toggle'),
        },
        mute_command=None,              # Mute command
        padding=3,                      # Padding left and right. Calculated if None.
        step=1,                         # Volume change for up an down commands in percentage.Only used if volume_up_command and volume_down_command are not set.
        theme_path=None,                # Path of the icons
        update_interval=0.1,            # Update time in seconds.
        volume_app=None,                # App to control volume
        volume_down_command=None,       # Volume down command
        volume_up_command=None,         # Volume up command
    ),

    widget.Image(
        background=colors['black'][1],  # Widget background color
        filename=bluetooth_icon_path,   # Image filename. Can contain '~'
        margin=3,                       # Margin inside the box
        margin_x=None,                  # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1": lazy.spawn("blueberry"),
            "Button2": lazy.spawn("blueberry"),
        },
        rotate=0.0,                     # rotate the image in degrees counter-clockwise
        scale=True,                     # Enable/Disable image scaling
    ),

    widget.Bluetooth(
        background=colors['black'][1],  # Widget background color
        fmt='{} ',                      # How to format the text
        font='cascadia code',           # Default font
        fontshadow=None,                # font shadow color, default is None(no shadow)
        fontsize=16,                    # Font size. Calculated if None.
        foreground='ffffff',            # Foreground colour
        hci='/dev_2C_BE_EB_02_C2_9A',   # hci0 device path, can be found with d-feet or similar dbus explorer.
        markup=True,                    # Whether or not to use pango markup
        max_chars=5,                    # Maximum number of characters to display in widget.
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1": lazy.spawn("blueberry"),
            "Button2": lazy.spawn("blueberry"),
        },
        padding=3,                      # Padding. Calculated if None.
    ),

    widget.TextBox(
        text="",                       # Text to be displayed.
        # width=None,                     # Width of the textbox.
        background=colors['black'][1],  # Widget background color.
        fmt='{}',                       # How to format the text.
        font='meslolgs',                # Text font.
        fontshadow=None,                # Font shadow color, default is None(no shadow).
        fontsize=24,                    # Font pixel size. Calculated if None.
        foreground=colors['grey'][1],   # Foreground colour.
        markup=True,                    # Whether or not to use pango markup.
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=0,                      # Padding left and right. Calculated if None.
    ),
    
    # extra_widget.ALSAWidget(
    #     background=colors['cyan'][1],   # Widget background color
    #     bar_colour_high='#999900',      # Colour of bar if high range
    #     bar_colour_loud='#990000',      # Colour of bar in loud range
    #     bar_colour_mute='#999999',	  # Colour of bar if muted
    #     bar_colour_normal='#009900',    # Colour of bar in normal range
    #     bar_width=75,                   # Width of display bar
    #     decorations=[],                 # Decorations for widgets
    #     device='Master',                # Name of ALSA device
    #     font='JetBrainsMono Nerd Font', # Text font.
    #     fontsize=18,                 	  # Font size
    #     foreground='#ffffff',           # Font colour
    #     hide_interval=5, 	              # Timeout before bar is hidden after update
    #     limit_high=90,                  # Max percentage for high range
    #     limit_loud=100, 	              # Max percentage for loud range
    #     limit_normal=70, 	              # Max percentage for normal range
    #     margin=3,                       # Margin inside the box
    #     margin_x=3,                     # X Margin. Overrides 'margin' if set
    #     margin_y=3,                     # Y Margin. Overrides 'margin' if set
    #     mode='both',                    # Display mode: 'icon', 'bar', 'both'.
    #     mouse_callbacks={}, 	          # Dict of mouse button press callback functions. Accepts functions and ``lazy`` calls.
    #     padding=3,                      # Padding inside the box
    #     padding_x=3,                    # X Padding. Overrides 'padding' if set
    #     padding_y=3,                    # Y Padding. Overrides 'padding' if set
    #     step=5,                         # Amount to increase volume by
    #     text_format='{volume}%',        # String format
    #     theme_path="/usr/share/icons/Paper/24x24/panel", # Path to theme icons.
    #     update_interval=0.1,            # Interval to update widget (e.g. if changes made in other apps).
    # ),

    widget.Spacer(
        length=5,                       # Length of the spacer
        background=colors['grey'][1],   # Widget background color
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    ),

    widget.Image(
        background=colors['grey'][1],   # Widget background color
        filename=cpu_icon_path,         # Image filename. Can contain '~'
        margin=3,                       # Margin inside the box
        margin_x=None,                  # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1": lazy.spawn("terminator -e 'bpytop'"),
            "Button3": lazy.spawn("terminator -e 'bpytop'"),
        },
        rotate=0.0,                     # rotate the image in degrees counter-clockwise
        scale=True,                     # Enable/Disable image scaling
    ),

    widget.CPU(
        background=colors['grey'][1],   # Widget background color
        fmt='{}  ',                     # How to format the text
        font='cascadia code',           # Default font
        fontshadow=None,                # font shadow color, default is None(no shadow)
        fontsize=16,                    # Font size. Calculated if None.
        foreground='#000000',           # Foreground colour
        format='{load_percent}%',       # CPU display format
        markup=True,                    # Whether or not to use pango markup
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1": lazy.spawn("terminator -e 'bpytop'"),
            "Button3": lazy.spawn("terminator -e 'bpytop'"),
        },
        padding=3,                      # Padding. Calculated if None.
        update_interval=1,              # Update interval for the CPU widget
    ),

    widget.Image(
        background=colors['grey'][1],   # Widget background color
        filename=memory_icon_path,      # Image filename. Can contain '~'
        margin=3,                       # Margin inside the box
        margin_x=0,                     # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1": lazy.spawn("terminator -e 'bpytop'"),
            "Button3": lazy.spawn("terminator -e 'bpytop'"),
        },
        rotate=0.0,                     # rotate the image in degrees counter-clockwise
        scale=True,                     # Enable/Disable image scaling
    ),

    widget.Memory(
        background=colors['grey'][1],   # Widget background color
        fmt='{}',                       # How to format the text
        font='cascadia code',           # Default font
        fontshadow=None,                # font shadow color, default is None(no shadow)
        fontsize=16,                    # Font size. Calculated if None.
        foreground='#000000',           # Foreground colour
        format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}', # Formatting for field names.
        markup=True,                    # Whether or not to use pango markup
        max_chars=0,                    # Maximum number of characters to display in widget.
        measure_mem='M',                # Measurement for Memory (G, M, K, B)
        measure_swap='M',               # Measurement for Swap (G, M, K, B)
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1": lazy.spawn("terminator -e 'bpytop'"),
            "Button3": lazy.spawn("terminator -e 'bpytop'"),
        },
        padding=None,                   # Padding. Calculated if None.
        update_interval=1.0,            # Update interval for the Memory
    ),

    # widget.CapsNumLockIndicator(
    #     background=colors["grey"][1],   # Widget background color
    #     fmt=' {}',                     # How to format the text
    #     font='JetBrainsMono Nerd Font', # Default font
    #     fontshadow=None,                # font shadow color, default is None(no shadow)
    #     fontsize=16,                    # Font size. Calculated if None.
    #     foreground='#000000',           # Foreground colour
    #     markup=True,                    # Whether or not to use pango markup
    #     max_chars=0,                    # Maximum number of characters to display in widget.
    #     mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    #     padding=None,                   # Padding. Calculated if None.
    #     update_interval=0.1,            # Update Time in seconds.
    # ),

    # widget.TextBox(
    #     text="",                       # Text to be displayed.
    #     # width=None,                     # Width of the textbox.
    #     background=colors['cyan'][1],   # Widget background color.
    #     fmt='{}',                       # How to format the text.
    #     font='meslolgs',                # Text font.
    #     fontshadow=None,                # Font shadow color, default is None(no shadow).
    #     fontsize=24,                    # Font pixel size. Calculated if None.
    #     foreground=colors['green'][1],  # Foreground colour.
    #     markup=True,                    # Whether or not to use pango markup.
    #     max_chars=0,                    # Maximum number of characters to display in widget.
    #     mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    #     padding=0,                      # Padding left and right. Calculated if None.
    # ),

    # widget.Systray(
    #     background=colors['green'][1],  # Widget background color
    #     icon_size=20,                   # Icon width
    #     mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    #     padding=5,                      # Padding between icons
    # ),

    widget.TextBox(
        text="",                       # Text to be displayed.
        # width=None,                     # Width of the textbox.
        background=colors['grey'][1],   # Widget background color.
        fmt='{}',                       # How to format the text.
        font='meslolgs',                # Text font.
        fontshadow=None,                # Font shadow color, default is None(no shadow).
        fontsize=24,                    # Font pixel size. Calculated if None.
        foreground=colors['black'][1],  # Foreground colour.
        markup=True,                    # Whether or not to use pango markup.
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=0,                      # Padding left and right. Calculated if None.
    ),

    widget.Spacer(
        length=5,                       # Length of the spacer
        background=colors['black'][1],  # Widget background color
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    ),

    widget.Image(
        background=colors['black'][1],  # Widget background color
        filename=network_icon_path,     # Image filename. Can contain '~'
        margin=3,                       # Margin inside the box
        margin_x=None,                  # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1": lazy.spawn(wifi_prompt),
        },
        rotate=0.0,                     # rotate the image in degrees counter-clockwise
        scale=True,                     # Enable/Disable image scaling
    ),

    widget.Net(
        background=colors['black'][1],  # Widget background color
        fmt='{}',                       # How to format the text
        font='cascadia code',           # Default font
        fontshadow=None,                # font shadow color, default is None(no shadow)
        fontsize=16,                    # Font size. Calculated if None.
        foreground='ffffff',            # Foreground colour
        format='{down}/s ↓ {up}/s ↑',   # Display format of down/upload/total speed of given interfaces
        interface="wlp3s0",             # List of interfaces or single NIC as string to monitor, None to display all active NICs combined
        markup=False,                   # Whether or not to use pango markup
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1": lazy.spawn(wifi_prompt),
        },
        padding=None,                   # Padding. Calculated if None.
        prefix=None,                    # Use a specific prefix for the unit of the speed.
        update_interval=1,              # The update interval.
        use_bits=False,                 # Use bits instead of bytes per second?
    ),

    widget.TextBox(
        text="",                       # Text to be displayed.
        # width=None,                     # Width of the textbox.
        background=colors['black'][1],  # Widget background color.
        fmt='{}',                       # How to format the text.
        font='meslolgs',                # Text font.
        fontshadow=None,                # Font shadow color, default is None(no shadow).
        fontsize=24,                    # Font pixel size. Calculated if None.
        foreground=colors['grey'][1],   # Foreground colour.
        markup=True,                    # Whether or not to use pango markup.
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=0,                      # Padding left and right. Calculated if None.
    ),

    widget.Spacer(
        length=5,                       # Length of the spacer
        background=colors['grey'][1],   # Widget background color
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    ),

    widget.BatteryIcon(
        background=colors['grey'][1],   # Widget background color
        battery=1,                      # Which battery should be monitored
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        scale=1,                        # Scale factor relative to the bar height. Defaults to 1
        theme_path=battery_icon_dir,    # Path of the icons
        update_interval=1,              # Seconds between status updates
    ),

    widget.Battery(
        background=colors['grey'][1],   # Widget background color
        battery=1,                      # Which battery should be monitored (battery number or name)
        charge_char='^',                # Character to indicate the battery is charging
        discharge_char='V',             # Character to indicate the battery is discharging
        empty_char='x',                 # Character to indicate the battery is empty
        fmt='{} ',                      # How to format the text
        font='JetBrainsMono Nerd Font', # Default font
        fontshadow=None,                # font shadow color, default is None(no shadow)
        fontsize=16,                    # Font size. Calculated if None.
        foreground='000000',            # Foreground colour
        format='{percent:2.0%} {hour:d}:{min:02d}', # Display format
        full_char='=',                  # Character to indicate the battery is full
        hide_threshold=None,            # Hide the text when there is enough energy 0 <= x < 1
        low_background=None,            # Background color on low battery
        low_foreground='FF0000',        # Font color on low battery
        low_percentage=0.1,             # Indicates when to use the low_foreground color 0 < x < 1
        markup=True,                    # Whether or not to use pango markup
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        notification_timeout=10,        # Time in seconds to display notification. 0 for no expiry.
        notify_below=None,              # Send a notification below this battery level.
        padding=None,                   # Padding. Calculated if None.
        show_short_text=True,           # Show "Full" or "Empty" rather than formated text
        unknown_char='?',               # Character to indicate the battery status is unknown
        update_interval=1,              # Seconds between status updates
    ),

    widget.Image(
        background=colors['grey'][1],   # Widget background color
        filename=temperature_icon_path, # Image filename. Can contain '~'
        margin=3,                       # Margin inside the box
        margin_x=0,                     # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        rotate=0.0,                     # rotate the image in degrees counter-clockwise
        scale=True,                     # Enable/Disable image scaling
    ),
    
    widget.ThermalSensor(
        background=colors['grey'][1],   # Widget background color
        fmt='{}',                       # How to format the text
        font='cascadia code',           # Default font
        fontshadow=None,                # font shadow color, default is None(no shadow)
        fontsize=16,                    # Font size. Calculated if None.
        foreground='#000000',           # Foreground colour
        foreground_alert='#ff0000',     # Foreground colour alert
        markup=True,                    # Whether or not to use pango markup
        max_chars=0,                    # Maximum number of characters to display in widget.
        metric=True,                    # True to use metric/C, False to use imperial/F
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=None,                   # Padding. Calculated if None.
        show_tag=False,                 # Show tag sensor
        tag_sensor=None,                # Tag of the temperature sensor. For example: "temp1" or "Core 0"
        threshold=70,                   # If the current temperature value is above, then change to foreground_alert colour
        update_interval=1,              # Update interval in seconds
    ),

    widget.TextBox(
        text="",                       # Text to be displayed.
        # width=None,                     # Width of the textbox.
        background=colors['grey'][1],   # Widget background color.
        fmt='{}',                       # How to format the text.
        font='meslolgs',                # Text font.
        fontshadow=None,                # Font shadow color, default is None(no shadow).
        fontsize=24,                    # Font pixel size. Calculated if None.
        foreground=colors['black'][1],  # Foreground colour.
        markup=True,                    # Whether or not to use pango markup.
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=0,                      # Padding left and right. Calculated if None.
    ),

    widget.Spacer(
        length=5,                       # Length of the spacer
        background=colors['black'][1],  # Widget background color
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    ),

    widget.Image(
        background=colors['black'][1],  # Widget background color
        filename=clock_icon_path,       # Image filename. Can contain '~'
        margin=3,                       # Margin inside the box
        margin_x=None,                  # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        rotate=0.0,                     # rotate the image in degrees counter-clockwise
        scale=True,                     # Enable/Disable image scaling
    ),

    widget.Clock(
        background=colors['black'][1],  # Widget background color
        fmt='{}',                       # How to format the text
        font='JetBrainsMono Nerd Font', # Text font.
        fontshadow=None,                # font shadow color, default is None(no shadow)
        fontsize=16,                    # Font size. Calculated if None.
        foreground='#ffffff',           # Foreground colour
        format="%Y-%m-%d %a %I:%M %p",# A Python datetime format string
        markup=True,                    # Whether or not to use pango markup
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=None,                   # Padding. Calculated if None.
        timezone=None,                  # The timezone to use for this clock, either as string if pytz or dateutil is installed (e.g. "US/Central" or anything in /usr/share/zoneinfo), or as tzinfo (e.g. datetime.timezone.utc). None means the system local timezone and is the default.
        update_interval=1.0,            # Update interval for the clock
    ),

    widget.TextBox(
        text="",                       # Text to be displayed.
        # width=None,                     # Width of the textbox.
        background=colors['black'][1],  # Widget background color.
        fmt='{}',                       # How to format the text.
        font='meslolgs',                # Text font.
        fontshadow=None,                # Font shadow color, default is None(no shadow).
        fontsize=24,                    # Font pixel size. Calculated if None.
        foreground=colors['grey'][1],   # Foreground colour.
        markup=True,                    # Whether or not to use pango markup.
        max_chars=0,                    # Maximum number of characters to display in widget.
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
        padding=0,                      # Padding left and right. Calculated if None.
    ),

    # widget.QuickExit(
    #     # widget=None,                    # Widget width
    #     background=colors['grey'][1],   # Widget background color
    #     countdown_format='{}',          # This text is showed when counting down.
    #     countdown_start=10,             # Time to accept the second pushing.
    #     default_text='',               # A text displayed as a button
    #     fmt='{}',                       # How to format the text
    #     font='JetBrainsMono Nerd Font', # Text font.
    #     fontshadow=None,                # font shadow color, default is None(no shadow)
    #     fontsize=16,                    # Font size. Calculated if None.
    #     foreground='#000000',           # Foreground colour
    #     markup=True,                    # Whether or not to use pango markup
    #     max_chars=0,                    # Maximum number of characters to display in widget.
    #     mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    #     padding=None,                   # Padding. Calculated if None.
    #     timer_interval=1,               # A countdown interval.
    # ),

    widget.Image(
        background=colors['grey'][1],   # Widget background color
        filename=logout_icon_path,      # Image filename. Can contain '~'
        margin=4,                       # Margin inside the box
        margin_x=None,                  # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1": lazy.spawn(logout_prompt),
            "Button3": lazy.spawn("i3lock-fancy"),
        },
        rotate=0.0,                     # rotate the image in degrees counter-clockwise
        scale=True,                     # Enable/Disable image scaling
    ),

    widget.Spacer(
        length=3,                       # Length of the spacer
        background=colors['grey'][1],   # Widget background color
        mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    ),

    widget.Image(
        background=colors['grey'][1],   # Widget background color
        filename=poweroff_icon_path,    # Image filename. Can contain '~'
        margin=4,                       # Margin inside the box
        margin_x=None,                  # X Margin. Overrides 'margin' if set
        margin_y=None,                  # Y Margin. Overrides 'margin' if set
        mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
            "Button1": lazy.spawn(poweroff_prompt),
            "Button3": lazy.spawn(suspend_prompt),
        },             
        rotate=0.0,                     # rotate the image in degrees counter-clockwise
        scale=True,                     # Enable/Disable image scaling
    ),

    widget.Spacer(
       length=5,                       # Length of the spacer
       background=colors['grey'][1],   # Widget background color
       mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    ),

    # widget.TextBox(
    #     text="",                       # Text to be displayed.
    #     # width=None,                     # Width of the textbox.
    #     background=None,                # Widget background color.
    #     fmt='{}',                       # How to format the text.
    #     font='meslolgs',                # Text font.
    #     fontshadow=None,                # Font shadow color, default is None(no shadow).
    #     fontsize=24,                    # Font pixel size. Calculated if None.
    #     foreground=colors['purple'][1], # Foreground colour.
    #     markup=True,                    # Whether or not to use pango markup.
    #     max_chars=0,                    # Maximum number of characters to display in widget.
    #     mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    #     padding=0,                      # Padding left and right. Calculated if None.
    # ),

    # widget.TextBox(
    #     text="  ",                       # Text to be displayed.
    #     # width=None,                     # Width of the textbox.
    #     background=None,                # Widget background color.
    #     fmt='{}',                       # How to format the text.
    #     font='meslolgs',                # Text font.
    #     fontshadow=None,                # Font shadow color, default is None(no shadow).
    #     fontsize=24,                    # Font pixel size. Calculated if None.
    #     foreground=None,                # Foreground colour.
    #     markup=True,                    # Whether or not to use pango markup.
    #     max_chars=0,                    # Maximum number of characters to display in widget.
    #     mouse_callbacks={},             # Dict of mouse button press callback functions. Acceps functions and lazy calls.
    #     padding=0,                      # Padding left and right. Calculated if None.
    # ),
]

screeen_list = [
    Screen(top=bar.Bar(
        widgets=widget_list,            # A list of widget objects.
        size=24,                        # The "thickness" of the bar, i.e. the height of a horizontal bar, or the width of a vertical bar.
        background='#00000000',         # Background colour.
        border_color='#000000',         # Border colour as str or list of str [N E S W].
        border_width=0,                 # Width of border as int of list of ints [N E S W].
        margin=0,                       # Space around bar as int or list of ints [N E S W].
        padding=0,
        opacity=1,                      # Bar window opacity.
    ),),
]

screens = screeen_list



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
# ----------------------- Hooks ------------------------
# ------------------------------------------------------

@hook.subscribe.startup_once
def start_once():
    subprocess.call(autostart)



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

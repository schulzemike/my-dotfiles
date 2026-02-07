# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from enum import Enum
from libqtile import bar, layout, hook, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget.textbox import TextBox

# qtile-extras
# from qtile_extras import widget



terminal = guess_terminal()
mod = "mod4"


keys = [

   # A list of available commands that can be bound to keys can be found
   # at https://docs.qtile.org/en/latest/manual/config/lazy.html
   # Switch between windows
   Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
   Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
   Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
   Key([mod], "up", lazy.layout.up(), desc="Move focus up"),


   # Move windows between left/right columns or move up/down in current stack.
   # Moving out of range in Columns layout will create new column.
   Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
   Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
   Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
   Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),


   # Grow windows. If current window is on the edge of screen and direction
   # will be to screen edge - window would shrink.
   Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
   Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
   Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
   Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
   Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),


   # Toggle between split and unsplit sides of stack.
   # Split = all windows displayed
   # Unsplit = 1 window displayed, like Max layout, but still with
   # multiple stack panes
   Key(
       [mod, "shift"],
       "Return",
       lazy.layout.toggle_split(),
       desc="Toggle between split and unsplit sides of stack",
   ),
   Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),


   # Toggle between different layouts as defined below
   Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),


   Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),


   Key(
       [mod],
       "f",
       lazy.window.toggle_fullscreen(),
       desc="Toggle fullscreen on the focused window",
   ),
   Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
   Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
   Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
   # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

   # #CHANGE WORKSPACES
   # Key(["alt", "shift" ], "Tab", lazy.screen.prev_group()),
   # Key(["alt"], "Tab", lazy.screen.next_group()),

   # CHANGE SCREENS
   Key([mod, "shift"], "Tab", lazy.prev_screen()),
   Key([mod], "Tab", lazy.next_screen()),

   # Restart qtile
   Key([mod, "shift"], "r", lazy.restart()),
]


# ------------------------------------------
# Set up the groups
# ------------------------------------------

# 
# group_names = ["1", "", "3", "4", "5", "6"]
group_names = ["1", "2", "3", "4", "5", "6"]

groups = [
    Group(name=group_names[0], layout = "columns"),
    Group(name=group_names[1], layout = "max", matches=[Match(wm_class="jetbrains-idea")]),
    Group(name=group_names[2], screen_affinity=1, layout = "max", matches=[Match(wm_class="google-chrome")]),
    Group(name=group_names[3], layout = "columns"),
    Group(name=group_names[4], layout = "columns"),
    Group(name=group_names[5], layout = "columns"),
    ScratchPad("scratchpad", [
        DropDown("term", "alacritty"),
        DropDown("keepassdd", "keepassxc", height=0.6)
    ]),
    #ScratchPad("keepass", [DropDown("keepassdd", "keepassxc", height=0.6)],"keepassxc"),
]


def group_keys():
    localkeys = []
    # Switch to the groups, we use fix mappings, because we also have 
    # at least one scratchpad
    keys_for_groups = ["1", "2", "3", "4", "5", "6", "7", "8", "9" ,"0"]
    
    for index, group in enumerate(groups):
        if index < len(keys_for_groups):
            keys.extend([
                Key([mod], keys_for_groups[index], lazy.group[group.name].toscreen(), desc="Switch to group {}".format(group.name)),
                Key([mod, "shift"], keys_for_groups[index], lazy.window.togroup(group.name, switch_group=False), desc="Move focused window to group {}".format(group.name)),
            ])
    
    
    localkeys.extend([Key([mod], "F9", lazy.group["scratchpad"].dropdown_toggle("term"))])
    localkeys.extend([Key([mod], "F1", lazy.group["scratchpad"].dropdown_toggle("keepassdd"))])
    return localkeys

keys.extend(group_keys())



# end of groups

# Config values
margin = 10

default_font = "Noto Sans"
font_size = 12



colors = {
    "bg" : ["#282828", "#282828"],
    "bg0" : ["#282828", "#282828"],
    "bg2": ["#504945", "#504945"],
    "bg0_h" : ["#1d2021", "#1d2021"],
    "bg1" : ["#3c3836", "#3c3836"],
    "fg" : ["#ebdbb2", "#ebdbb2"],
    "fg0": ["#fbf1c9", "#fbf1c9"],
    "gray": ["#a89984", "#a89984"],
    "gray8": ["#928374", "#928374"],
    "green":["#98971a", "#98971a"],
    "orange":["#d65d0e","#d65d0e"],
    "orange_light":["#fe8019","#fe8019"],
    "red":["#cc241d","#cc241d"],
    "red_9":["#fb4934","#fb4934"],
    "yellow":["#d79921","#d79921"],

}

layouts = [
    layout.Columns(
        border_focus=colors["orange"],
        border_focus_stack=colors["green"],
        border_normal_stack=colors["yellow"],
        border_on_single=True,
        border_width=2,
        margin=margin
    ),
    layout.Max(
        border_focus=colors["orange"],
        border_width=2,
        margin=margin),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_focus=colors["orange"],
        margin=margin,
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]




widget_defaults = dict(
    font=default_font,
    fontsize=font_size,
    padding=3,
)
extension_defaults = widget_defaults.copy()

Orientation = Enum("Orientation", ["TOP_LEFT", "TOP_RIGHT", "BOTTOM_LEFT", "BOTTOM_RIGHT"])

#      
def slope(orientation, fg_color, bg_color): 
#    icon = ""
    icon = "-"

    match orientation:
        case Orientation.TOP_LEFT:
            icon = ""
        case Orientation.TOP_RIGHT:
            icon = ""
        case Orientation.BOTTOM_LEFT:
            icon = ""
        case Orientation.BOTTOM_RIGHT:
            icon = ""

    return TextBox(icon,
       fontsize=22,
       # fmt="<span rise='6500'>{}</span>",
       padding=0,
       background = bg_color,
       foreground = fg_color,
    )


def init_widgets():
    widgets = [
        widget.GenPollCommand(
            background = colors["bg1"],
            cmd = "${XDG_CONFIG_HOME}/qtile/scripts/w_status_hostsystem.sh \#cc241d",
            padding = 11,
            shell = True,
            update_interval = 30,
        ),
        slope(Orientation.TOP_LEFT, colors["bg1"], colors["gray8"]),
        widget.Spacer(
            length = 24,
            background = colors["gray8"],
        ),
        slope(Orientation.TOP_LEFT, colors["gray8"], colors["bg1"]),
        widget.CurrentLayout(
            padding = 12,
            foreground = colors["fg"],
            background = colors["bg1"],
        ),
        slope(Orientation.TOP_LEFT, colors["bg1"], colors["bg"]),
        widget.Spacer(
            length = 8,
            background = colors["bg"],
        ),
        widget.GroupBox(
            background = colors["bg"],
            disable_drag = True,
            this_current_screen_border = colors["orange"],
            this_screen_border = colors["gray"],
        ),
        widget.Spacer(
            length = 8,
            background = colors["bg"],
        ),
        slope(Orientation.TOP_LEFT, colors["bg"], colors["bg1"]),
        # widget.Prompt(),
        widget.Spacer(
            background = colors["bg1"],
        ),
        widget.WindowName(
            foreground = colors["fg"],
            background = colors["bg1"],
        ),
        widget.Spacer(
            background = colors["bg1"],
        ),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.TextBox(
            "",
            fontsize=20,
            forground = colors["gray8"],
            background = colors["bg1"],
        ),
        # does not work in VM - i guess it just times out
        # widget.Wttr(
        #     lang='de',
        #     format="3",
        #     location="Wuensdorf",
        #     update_interval=6000,
        #     units="m",
        #     parse=lambda r: r.strip() or "Offline",
        # ),
        widget.GenPollCommand(
            cmd="curl -s 'wttr.in/Wuensdorf?format=1' || echo 'N/A'",
            shell=True,
            update_interval=1800,
            parse=lambda x: x.strip(),
            foreground = colors["fg"],
            background = colors["bg1"],
            padding = 1,
        ),
        widget.Spacer(
            length = 12,
            background = colors["bg1"],
        ),
        widget.Systray(
            background = colors["bg1"],
        ),
        widget.Spacer(
            length = 12,
            background = colors["bg1"],
        ),
        slope(Orientation.TOP_RIGHT, colors["bg2"], colors["bg1"]), 
        widget.Clock(format="%a. %d.%m. %H:%M:%S",
            foreground = colors["fg"],
            background = colors["bg2"],
        ),
        slope(Orientation.TOP_RIGHT, colors["gray8"], colors["bg2"]), 
        widget.QuickExit(
            default_text = "   [ logout ]    ",
            background = colors["gray8"],
            foreground = colors["bg1"],
        ),
    ]
    return widgets


def init_widgets_for_other_screens():
    widgets = init_widgets()
    # delete the systray
    # del widgets[7:9] if more widgets have to be deleted
    del widgets[len(widgets) - 6]
    return widgets


screens = [
    Screen(
        top=bar.Bar(
            init_widgets(),
            size=24,
            margin=[margin, margin, 0, margin],
            # for transparent bar
            # background=["#00000000"],
            # opacity=1,
            background=colors["bg0_h"],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
        #left=bar.Gap(margin),
        #right=bar.Gap(margin),
        #bottom=bar.Gap(margin),
        wallpaper="~/.local/share/wallpapers/beautiful-shot-snowy-mountain-sunset.jpg",
        # set the mode to "fill" or "stretch"
        wallpaper_mode="fill",
    ),
    Screen(
        top=bar.Bar(
            init_widgets_for_other_screens(),
            size=24,
            margin=[margin, margin, 0, margin],
            background=colors["bg0_h"],
        ),
        # wallpaper="~/.local/share/wallpapers/tall-trees-forest-mountains-covered-with-fog.jpg",
        wallpaper="~/.local/share/wallpapers/beautiful-shot-snowy-mountain-sunset.jpg",
        # set the mode to "fill" or "stretch"
        wallpaper_mode="fill",
    ),
    Screen(
        top=bar.Bar(
            init_widgets_for_other_screens(),
            size=24,
            margin=[margin, margin, 0, margin],
            background=colors["bg0_h"],
        ),
        wallpaper="~/.local/share/wallpapers/beautiful-shot-snowy-mountain-sunset.jpg",
        # set the mode to "fill" or "stretch"
        wallpaper_mode="fill",
    ),
]






# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]









@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

# @hook.subscribe.client_new
# def new_client(client):
#     assign_app_to_group(client)


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
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
        Match(wm_class="de-eurodata-commons-swing-AbstractSwingApplication"),
    ],
    border_focus=colors["gray"],
    
)


auto_fullscreen = True
focus_on_window_activation = "focus" # or smart
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
wmname = "qtile"






def left_triangle(fg_color, bg_color):
    return widget.TextBox(
        " ",
        fontsize=18,
        fmt="<span rise='6500'>{}</span>",
        padding=0,
        background = bg_color,
        foreground = fg_color,
        )

def right_triangle(fg_color, bg_color):
    return widget.TextBox(
        "",
        fontsize=18,
        fmt="<span rise='6500'>{}</span>",
        padding=0,
        background = bg_color,
        foreground = fg_color,
        )


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
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget.textbox import TextBox

# specific config files
from groups import groups
from groups import assign_app_to_group
from keys import key_binding


keys = key_binding()



# Config values
margin = 10



terminal = guess_terminal()
super = "mod4"

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
    font="Noto Sans",
    fontsize=12,
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
        # widget.TextBox(
        #    "",
        #    fontsize=22,
        #    # fmt="<span rise='6500'>{}</span>",
        #    padding=0,
        #    background = colors["bg2"],
        #    foreground = colors["gray8"],
        # ),
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
        wallpaper="/usr/share/backgrounds/arcolinux/landscape-3840x2160.jpg",
        # set the mode to "fill" or "stretch"
        wallpaper_mode="stretch",
    ),
    Screen(
        top=bar.Bar(
            init_widgets_for_other_screens(),
            size=24,
            margin=[margin, margin, 0, margin],
            background=colors["bg0_h"],
        ),
        wallpaper="/usr/share/backgrounds/arcolinux/landscape-3840x2160.jpg",
        # set the mode to "fill" or "stretch"
        wallpaper_mode="fill",
    ),
]






# Drag floating layouts.
mouse = [
    Drag([super], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([super], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([super], "Button2", lazy.window.bring_to_front()),
]









@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.client_new
def new_client(client):
    assign_app_to_group(client)


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
    ],
    border_focus=colors["gray"],
    
)


auto_fullscreen = True
focus_on_window_activation = "focus" # or smart
# reconfigure_screens = True

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


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
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# specific config files
from groups import groups
from groups import assign_app_to_group
from keys import key_binding


keys = key_binding()



# Config values
margin = 10


terminal = guess_terminal()
super = "mod4"



layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2, margin=[0, margin, margin, margin]),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(margin=margin),
    layout.MonadWide(),
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


def init_widgets():
    widgets = [
        widget.TextBox(
            text="",
            padding=6
        ),
        widget.CurrentLayout(),
        widget.GroupBox(),
        widget.Prompt(),
        widget.Spacer(),
        widget.WindowName(),
        widget.Spacer(),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Systray(),
        widget.Clock(format="%d. %m. %a %I:%M %p"),
        widget.QuickExit(),
    ]
    return widgets

def init_widgets_for_other_screens():
    widgets = init_widgets()
    # delete the systray
    # del widgets[7:9] if more widgets have to be deleted
    del widgets[len(widgets) - 3]
    return widgets


screens = [
    Screen(
        top=bar.Bar(
            init_widgets(),
            size=24,
            margin=[margin, margin, margin, margin],
            #background=["#1F1F28"],
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
            margin=[margin, margin, margin, margin],
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
wmname = "qtile"


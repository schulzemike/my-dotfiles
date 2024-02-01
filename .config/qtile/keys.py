from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


super = "mod4"
terminal = guess_terminal()


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([super], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([super], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([super], "down", lazy.layout.down(), desc="Move focus down"),
    Key([super], "up", lazy.layout.up(), desc="Move focus up"),
    Key([super], "space", lazy.layout.next(), desc="Move window focus to other window"),
    

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([super, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([super, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([super, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([super, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),


    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([super, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([super, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([super, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([super, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([super], "n", lazy.layout.normalize(), desc="Reset all window sizes"),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [super, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([super], "Return", lazy.spawn(terminal), desc="Launch terminal"),


    # Toggle between different layouts as defined below
    Key([super], "Tab", lazy.next_layout(), desc="Toggle between layouts"),


    Key([super], "q", lazy.window.kill(), desc="Kill focused window"),


    Key(
        [super],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([super], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([super, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([super, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([super], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Restart qtile
    Key([super, "shift"], "r", lazy.restart()),
]

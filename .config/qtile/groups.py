from libqtile.config import Group, ScratchPad, DropDown


groups = [
    Group("1", layout = "columns"),
    Group("2", layout = "monadtall"),
    Group("web", layout = "monadtall"),
    Group("ide", layout = "monadtall"),
    Group("teams", layout = "monadtall"),
    Group("6", layout = "monadtall"),
    ScratchPad("sc", [DropDown("term", "alacritty")]),
]

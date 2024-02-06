from libqtile.config import Group, ScratchPad, DropDown

group_names = ["1", "2", "web", "ide", "teams", "6"]

groups = [
    Group(group_names[0], layout = "columns"),
    Group(group_names[1], layout = "monadtall"),
    Group(group_names[2], layout = "monadtall"),
    Group(group_names[3], layout = "monadtall"),
    Group(group_names[4], layout = "monadtall"),
    Group(group_names[5], layout = "monadtall"),
    ScratchPad("sc", [DropDown("term", "alacritty")]),
]

def assign_app_to_group(client):
    d = {}

    d[group_names[2]] = ["google-chrome"]
    d[group_names[3]] = ["jetbrains-idea"]
    d[group_names[5]] = ["keepassxc"]

    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)

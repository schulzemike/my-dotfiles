import unittest
from inspect import cleandoc

from pyfakefs.fake_filesystem_unittest import TestCase

from extractKeybings import read_qtile_keymap


class TestMyReader(TestCase):

    CONFIG_PATH = "/mock/path/config.py"

    def setUp(self):
        # Aktiviert das Fake-Dateisystem automatisch für diese Testklasse
        self.setUpPyfakefs()


    def test_standard_key(self):
        # 1. Arrange: Datei im RAM-Dateisystem erstellen
        self.fs.create_file(self.CONFIG_PATH, contents=cleandoc("""
        keys = [
            # A list of available commands that can be bound to keys can be found
            # at https://docs.qtile.org/en/latest/manual/config/lazy.html
            # Switch between windows
            Key([mod], "left", lazy.layout.left(), desc="Move focus to left")
        ]
        """))

        # 2. Act: Funktion ausführen
        result = read_qtile_keymap(self.CONFIG_PATH)

        # 3. Assert: Unittest-Assertion nutzen
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "Super + left\tMove focus to left")

    def test_two_mods(self):
        # Jedes Testergebnis ist isoliert. Wir können andere Inhalte definieren.
        self.fs.create_file(self.CONFIG_PATH, contents=cleandoc("""
        keys = [
            Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        ]
        """))

        result = read_qtile_keymap(self.CONFIG_PATH)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "Super + Control + r\tReload the config")


    def test_group_keys_are_extracted(self):
        # Jedes Testergebnis ist isoliert. Wir können andere Inhalte definieren.
        self.fs.create_file(self.CONFIG_PATH, contents=cleandoc("""
        groups = [
            Group(name=group_names[0], layout = "columns"),
            Group(name=group_names[1], layout = "max", matches=[Match(wm_class="jetbrains-idea")]),
            Group(name=group_names[2], screen_affinity=1, layout = "max", matches=[Match(wm_class="google-chrome"), Match(wm_class="qutebrowser")]),
            Group(name=group_names[3], layout = "columns"),
            Group(name=group_names[4], layout = "columns", matches=[Match(wm_class="keepassxc")]),
            Group(name=group_names[5], layout = "columns"),
            ScratchPad("scratchpad", [
                DropDown("term", "kitty"),
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
                    ])
            return localkeys
        """))

        result = read_qtile_keymap(self.CONFIG_PATH)
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0], "Super + 1\tSwitch to group 1")
        self.assertEqual(result[1], "Super + 2\tSwitch to group 2")
        self.assertEqual(result[2], "Super + 3\tSwitch to group 3")
        self.assertEqual(result[3], "Super + 4\tSwitch to group 4")
        self.assertEqual(result[4], "Super + 5\tSwitch to group 5")
        self.assertEqual(result[5], "Super + 6\tSwitch to group 6")


if __name__ == "__main__":
    unittest.main()

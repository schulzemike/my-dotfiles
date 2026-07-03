import ast
import os
import sys


def read_qtile_keymap(config_filepath: str) -> list[str]:
    with open(os.path.expanduser(config_filepath), "r") as f:
        tree = ast.parse(f.read())

    def resolve_val(node):
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            return str(node.value)
        return ""

    def resolve_mods(key_node) -> list[str]:
        if key_node.args and isinstance(key_node.args[0], ast.List):
            return [resolve_val(el) for el in key_node.args[0].elts]
        return []

    def resolve_key(key_node, tree_root=None) -> list[str]:
        if len(key_node.args) > 1:
            key_arg = key_node.args[1]
            if isinstance(key_arg, ast.Constant) and isinstance(key_arg.value, str):
                return [str(key_arg.value)]

            elif isinstance(key_arg, ast.Subscript):
                if isinstance(key_arg.value, ast.Name):
                    array_name = key_arg.value.id

                    # 1. Zuerst ermitteln wir, wie viele Gruppen tatsächlich definiert sind
                    # (Das emuliert das `enumerate(groups)` aus deiner Config)
                    num_groups = 0
                    for outer_node in ast.walk(tree_root):
                        if isinstance(outer_node, ast.Assign):
                            for target in outer_node.targets:
                                if isinstance(target, ast.Name) and target.id == 'groups':
                                    if isinstance(outer_node.value, ast.List):
                                        # Zähle nur echte Group-Objekte, ignoriere ScratchPads
                                        num_groups = sum(
                                            1 for el in outer_node.value.elts
                                            if isinstance(el, ast.Call) and getattr(el.func, 'id', '') == 'Group'
                                        )

                    # 2. Jetzt holen wir die Keys aus dem Array (z.B. keys_for_groups)
                    for outer_node in ast.walk(tree_root):
                        if isinstance(outer_node, ast.Assign):
                            for target in outer_node.targets:
                                if isinstance(target, ast.Name) and target.id == array_name:
                                    if isinstance(outer_node.value, ast.List):
                                        all_keys: list[str] = [
                                            str(el.value) for el in outer_node.value.elts if isinstance(el, ast.Constant)
                                        ]
                                        # Schneide das Array auf die tatsächliche Anzahl der Gruppen zu
                                        return all_keys[:num_groups]
        return []

    def resolve_key_description(key_node) -> str:
        for kw in key_node.keywords:
            if kw.arg == 'desc' and isinstance(kw.value, ast.Call) and isinstance(kw.value.func, ast.Attribute) and isinstance(kw.value.func.value, ast.Constant):
                desc_constant = kw.value.func.value
                if isinstance(desc_constant.value, str):
                    return str(desc_constant.value)
            if kw.arg == 'desc' and (isinstance(kw.value, ast.Constant) or isinstance(kw.value, ast.Call)):
                desc_constant = kw.value
                if isinstance(desc_constant.value, str):
                    return str(desc_constant.value)
        return ""

    key_bindings = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'Key':
            mods = resolve_mods(node)
            mod_list = ["Super" if m == "mod" else "Alt" if m == "alt" else m.capitalize() for m in mods]
            combo_base = " + ".join(mod_list)

            key_names = resolve_key(node, tree)

            for key_name in key_names:
                combo = f"{combo_base} + {key_name}"
                desc = resolve_key_description(node).format(key_name)
                key_bindings.append((combo, desc))

    return [f"{combo}\t{desc}" for combo, desc in key_bindings]


if __name__ == "__main__":
    # sys.argv[0] is the script name itself
    # sys.argv[1] is the first user parameter
    if len(sys.argv) < 2:
        print("Error: Please provide a parameter.")
        sys.exit(1)

    for line in read_qtile_keymap(sys.argv[1]):
        print(line)

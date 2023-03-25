COLOR_CYAN = '\033[96m'
COLOR_GREEN = '\033[92m'
COLOR_WARNING = '\033[93m'
COLOR_END = '\033[0m'


def print_success(msg: str):
    print(f"{COLOR_CYAN}y.k.'s node suite:{COLOR_END} {COLOR_GREEN}{msg}{COLOR_END}")


def print_info(msg: str):
    print(f"{COLOR_CYAN}y.k.'s node suite:{COLOR_END} {msg}")


def print_error(msg: str):
    print(f"{COLOR_CYAN}y.k.'s node suite:{COLOR_END} {COLOR_WARNING}{msg}{COLOR_END}")


PACKAGE_EXISTS = {}

COMFYUI_ROOT = None


def comfyui_root():
    global COMFYUI_ROOT

    if COMFYUI_ROOT:
        return COMFYUI_ROOT

    import os

    root = os.path.dirname(__file__)

    while True:
        new_root = os.path.dirname(root)
        # no more parent
        if new_root == root:
            raise ValueError("could not find comfyui root")
        root = new_root

        # found custom_nodes
        if os.path.basename(root) == "custom_nodes":
            COMFYUI_ROOT = os.path.dirname(root)
            return COMFYUI_ROOT


def ensure_package(name: str):
    global PACKAGE_EXISTS

    if PACKAGE_EXISTS.get(name, False):
        return

    import sys
    import subprocess

    current = [
        r.decode().split('==')[0].strip()
        for r in subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).split()
    ]

    if name in current:
        PACKAGE_EXISTS[name] = True
        return

    print_info(f"installing {name}...")

    subprocess.check_call([sys.executable, '-m', 'pip', '-q', 'install', name])

    print_success(f"installed {name}...")

import platform
from json import dump, loads
from os import path, stat, system
from pathlib import Path
from time import time
from typing import Any


def save_json(obj_str: str, out_path: str, file_name: str) -> None:
    out_path = Path(out_path)
    out_path.mkdir(parents=True, exist_ok=True)

    with (out_path / file_name).open("w") as out_file:
        dump(loads(obj_str), out_file)


def save_file(obj: Any, out_path: str, file_name: str) -> None:
    out_path = Path(out_path)
    out_path.mkdir(parents=True, exist_ok=True)

    with (out_path / file_name).open("w") as out_file:
        out_file.write(obj)


def delete_file(path: str, file_name: str) -> None:
    (Path(path) / file_name).unlink()


def generate_js_save_script(base_str: str, out_path: str, file_name: str) -> str:
    return (
        base_str
        + f"""
const fs = require('fs');
if (Object.keys(exports).length === 1)
    fs.writeFileSync(`{out_path}/{file_name}`, JSON.stringify(exports[Object.keys(exports)[0]]));
else
    fs.writeFileSync(`{out_path}/{file_name}`, JSON.stringify(exports));
    """
    )


def save_js(js_str: str, out_path: str, file_name: str = None) -> None:
    temp_file_name = "temp.js"
    out_js = generate_js_save_script(js_str, out_path, file_name)

    save_file(out_js, out_path, temp_file_name)
    system(f"node {out_path}/{temp_file_name}")
    delete_file(out_path, temp_file_name)


def file_exists(check_path):
    return Path(check_path).is_file()


def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == "Windows":
        return path.getctime(path_to_file)
    else:
        f_stat = stat(path_to_file)
        try:
            return f_stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return f_stat.st_mtime


def get_time_delta_now(path_to_file):
    return time() - creation_date(path_to_file)

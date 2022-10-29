from json import dump
from pathlib import Path


def save_json(obj: dict, out_path: str, file_name: str) -> None:
    out_path = Path(out_path)
    out_path.mkdir(parents=True, exist_ok=True)

    with (out_path / file_name).open('w') as out_file:
        dump(obj, out_file)

from pathlib import Path
from typing import Dict, Union

import attr
from furl import furl
from ruamel import yaml


@attr.s(auto_attribs=True)
class Redirect:
    destination: furl
    status_code: int = 307
    maintain_path: bool = True


def parse_config_entry(entry: Union[str, dict]) -> Redirect:
    if isinstance(entry, str):
        return Redirect(destination=entry)
    return Redirect(**entry)


def read_config(path: Path) -> Dict[str, Redirect]:
    config = {}
    for k, v in yaml.safe_load(path.read_text()).items():
        config[k] = parse_config_entry(v)
    return config

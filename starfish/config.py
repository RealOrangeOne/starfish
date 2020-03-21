from pathlib import Path
from string import Template
from typing import List, Union

import attr
from furl import furl
from ruamel import yaml

CADDY_TEMPLATE = Template(
    """
$source {
    redir $destination $status_code
}
"""
)


@attr.s(auto_attribs=True)
class Redirect:
    source: furl
    destination: furl
    status_code: int = 307
    maintain_path: bool = True

    @property
    def caddy_destination(self) -> str:
        destination = self.destination.url
        if self.maintain_path:
            destination += "{uri}"
        return destination

    def as_caddy_rule(self) -> str:
        return CADDY_TEMPLATE.substitute(
            {
                "source": self.source.url,
                "destination": self.caddy_destination,
                "status_code": self.status_code,
            }
        )


def parse_config_entry(source: str, entry: Union[str, dict]) -> Redirect:
    if isinstance(entry, str):
        return Redirect(source=furl(source), destination=furl(entry))
    destination = entry.pop("destination")
    return Redirect(source=furl(source), destination=furl(destination), **entry)


def read_config(path: Path) -> List[Redirect]:
    return [
        parse_config_entry(k, v) for k, v in yaml.safe_load(path.read_text()).items()
    ]

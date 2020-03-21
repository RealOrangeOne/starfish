import argparse
import logging
from pathlib import Path

import coloredlogs

from .redirect import read_redirects

CADDY_GLOBAL_OPTIONS = """
{
    admin off
}
"""


def valid_input_file(arg: str):
    if not Path(arg).exists():
        raise argparse.ArgumentTypeError(f"{arg} does not exist")
    return Path(arg).resolve()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=valid_input_file)
    parser.add_argument("output", type=Path)
    return parser.parse_args()


def main():
    coloredlogs.install(
        level=logging.INFO, fmt="%(levelname)s %(message)s",
    )
    args = get_args()
    args.output = args.output.resolve()
    if args.output.exists():
        logging.warning(f"File '{args.output}' already exists, overriding")
    redirects = read_redirects(args.input)
    logging.info("Found %s redirects", len(redirects))
    args.output.write_text(
        CADDY_GLOBAL_OPTIONS
        + "\n".join([redirect.as_caddy_site() for redirect in redirects])
    )
    logging.info("Wrote %s redirects to %s", len(redirects), str(args.output))


if __name__ == "__main__":
    main()

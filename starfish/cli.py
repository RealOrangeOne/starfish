import argparse
import logging
from pathlib import Path

import coloredlogs

from .config import read_config


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
    config = read_config(args.input)
    logging.info("Found %s redirect rules", len(config))
    args.output.write_text("\n".join([redirect.as_caddy_rule() for redirect in config]))
    logging.info("Wrote %s rules to %s", len(config), str(args.output))


if __name__ == "__main__":
    main()

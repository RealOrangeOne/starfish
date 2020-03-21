#!/bin/sh

set -e

python -m starfish /config/redirects.yml /config/Caddyfile

caddy run --config /config/Caddyfile --adapter caddyfile

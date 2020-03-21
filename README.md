# Starfish

Starfish generates Caddy `Caddyfile` configurations based off a simple YAML file, to perform redirections.

## Requirements

Install the dependencies in `requirements.txt` inside your environment with `pip install -r requirements.txt`.

You'll also need a valid `redirect.yml` file. An example can be found at `starfish/example-redirects.yml`.

## Usage

The easiest way to use this is via Docker, and `docker-compose`:

```yaml
version: "2.3"

services:
  caddy:
    image: theorangeone/starfish
    container_name: starfish
    volumes:
      - ./redirects.yml:/config/redirects.yml
    ports:
      - 80:80
    restart: unless-stopped

```

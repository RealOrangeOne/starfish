FROM caddy/caddy:v2.0.0-beta.17-alpine as caddy

FROM python:3.8.1-alpine3.11

COPY --from=caddy /usr/bin/caddy /usr/bin/caddy

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./starfish /app/starfish
COPY docker-entrypoint.sh /app/docker-entrypoint.sh

COPY ./starfish/example-redirects.yml /config/redirects.yml

WORKDIR /app

EXPOSE 80
EXPOSE 443

CMD ["/app/docker-entrypoint.sh"]

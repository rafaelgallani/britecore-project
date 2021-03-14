# Dockerfile

FROM python:3.9.1-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends

COPY nginx.default /etc/nginx/sites-available/default

RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/app

COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache

RUN chown -R www-data:www-data /opt/app

EXPOSE 8000
EXPOSE 8010
STOPSIGNAL SIGTERM
CMD ["/opt/app/start.sh"]

WORKDIR /opt/app
# Dockerfile
FROM python:3.8

# install nginx
RUN apt-get update
#RUN apt-get install nginx vim -y --no-install-recommends
#COPY nginx.conf /etc/nginx/sites-available/default
#RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app/
COPY . /opt/app/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/.pip_cache
RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 8000
#EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]

# Version: 0.0.1
FROM ubuntu:18.04
RUN apt-get update && apt-get install -y apt-transport-https && apt-get install -my wget gnupg1
RUN apt-get install -y nginx
RUN apt-get install -y wget
RUN apt-get install -y python2.7
RUN apt-get install -qqy curl
RUN wget https://github.com/nginxinc/nginx-amplify-agent/raw/master/packages/install.sh
RUN curl -fs http://nginx.org/keys/nginx_signing.key | apt-key add -

# Keep the nginx logs inside the container
RUN unlink /var/log/nginx/access.log \
    && unlink /var/log/nginx/error.log \
    && touch /var/log/nginx/access.log \
    && touch /var/log/nginx/error.log \
    && chown www-data /var/log/nginx/*log \
    && chmod 644 /var/log/nginx/*log
 
COPY ./index.html /usr/share/nginx/html/index.html
COPY ./default /etc/nginx/sites-available/default
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./conf.d/stub_status.conf /etc/nginx/conf.d
#COPY ./install.sh /install.sh
RUN service nginx restart
EXPOSE 80 443
CMD ["/bin/bash", "-l"]
CMD ["nginx", "-g", "daemon off;"]

RUN API_KEY='edb94368136bd64922ad1c60d4be238a' sh ./install.sh -y
RUN service amplify-agent start

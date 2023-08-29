FROM nginx
RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY gateway/config/* /etc/nginx

RUN mkdir api_conf.d

COPY gateway/config/api_conf.d/bookstore_api.conf /etc/nginx/api_conf.d/bookstore_api.conf

COPY gateway/certs/bookstore.crt /etc/ssl/certs/bookstore.crt
COPY gateway/certs/bookstore.key /etc/ssl/certs/bookstore.key
FROM centos:7
RUN yum install httpd -y && \
    yum install net-tools -y
COPY ./index.html /var/www/html/
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
EXPOSE 80
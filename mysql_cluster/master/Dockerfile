FROM mysql:latest

USER root
RUN echo "master" > master.txt

ADD master.cnf /engn001/mysql/
ADD master-entrypoint.sh /usr/local/bin
RUN chmod 640 /engn001/mysql/master.cnf
RUN chmod 755 /usr/local/bin/master-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/slave-entrypoint.sh"]
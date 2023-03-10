FROM mysql:latest

USER root
RUN echo "slave" > slave.txt

ADD slave.cnf /engn001/mysql/
ADD slave-entrypoint.sh /usr/local/bin
RUN chmod 640 /engn001/mysql/slave.cnf
RUN chmod 755 /usr/local/bin/slave-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/slave-entrypoint.sh"]
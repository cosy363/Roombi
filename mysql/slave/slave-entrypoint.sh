#!/bin/bash
set -e
rm -rf /engn001/mysql/data/auto.cnf
/engn001/mysql/bin/mysqld --defaults-file=/engn001/mysql/slave.cnf &

sleep 30
## create user
/engn001/mysql/bin/mysql -uroot -p'qhdks123' -S /engn001/mysql/data/mysql.sock -e "create user 'replUser'@'172.16.0.%' identified with mysql_native_password"
/engn001/mysql/bin/mysql -uroot -p'qhdks123' -S /engn001/mysql/data/mysql.sock -e "alter user 'replUser'@'172.16.0.%' identified by 'qhdks123'"
/engn001/mysql/bin/mysql -uroot -p'qhdks123' -S /engn001/mysql/data/mysql.sock -e "grant replication slave on *.* to 'replUser'@'172.16.0.%'"



## get  status

master_log_file=`/engn001/mysql/bin/mysql -uroot -p'qhdks123' -h 172.16.0.10 -S /engn001/mysql/data/mysql.sock -e"show master status\G" | grep mysql-bin`
re="[a-z]*-bin.[0-9]*"

if [[ ${master_log_file} =~ $re ]];then
    master_log_file=${BASH_REMATCH[0]}
fi

master_log_pos=`/engn001/mysql/bin/mysql -uroot -p'qhdks123' -h 172.16.0.10 -S /engn001/mysql/data/mysql.sock -e"show master  status\G" | grep Position`

re="[0-9]+"

if [[ ${master_log_pos} =~ $re ]];then
    master_log_pos=${BASH_REMATCH[0]}
fi

query="change master to master_host='172.16.0.10', master_user='replUser', master_password='qhdks123', master_log_file='${master_log_file}', master_log_pos=${master_log_pos}, master_port=3306"

mysql -uroot -p'qhdks123' -S /engn001/mysql/data/mysql.sock -e "${query}"
mysql -uroot -p'qhdks123' -S /engn001/mysql/data/mysql.sock -e "start slave"
/bin/bash


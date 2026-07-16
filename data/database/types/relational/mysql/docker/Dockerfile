FROM mysql
ENV MYSQL_ROOT_PASSWORD 123
COPY script.sql /docker-entrypoint-initdb.d # files in this folder are automatically executed by mysql image when the container starts

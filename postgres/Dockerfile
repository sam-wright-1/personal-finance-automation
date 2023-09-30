FROM postgres:15
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB personal_finance

COPY postgres/init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

# Any copy commands

CMD ["postgres"]
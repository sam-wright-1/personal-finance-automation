FROM postgres:15
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=personal_finance

COPY lib/postgres/sql/init.sql /docker-entrypoint-initdb.d/

# Any copy commands

CMD ["postgres"]
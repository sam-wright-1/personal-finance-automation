FROM postgres:15
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=personal_finance

COPY lib/postgres/sql/init.sql /docker-entrypoint-initdb.d/

EXPOSE 6543

# Any copy commands

CMD ["postgres"]
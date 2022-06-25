#!/bin/bash

psql -d postgres -tc "SELECT 1 FROM pg_database WHERE datname = '${POSTGRES_DBNAME}'" | grep -q 1 || createdb $POSTGRES_DBNAME
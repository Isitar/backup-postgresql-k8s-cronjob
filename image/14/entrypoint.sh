#!/bin/bash
pg_dumpall --no-owner --no-privileges -U $POSTGRES_USER -p $POSTGRES_PASSWORD -h $POSTGRES_HOST | gzip > backup.sql
python3 main.py backup.sql
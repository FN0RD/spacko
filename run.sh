#!/bin/sh
celery -A spacko.celery worker --loglevel=info &
python spacko.py

#!/usr/bin/env bash

cd ..

echo `ls`

echo `pwd`

celery -B -A celery_task worker --loglevel=info
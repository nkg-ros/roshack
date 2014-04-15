#!/bin/bash

MY_DIR=`dirname $0`
NAME="hack"                                  # Name of the application
APP_DIR=$MY_DIR/..             # Django project directory
USER=hack
GROUP=hack
NUM_WORKERS=5
WSGI_MODULE=app
ADDRESS=127.0.0.1:5001

echo $APP_DIR
cd $APP_DIR
echo $HOME

# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn 'app:app' \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --bind=$ADDRESS

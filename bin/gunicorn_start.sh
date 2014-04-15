#!/bin/bash

MY_DIR=`dirname $0`
NAME="hack"                                  # Name of the application
APP_DIR=$MY_DIR/..             # Django project directory
#SOCKFILE=/tmp/$NAME.gunicorn.sock
USER=hack
GROUP=hack
NUM_WORKERS=5
#SETTINGS_FILE=settings.production
WSGI_MODULE=app
ADDRESS=127.0.0.1:5001
#echo "Starting $NAME as `whoami`"

# Activate the virtual environment
echo $APP_DIR
cd $APP_DIR
echo $HOME
#export SETTINGS_FILE=$SETTINGS_FILE
#export PYTHONPATH=$APP_DIR:$PYTHONPATH:..


# Create the run directory if it doesn't exist
#RUNDIR=$(dirname $SOCKFILE)
#test -d $RUNDIR || mkdir -p $RUNDIR
#gunicorn -w=4 'app:create_app(settings_module="settings.production")'
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn 'app:app' \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --bind=$ADDRESS

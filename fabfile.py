from fabric.api import env, run, sudo, local, put, hosts
env.remote_user = "hack"
env.user = "hack"
env.host = 'hack.galv.in'
env.hosts = [env.host,]
env.base_dir = "/home/hack/www/roshack"
env.app_name = "app"
env.domain_name = "hack.galv.in"
env.git_clone = "https://github.com/nkg-ros/roshack"

def start_nginix():
    """Start the application servers"""
    sudo("service nginix start")

def restart_nginix():
    """Restarts your application"""
    sudo("service nginix reload")

def stop_nginix():
    """Stop the application servers"""
    sudo("service nginix  stop")


def resart_supervisor():
    sudo("supervisorctl reload hack")


def checkout():
    """Checkout code to the remote servers"""
    run("cd /home/hack/www/roshack; git pull")

def requirements():
    sudo("cd  /home/hack/www/roshack;  pip install -r requirements.txt")

#@hosts(['hack.galv.in'])
def deploy():
    checkout()
    requirements()
    resart_supervisor()

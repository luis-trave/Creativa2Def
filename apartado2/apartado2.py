#!usr/bin/python3
from subprocess import call
import os


os.system('sudo apt-get remove docker docker-engine docker.io containerd runc')
os.system('sudo apt-get install docker.io')

os.system('docker rmi $(docker imagenes -q)')
call(['sudo','docker', 'build', '-t', '36/product-page', '.'])
os.system('sudo docker run -it --name 36-productpage -p 9080:9080 --env GROUP_NUMBER=36 36/product-page')

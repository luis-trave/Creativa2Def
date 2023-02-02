#!usr/bin/python3
from subprocess import call
import os

os.system('sudo docker rm /36-productpage')
call(['sudo','docker', 'build', '-t', '36/product-page', '.'])
os.system('sudo docker run -it --name 36-productpage -p 9080:9080 --env GROUP_NUMBER=36 36/product-page')

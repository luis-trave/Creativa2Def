#!usr/bin/python3
from subprocess import call
import os

os.system('sudo docker rm /36-productpage')
os.system('sudo docker rm /36-details')
os.system('sudo docker rm /36-reviews')
os.system('sudo docker rm /36-ratings')


os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')
os.chdir('practica_creativa2/bookinfo/src/reviews')
os.system('sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')
os.chdir(os.path.expanduser("~"))

os.system('sudo docker-compose build')


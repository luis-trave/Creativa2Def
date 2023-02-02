#!usr/bin/python3
from subprocess import call
import os

os.system('apt-get remove docker docker-engine docker.io containerd runc')
os.system('apt-get update')
os.system('apt-get install -y ca-certificates curl gnupg lsb-release')
os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg')
os.system('echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
os.system('apt-get update')
os.system('apt-get install -y docker-ce docker-ce-cli containerd.io')

call(['sudo','docker', 'build', '-t', '36/product-page', '.'])
os.system('sudo docker run -it --name 36-productpage -p 9080:9080 --env GROUP_NUMBER=36 36/product-page')

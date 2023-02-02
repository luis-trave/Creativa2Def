#!/usr/bin/python3
from subprocess import call
import os 

call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
call(['sudo', 'apt-get', 'update'])
call(['sudo', 'apt-get', 'install', '-y', 'python3-pip'])

call(['pip3', 'install', '-r', 'requirements.txt'])

os.chdir('practica_creativa2/bookinfo/src/productpage')

os.environ['GROUP_NUMBER'] = '36'
numGrupo = os.environ.get('GROUP_NUMBER')

os.chdir('templates')
call(['mv', 'productpage.html', 'productpage_temporal.html'])
fin = open('productpage_temporal.html', 'r')
fout = open('productpage.html', 'w')

for line in fin:
	# Cambiamos el titlte del html con la variable recibida del python
	if '{% block title %}Simple Bookstore App{% endblock %}' in line :
		fout.write(line.replace('{% block title %}Simple Bookstore App{% endblock %}', '{% block title %}Simple Bookstore App [' + numGrupo + ']{% endblock %}'))
	else :
		fout.write(line)

fin.close()
fout.close()
call(['rm', '-f', 'productpage_temporal.html'])

os.chdir('..')
call(['python3', 'productpage_monolith.py', '9080'])

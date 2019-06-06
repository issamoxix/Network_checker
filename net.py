#CHeck How many of ip addresses are connected to the same network as you
#Using a simple commande line ping -a
#all the ip adresses are stored in a txt file call count(a,b).txt
#how to use >py net.py a b
#where a<b a and b are integers [a,b]
import subprocess
import sys
import os
# intervale [y,z]
def my(x,f):
    cp = subprocess.run(["ping",'-n','1',"192.168.1."+str(x)], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if 'Impossible' in cp.stdout:
        print('NOt FOund =>'+"192.168.1."+str(x))
    else:
        print('FOUND =>'+"192.168.1."+str(x))
        f.write("192.168.1."+str(x)+"\n")
def start(y,z):
    f = open('count('+str(y)+','+str(z)+').txt','a')
    for x in range(y,z+1):
        my(x,f)
    f.close()
if sys.argv[1]>sys.argv[2]:
    print('You should try a<b')
else:
    start(int(sys.argv[1]),int(sys.argv[2]))
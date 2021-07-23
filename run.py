from server import keep
from os import name,system

cmd=input("[#]Insert command to run your script")

keep()
system("cls") if name=="nt" else system("clear")
system(cmd)

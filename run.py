from server import keep
import os

with open("cmd.txt","r") as f:
    cmd=f.read()
    f.close()

keep()
os.system(cmd)

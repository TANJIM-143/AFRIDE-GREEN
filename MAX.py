import os, sys
os.system("git pull")
try:
    __import__("GREEN").Main_TNX()
except Exception as e:
    exit(str(e))
 

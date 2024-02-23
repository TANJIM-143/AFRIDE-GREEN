import os, sys
os.system("git pull")
try:
    __import__("MAX").Main_TNX()
except Exception as e:
    exit(str(e))
 

import os, sys
os.system("git pull")
try:
    __import__("RNDM").menu()
except Exception as e:
    exit(str(e))
 

-1

This question is asking a solution to the Fix a slow system with Python test of the Troubleshooting and Debugging Techniques (Week 2) course of Google, hosted on the Coursera platform.

In my code, I list all the directories inside data/prod/ and then I use that list as a parameter to the run function that runs in a Pool of Process, so that I launch more instances of rsync in parallel

It is ready to use and you can even just copy-paste it, but remember that you must change your username accordingly (it should be in a format like student-03-12345678, look at the code comments to change it).

#!/usr/bin/env python
import os
import subprocess
from multiprocessing import Pool

src = "data/prod/"
dest = "data/prod_backup/"

def run(dir):
    subprocess.call(["rsync", "-arq", src + str(dir), dest])

os.chdir(os.getenv("HOME"))
dirs = []
for path,dir,file in os.walk(src):
    dirs.append(dir)

dirs=dirs[0]
print(dirs) #Used to debug

# Create the pool
p = Pool(len(dirs))

# Start tasks
p.map(run, dirs)

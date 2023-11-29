import os
from datetime import datetime
4
5 os.chdir (' /Users/coreyschafer /Desktop/')
6
7 mod_time = os.stat ('demo.txt') .st_mtime
" 8 print (datetime. fromtimestamp (mod_time))
9
10 # print(os.listdir ())
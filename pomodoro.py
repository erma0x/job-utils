import time
import os
from datetime import datetime


t1 = datetime.now()
while True:
    os.system('clear')
    t2 = datetime.now()-t1
    print('\n\t',str(t2)[:7])

    
    if str(t2)[:7] == "0:25:00":
    	print('pomodoro ended')
    	break
    	
    time.sleep(1)

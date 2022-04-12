
import subprocess
import os
import sys
from datetime import datetime, timedelta
from threading import Timer


# x = datetime.today()
# y = x.replace(day=x.day, hour=19,minute=50,second=0,microsecond=0) + timedelta(days=0)
# delta_t = y-x

# secs = delta_t.total_seconds()

# def hellow():
#     print("Heeey")



#t = Timer(secs,hellow)
#t.start()

##### runing test case works !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def Run_test():
    current_dir = os.path.abspath(__file__)
    head, tiel = os.path.split(current_dir)
    test_case_name = "\\01_robot-file.robot"
    Running_test_case = head + test_case_name
    python_pathy = sys.executable
    subprocess.call([python_pathy,'-m','robot',Running_test_case])
    print(head)

Run_test()

# import sys
# print (sys.executable)
# print(sys.version)
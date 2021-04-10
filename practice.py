import psutil

from time import sleep
from pprint import pprint


def getProcesses():
    try:
        for proc in psutil.process_iter():
            pid = proc.as_dict(attrs=['pid'])

            p = psutil.Process(pid['pid'])
            print(p.name(), p.status(), p.cpu_percent(interval=1))
    except Exception as e:
        pass


while True:
    getProcesses()

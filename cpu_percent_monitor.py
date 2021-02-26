import psutil

while True:
    p = psutil.cpu_percent()
    print(p)
    import os
    from time import sleep
    sleep(0.8)
    os.system("clear")

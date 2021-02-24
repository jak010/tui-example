
import psutil
from progress.bar import Bar
from pprint import pprint
from time import sleep

bar = Bar("Processing", max=100, suffix="%(index).1f%% - %(max)d%% cpu  ")

while True:
    p = psutil.cpu_percent()
    bar.index = float(p)
    bar.next()
    sleep(0.2)
bar.finish()

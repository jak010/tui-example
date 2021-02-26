
import psutil

p = psutil.Process(560).as_dict()

print(p)
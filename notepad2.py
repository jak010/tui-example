import psutil


class CpuStat(object):
    def __init__(self):
        self.current_cpu = None

    def update_cpu(self, cpu):
        print("Before:", self.current_cpu)
        if self.current_cpu != cpu:
            self.current_cpu = cpu

    def save_cpu(self, cpu):
        self.current_cpu = cpu
        print("After",self.current_cpu )
        return float(self.current_cpu)


cpu = CpuStat()
from time import sleep

while True:
    cpu_value = psutil.cpu_percent()
    cpu.save_cpu(cpu_value)
    sleep(1)
    cpu.update_cpu(cpu_value)

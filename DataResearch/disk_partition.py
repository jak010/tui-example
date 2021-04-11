import psutil

cpu_core = psutil.cpu_count() # 논리 프로세서 수
cpu_count = psutil.cpu_count(logical=False) # 물리적인 코어 수

print(cpu_core)
print(cpu_count)

mem_total = psutil.virtual_memory()
mem_total_data = mem_total.total / 1024 ** 3
mem_avail = mem_total.available / 1024 ** 3
print(f"{round(mem_total_data)} GB")
print(f"{round(mem_avail,1 )} GB")
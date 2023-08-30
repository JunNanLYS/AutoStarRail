from concurrent.futures import ThreadPoolExecutor

print("开启线程池")
script_thread = ThreadPoolExecutor(max_workers=1)  # 脚本线程
function_thread = ThreadPoolExecutor(max_workers=3)  # 方法线程
print("线程池开启完毕")

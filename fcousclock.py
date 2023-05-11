import time

focus_duration = 25 # 专注时间长度为25分钟
break_duration = 5 # 休息时间长度为5分钟

while True: # 无限循环
    print("Focus!") # 打印 "专注！"
    time.sleep(focus_duration*60) # 等待"专注时间长度*60"秒
    
    print("Break!") # 打印 "休息！"
    time.sleep(break_duration*60) # 等待 "休息时间长度*60" 秒

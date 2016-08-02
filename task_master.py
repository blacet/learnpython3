'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')
'''

# Windows下调试通过
#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# task_master.py for win7

import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support


# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从BaseManager集成的QueueManager
class QueueManager(BaseManager):
    pass

# win7 不能运行问题 用于替换lambda
def return_task_queue ():
    global task_queue
    return task_queue

def return_result_queue ():
    global result_queue
    return result_queue

# win7 问题 需要把代码放入函数中, 原因不明
def test ():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象 : 
    # QueueManager.register('get_task_queue', callable=lambda: task_queue)   
    # QueueManager.register('get_result_queue', callable=lambda: result_queue)
    QueueManager.register('get_task_queue', callable=return_task_queue)   
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口5000, 设置验证码'abc'
    #manager = QueueManager(address=('', 5000), authkey=b'abc')
    # win7需要写ip地址
    manager = QueueManager(address=('172.16.73.89', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()
    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果
    print('Try get result...')
    for i in range(10):
        # 这里我自己加了异常捕获
        # 运行这个后应该接着在另一个cmd中运行 task_worker.py, 不然一直获取不到数据
        try:
            r = result.get(timeout = 5)
            print('Result: %s' % r)
        except queue.Empty: # 老师的是Queue.Empty 我这里报错了, 改为 queue.Empty
            print('result queue is empty.')
    # 关闭
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    freeze_support()
    test()
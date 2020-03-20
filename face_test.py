from multiprocessing import Process
import time
from time import sleep


'''开启子进程的两种方式'''

# def test(name):
#     print("%s is running",name)
#     sleep(1)
#     print("%s is done")
#
# if __name__ == '__main__':
#     p = Process(target=test,args=("jack",))
#     p.start()

# class MyProcess(Process):
#     def __init__(self,name):
#         super(MyProcess, self).__init__()
#         self.name = name
#
#     def run(self):
#         print("%s is running", self.name)
#         sleep(1)
#
# if __name__ == '__main__':
#     p = MyProcess("jack")
#     p.start()

'''进程间相互隔离'''
# x = 1999
#
# def test():
#     global x
#     x = 0
#     print("x is %s",x)
#
# if __name__ == '__main__':
#     print(x)
#     p = Process(target=test)
#     p.start()
#     print(x)

'''join函数'''
# 调用start函数之后，就由操作系统来玩了，至于何时开启进程，何时执行
# x = 1000
# def test():
#     global x
#     x = 10
#     print("test's x is", x)
#     # sleep(1)
#
# if __name__ == '__main__':
#     p = Process(target=test)
#     p.start()
#
#     p.join()  # 让父进程在原地等
#     print(x)
'''案例2'''
# def test(num):
#     print("test num is %s" %num)
#     sleep(1)
#
# if __name__ == '__main__':
#     p1 = Process(target=test,args=(1,))
#     p3= Process(target=test,args=(3,))
#     p4 = Process(target=test,args=(4,))
#     p5 = Process(target=test,args=(5,))
#     p1.start()
#     p3.start()
#     p4.start()
#     p5.start()
#     # p1.join()
#     # p3.join()
#     # p4.join()



def task(n):
    print('%s is running' % n)
    time.sleep(1)


if __name__ == '__main__':
    start_time = time.time()

    p1 = Process(target=task, args=(1,))
    p2 = Process(target=task, args=(2,))
    p3 = Process(target=task, args=(3,))
    p1.start()
    p2.start()
    p3.start()

    p3.join()  # 3s
    p1.join()
    p2.join()

    print('主', (time.time() - start_time))

    start_time = time.time()
    p_l = []
    for i in range(1, 4):
        p = Process(target=task, args=(i,))
        p_l.append(p)
        p.start()
    for p in p_l:
        p.join()

    print('主', (time.time() - start_time))
















import threading
import time


"""
多线程
"""
class Mythread():
    counter = 0
    lock = threading.Lock()  # 添加一个锁

    def __init__(self):
        pass

    # 定义一个线程执行的函数
    def my_thread_function1(self):
        for i in range(3):
            time.sleep(1)
            with self.lock:  # 使用上下文管理器自动处理锁的获取和释放
                Mythread.counter += 1
                print("Thread 1:", i)

    def my_thread_function2(self):
        for i in range(5):
            time.sleep(0.5)
            with self.lock:  # 使用上下文管理器自动处理锁的获取和释放
                Mythread.counter += 1
                print("Thread 2:", i)


if __name__ == '__main__':
    mythread = Mythread()
    t1 = threading.Thread(target=mythread.my_thread_function1)
    t2 = threading.Thread(target=mythread.my_thread_function2)

    # 启动线程
    t1.start()
    print("t1 start")
    t2.start()
    print("t2 start")

    # 等待所有线程完成
    t1.join()
    print("All threads completed.")
    t2.join()

    print("Main thread waiting for threads to complete...")

    print("Counter (instance):", mythread.counter)
    print("Counter (class):", Mythread.counter)
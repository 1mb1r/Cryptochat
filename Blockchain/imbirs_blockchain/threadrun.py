from node import Node
from mainn import OneWindow
from threading import Thread

thread1 = Thread(target=OneWindow.main, args=())
thread2 = Thread(target=Node.start, args=())

thread1.start()
thread2.start()
thread1.join()
thread2.join()
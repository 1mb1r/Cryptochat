import node
from mainn import OneWindow
from threading import Thread

thread1 = Thread(target=OneWindow.main, args=())
thread2 = Thread(target=node.start, args=())

thread2.start()
thread1.run()
# thread1.join()
# thread2.join()

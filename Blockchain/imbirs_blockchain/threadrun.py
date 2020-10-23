from pyngrok import ngrok
import node
from mainn import OneWindow
from threading import Thread
from blockchain import *



public_url = ngrok.connect(5000)
print(public_url)
# blockkek = Blockchain()
# blockkek.add_peer_node(public_url)
thread1 = Thread(target=OneWindow.main, args=())
thread2 = Thread(target=node.start, args=())


thread2.start()
thread1.run()
# thread1.join()
# thread2.join()

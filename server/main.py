import listener
from multiprocessing import Process
import time

def process_one():
    listener.iniz()
    listener.start_listener()

listen_process = Process(target=process_one)
listen_process.start()



print("[critical] ", "server started")





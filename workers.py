import time
from multiprocessing import Process
from flask import Flask
worker_1 = Flask("Server #1")
worker_2 = Flask("Server #2")
worker_3 = Flask("Server #3")
worker_4 = Flask("Server #4")
worker_5 = Flask("Server #5")

@worker_1.route('/', methods=['GET'])
def ping():
    time.sleep(5)
    return "1"

@worker_2.route('/', methods=['GET'])
def ping():
    time.sleep(5)
    return "2"

@worker_3.route('/', methods=['GET'])
def ping():
    time.sleep(5)
    return "3"

@worker_4.route('/', methods=['GET'])
def ping():
    time.sleep(5)
    return "4"

@worker_5.route('/', methods=['GET'])
def ping():
    time.sleep(5)
    return "5"

if __name__ == "__main__":
    p1 = Process(target=lambda: worker_1.run(port=7001))
    p2 = Process(target=lambda: worker_2.run(port=7002))
    p3 = Process(target=lambda: worker_3.run(port=7003))    
    p4 = Process(target=lambda: worker_4.run(port=7004))
    p5 = Process(target=lambda: worker_5.run(port=7005)) 
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
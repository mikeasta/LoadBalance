import time
from flask import Flask

worker_2 = Flask("Server #2")

@worker_2.route('/', methods=['GET'])
def ping():
    time.sleep(5)
    return "2"

if __name__ == "__main__":
    worker_2.run(port=7002)
import time
from flask import Flask

worker_1 = Flask("Server #1")

@worker_1.route('/', methods=['GET'])
def ping():
    time.sleep(5)
    return "1"

if __name__ == "__main__":
    worker_1.run(port=7001)
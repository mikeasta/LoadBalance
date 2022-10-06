import time
from flask import Flask

worker_5 = Flask("Server #5")

@worker_5.route('/', methods=['GET'])
def ping():
    time.sleep(5)
    return "5"

if __name__ == "__main__":
    worker_5.run(port=7005)
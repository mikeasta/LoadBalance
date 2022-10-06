import time
from flask import Flask

worker_3 = Flask("Server #3")

@worker_3.route('/', methods=['GET'])
def ping():
    time.sleep(5)
    return "3"

if __name__ == "__main__":
    worker_3.run(port=7003)
import time
from flask import Flask

worker_4 = Flask("Server #4")

@worker_4.route('/', methods=['GET'])
def ping():
    time.sleep(5)
    return "4"

if __name__ == "__main__":
    worker_4.run(port=7004)
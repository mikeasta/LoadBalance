import time
from flask import Flask
from multiprocessing import Process
from config import SERVER_AMOUNT, START_WORKER_PORT

# Variables
workers = []

# Initializes worker unit
def init_worker(index):
    worker = Flask(f'Server #{index}')

    @worker.route('/', methods=['GET'])
    def ping():
        time.sleep(5)
        return str(index) 
    
    return worker


# Creates defined number of workers
def create_workers(amount):
    for i in range(amount):
        workers.append(init_worker(i+1))


# Run all workers
def run_workers(start_port):
    procs = []
    for index, worker in enumerate(workers):
        server_port = start_port + index + 1
        process = Process(target=lambda: worker.run(port=server_port))
        process.start()
        procs.append(process)

    for p in procs:
        p.join()


# Script runner
def main():
    start_port = START_WORKER_PORT 
    amount = SERVER_AMOUNT 
    
    create_workers(amount)
    run_workers(start_port)


if __name__ == "__main__":
    main()
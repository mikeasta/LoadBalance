from workers.w_1 import worker_1
from workers.w_2 import worker_2
from workers.w_3 import worker_3
from workers.w_4 import worker_4
from workers.w_5 import worker_5

from multiprocessing import Process

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
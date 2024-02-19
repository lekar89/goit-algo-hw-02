from queue import Queue
from random import randrange
from collections import deque

class RequestsProcessor():
    q = Queue()    
    def generate_request(self):
        print("generate request")
        self.q.put(randrange(1000))

    def process_request(self):
        if not self.q.empty():
            print("process request")
            print(self.q.get())
        else :
          print("queue is empty")
            
def main():
    repr = RequestsProcessor()
    while True:
        repr.generate_request()
        repr.process_request()

if __name__ == "__main__":
    main()


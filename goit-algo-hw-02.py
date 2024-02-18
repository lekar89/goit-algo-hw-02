from queue import Queue
from random import randrange
from collections import deque

class RequestsProcessor():
    q = Queue()    
    def generate_request(self):
        self.q.put(randrange(1000))

    def process_request(self):
        if not self.q.empty():
            print(self.q.get())
        else :
          print("queue is empty")

def check_is_palindrome(text: str ):
    is_palindrome = True
    a = deque()
    for c in text.lower():
        if c.isalpha():
            a.append(c)
            # print(c)
            
    for i in range(len(a)// 2):
        if  a.pop() != a.popleft():
           is_palindrome = False 
    return is_palindrome
    
        
def main():
    repr = RequestsProcessor()
    while True:
        repr.generate_request()
        repr.process_request()

if __name__ == "__main__":
    main()


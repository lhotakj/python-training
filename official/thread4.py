import os

__spec__ = None
from multiprocessing import Process 
__spec__ = None
import time
def f():
  print(os.getpid(), ": zacatek...")
  time.sleep(os.getpid() % 7)
  print(os.getpid(), ": trvalo mi to", (os.getpid() % 7), "s.")

if __name__ == '__main__':
  for i in range(7):
    p = Process(target=f, args=())
    p.start()

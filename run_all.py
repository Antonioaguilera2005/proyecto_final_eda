from multiprocessing import Process
import os

def run_mercadona():
    os.system("python mercadona_api.py")

def run_carrefour():
    os.system("python carrefour_api.py")

def run_ldl():
    os.system("python ldl_api.py")

if __name__ == "__main__":
    p1 = Process(target=run_mercadona)
    p2 = Process(target=run_carrefour)
    p3 = Process(target=run_ldl)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

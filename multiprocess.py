
def fact(n):
    print(n)
    # Python code to demonstrate naive method 
    fact = 1
      
    for i in range(1,n+1): 
        fact = fact * i 
    print ("The factorial of {} is : ".format(n)) 
    #print("number  digit is:\n")

    #return len(str(results)) #such as sync
    return "number  digit is:\n"

import time
from multiprocessing import Pool
if __name__ == '__main__':
    tic=time.perf_counter()
    n=200000

    with Pool(7) as pool:
        print(pool.map(fact, [n]))
        #print(len(str(results)))??????
    toc=time.perf_counter()
    print(f"time calculate fact is:{toc-tic:0.4f} " )
            

def fact(n):
    # Python code to demonstrate naive method 
    fact = 1
      
    for i in range(1,n+1): 
        fact = fact * i 
    print ("The factorial of {} is : ".format(n)) 
    print("number  digit is:\n")
    
    #return (len(str(fact)))#such as sync
    return "number  digit is:\n"
from concurrent.futures import ThreadPoolExecutor
import time
n=200000

tic=time.perf_counter()
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=100) as executor:
        
        future=executor.map(fact,[n])
        #print(future)
        executor.shutdown()
toc=time.perf_counter()
print(f"time calculate fact is:{toc-tic:0.4f} " )

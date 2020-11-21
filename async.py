import asyncio
async def fact(n):
    # Python code to demonstrate naive method 
    fact = 1
      
    for i in range(1,n+1): 
        fact = fact * i 
    print ("The factorial of {} is : ".format(n)) 
    print("number  digit is:\n")
    
    #return (len(str(fact)))#such as sync
    return "number  digit is:\n"

import time
n=200000

tic=time.perf_counter()
loop=asyncio.get_event_loop()
try :
    
    loop.run_until_complete(fact(n))
except Exception as e:
    pass
finally:
    loop.stop()
    
toc=time.perf_counter()
print(f"time calculate fact is:{toc-tic:0.4f} " )

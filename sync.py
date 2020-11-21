'''
def fact(n):
    if(n==0 or n==1):
        return n
    else:
        return ( (n) *fact(n-1))
'''
def fact(n):
    # Python code to demonstrate naive method 
    fact = 1
      
    for i in range(1,n+1): 
        fact = fact * i 
    print ("The factorial of {} is : ".format(n)) 
    print("number  digit is:\n")
    
    #return (len(str(fact)))
    return "number  digit is:\n"
import time
tic=time.perf_counter()
n=200000

print(fact(n))
toc=time.perf_counter()
print(f"time calculate fact is:{toc-tic:0.4f} " )


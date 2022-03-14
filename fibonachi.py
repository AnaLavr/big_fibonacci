def fibo(n): 
    i=0
    if n<2:
        return(1)
    else:
        f=[0]*n 
        f[0]=1
        f[1]=1
        for i in range(2,n):
            f[i]=f[i-1]+f[i-2]
    return(f[i])

def big_fibonachi(n):
    counter='1'
    num=1
    while(len(counter)<n):
        counter=str(fibo(num))
        num+=1
    return(counter)

print(big_fibonachi(3))

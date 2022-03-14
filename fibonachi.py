def fibo(n): #вычислить n-ный элемент фибоначи
    i=0
    if n<2:
        return(1)
    else:
        f=[0]*n #задаем список длиной в n Элементов
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
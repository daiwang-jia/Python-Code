N=int(input())
def is_prime(num):
    a=0
    if num>2:
        for i in range(2,num):
            if num%i==0:
                a=0
                break
            else:
                a=1
    else:
        a=1
    return a
for k in range(2,N+1):
    if is_prime(k):
        print(k,end=" ")
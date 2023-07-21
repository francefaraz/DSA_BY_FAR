
# if n=4 , return 4+3+2+1+0, which is 10.
def rec_sum(n):
    if n==0:
        return 0
    return n+rec_sum(n-1)


print(rec_sum(4))



def sum_func(n):
    pass



print(sum_func(4321))
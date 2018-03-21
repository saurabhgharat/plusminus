import sys

def plusMinus(arr):
    def check_positivenumber(num):
         return num>0
    a=list(filter(check_positivenumber,arr))
    
    def check_negativenumber(num):
         return num<0
    b=list(filter(check_negativenumber,arr))
    
    def check_zero(num):
         return num==0    
    c=list(filter(check_zero,arr))
    
    print(float(len(a)/len(arr)))
    print(float(len(b)/len(arr)))
    print(float(len(c)/len(arr)))
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
    
    
import datetime
import math

def func1(func):
    def func2():
        time1 = datetime.datetime.now().microsecond
        print(time1)
        func()
        time2 = datetime.datetime.now().microsecond
        print(time2)
        print(time2 - time1)
    return func2

@func1
def print1():
    y=0
    for i in range(1000):
        y=y+1
    return


# if __name__ == '__main__':
#     print1()



# ---------------------------

MyDictionary={}
def cache(func):
    def wrapper(*args):
        if(((int)(*args)) in MyDictionary):
            print (MyDictionary[(int)(*args)])
            print("yes")
        else:
            y=func(*args)
            print(y)
            MyDictionary[(int)(*args)] = y
    return wrapper

@cache
def print1(y):
    return y*y*y*y*y*y*y*y*y*y*y*y

if __name__ == '__main__':
    print1(2)
    print1(12)
    print1(22)
    print1(2)
    print1(45)
    print1(2)
    print1(12)

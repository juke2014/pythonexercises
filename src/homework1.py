Chapter 1 



def if_function(condition, true_result, false_result):
    return true_result if condition else false_result
print if_function(3==2, 3+2, 3-2)


def findMax(a, b, c):
    return max(a, b, c)
print findMax(1, -3, -4)    

def findSqr(a, b, c):
    return pow(max(a, b, c), 2)
    
print findSqr(1, 2, 3)  


def findMiddle(a, b, c):
    return (pow(a + b + c - max(a, b, c) - min(a, b, c), 2) + 
        pow(max(a, b, c), 2))
print findMiddle(1, -1, 3)   


def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result 

def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

x = 1
def c():
   return False

def t():
    global x
    x = 2
    return 1
   
def f():
   global x    
   return x

print x

print with_if_function()
print x
print with_if_statement()


Question 4
Douglas Hofstadter’s Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.
Pick a positive integer n as the start.
If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1.
Continue this process until n is 1.

def hailstone(n):
        count = 1
        print 'Current variable value :', n
        while n > 1:
            count = count + 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = n * 3 + 1
            print 'Current variable value :', n
        return count        
        
           
print hailstone(10)           


def nextNumber(n):
    if n % 2 == 0:
        return n/2
    else:
        return n * 3 + 1
        
#print nextNumber(13)

def h(n):
    count = 1
    while n > 1:
        print n
        count += 1
        n = nextNumber(n)
    print n
    return count
            
#print("length:", h(6))       
       


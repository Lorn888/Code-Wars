# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

# Your function will be tested with pre-made examples as well as random ones.

# If you can, try writing it in one line of code.

a=[3,2,6]
b=[1,4,4]

def find_difference(a,b):
    x = a[0]*a[1]*a[2]
    y = b[0]*b[1]*b[2]

    if x > y:
        return x - y
    else:
        return y - x
    
    # Your code here!
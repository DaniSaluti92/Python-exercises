def fizzbuzz(x):

    a=x%3
    b=x%5

    if (a==0) and (b!=0):
        return "Fizz"
    elif (a!=0) and (b==0):
        return "Buzz"
    elif (a==0) and (b==0):
        return "FizzBuzz"
    else:
        return (x)
    

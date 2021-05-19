#to perform operation to largest value
#
def avoid_zero(func):
    def wrapper(num1,num2):
        if num1==0 or num2 == 0:
         raise Exception("Zero division not possible")
        return func(num1,num2)
    return wrapper

def revert_values(func):
    def wrapper(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
        return func(num1,num2)
    return wrapper


@revert_values
def sub(num1,num2):
    return num1-num2
@revert_values
@avoid_zero
def div(num1,num2):
    return num1/num2



print(sub(4,24))
print(div(0,10))
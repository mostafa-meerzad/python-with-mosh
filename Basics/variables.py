message = "global message"  # a global variable


def greet():
    # accessing global message variable before making it a local variable
    print(message)  # message still shows global value 'global message'

    # if you assign global variable another value in this function block
    # like so
    message = "new message"
    # python will create another local variable with the same name 'message' and assign it the new value
    # doing so as no effect on the global value

    print(message)  # message is now a local variable and has 'new message'


print(message)  # message is 'global message'

def sayHi():
    # block level variables are accessible throughout the function
    # message = "Hello" # function level variable


    # if you need to change the value of a global variable here is how
    global message
    message = "Hello global" # function level variable

    if True:
        print(message)
        other = "CONDITIONAL" # var defined inside code-block

    for x in [1,2]:
        # print("x value ", x)
        print(x, " ", message)
        another = "LOOP" # var defined inside loop body

    print("var defined in conditional statement ", other)
    print("var defined in loop ", another)
    print("var defined in function ", message)

sayHi()
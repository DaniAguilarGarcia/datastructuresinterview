
#everything inside the () are the arguments to the function
#parameters:  what you can pass to a function, when you actually use it and pass it values are arguments 
print(*objects, sep=' ', end='/n', file=sis.stdout, flush=False)

# *objects= function can take any number of objects
# sep - short for separator, single blank space
# end default /n -> new line

print("hello, ", end="" ) #there is no new line after it ends

name = input("What's your name? ")
name = name.strip() # removes whitespace from str
name = name.capitalize() 
name = name.title() #capitalizes every word
#or we can combine
name = name.strip().title()
# or
name = input("What's your name? ").strip().title()
print(f'hello, {name}')


# f string or format string, re format to string

#interactive code - on terminal, doesnt safe, type python to start >>>


#1:03:48 min

#float, can take more than just integers
# [] in argument documentation is optional

def #invent your own function, defince function

def hello(to): ##function is being design to take a parameter
    #meaning of the function
    print("Hello,", to)

name = input("What's your name?")
hello(name) #passing the input as an argument, thats whats being pass into hello


def main():
    name = input("What's your name?")
    hello(name)

def hello(to="World"):   
    print("Hello,", to)

main()


return 


def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))
def square(n):
    return n * n
main()


def main():
    x = int(input("What is x?"))
    print("x square is", square(x))

def square(n):
    return pow(n, 2)
main()



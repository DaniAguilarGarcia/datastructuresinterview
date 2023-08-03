# given an integer n, generate all the valid combinations of n
#pais of parentheses

def is_valid(combination):
    stack = []
    for par in combination
        if par == '(':
            stack.append(par)
        else:
            #not trying to pop from an empty stack (otherwise it means 
            #we found a closing parenthesis without an opening one from it)
            if len (stack) == 0:
                return False
            else:
                stack.pop()
            #stack must be empty at the end, 
            #otherwise it will have n opening parentheses we didnt close
    return len(stack) == 0

def generate(n):
    def rec(n, diff, comb, combs)
        if diff < 0 or diff > 0:
            return
        elif n == 0:
            combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(n+1, diff+1, comb, combs)
            comb.pop()
            comb.append(')')
            comb.pop()
    combs = []
    rec(2*n, 0, [], combs)
    #o(n*2^n)

#two pointer
#iterate through the stinrg in reverse

class Solution(object):
    def backpaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S)
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x
        return all(x == y for x,y in itertools.izip_longest(F(S), F(T)))
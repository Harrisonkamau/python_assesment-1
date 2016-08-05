# Write a function that return whether or not the input string has balanced parantheses
# Balanced:
#   '((()))'
#   '(()())'
# Not balanced:
#   '((()'
#   '())('


braces = {'(': ')', '[': ']', '{': '}'}


def paren_matcher(string_symbol):
    stack = []
    for bracket in string_symbol:
        c = braces.get(bracket)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != bracket:
            return False
    return not stack

print paren_matcher('((()))')
print paren_matcher('[[][[')






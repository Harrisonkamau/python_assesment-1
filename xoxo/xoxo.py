# Using Python, have the function xoxo(str) take the str parameter
# being passed and return the string true if there is an equal number of x's and o's,
# because you cannot recieve an uneven number of hugs and kisses :-)
# otherwise return the string false. Only these two letters will be entered in the string,
# no punctuation or numbers.
# For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.


def xoxo(string):
    count_o = string.count('o')  # count the number of o's
    cont_x = string.count('x')  # count the number of x's
    if cont_x == count_o:  # if the number of x's equals the number of o's, return True, else False
        return True
    return False


print xoxo('xxxxxooooo')
print xoxo('xxooo')
print xoxo('xxooxxooxxxxo')





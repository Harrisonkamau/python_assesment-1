import random

# define the key for generating passwords
key_ = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# define passwords length
pass_len = 10

# generate password randomly
password = "".join(random.sample(key_, pass_len))
print password

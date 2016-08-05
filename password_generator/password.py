import random

key_ = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pass_len = 10

password = "".join(random.sample(key_, pass_len))
print password

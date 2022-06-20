import string
import random
N = 7
for ind in range(5):
    res = ''.join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase+string.punctuation, k = N))
    print(str(res))

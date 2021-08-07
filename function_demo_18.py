# function_demo_18.py


def get_int():
    i = 0
    while True:
        yield i

        i += 1

gen1 = get_int()

gen2 = get_int()


def get_limited(limit):
    i = 0
    while i <= limit:
        yield i         #keyword makes this function be a generator

        i += 1
for i in get_limited(10):
    print(i)

"""we should run as a loop because the value of the i is incresing"""
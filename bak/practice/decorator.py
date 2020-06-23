import time


def deco(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("This time is %s" % (stop_time - start_time))

    return wrapper


@deco  # test1=deco(test1)
def test1():
    time.sleep(3)
    print("___________index_____________")


# test1 = deco(test1)
test1()

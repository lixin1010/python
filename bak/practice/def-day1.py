import time


def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)

    with open('a.txt', 'a+') as f:
        f.write('%s end action\n' % time_current)
        time.sleep(1)


def test1():
    logger()


def test2():
    logger()


def test3():
    logger()


test1()
test2()
test3()

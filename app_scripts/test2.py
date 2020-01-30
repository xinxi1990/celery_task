
from .. import app
import time


count = 0



def test33():
    time.sleep(1)
    print('test33')


def test44():
    time.sleep(1)
    print('test44')
    test33()


@app.task
def test2_run():
    # test33()
    # test44()
    global count
    count = count + 1

    print("######### hello world {0} #########".format(count))
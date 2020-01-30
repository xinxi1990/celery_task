
from .. import app
import time


def test11():
    time.sleep(1)
    print('test11')


def test22():
    time.sleep(2)
    print('test22')
    test11()


@app.task
def test1_run():
    test11()
    test22()
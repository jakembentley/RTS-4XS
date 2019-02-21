from rts4xs_objects import Countable

def assertIncrementCountable(c):
    e = c.getElement()
    c.increment(v = 1)
    assert c.getElement() > e
    return

def main():
    #actual body of tests
    item = Countable(e = 0)
    assertIncrementCountable(item)
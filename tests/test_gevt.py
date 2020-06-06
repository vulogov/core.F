import sys
import os
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *

def answer(ns, *args, **kw):
    ns.V("/tmp/answer", 42)

def killer(ns):
    f = lf(ns)
    while True:
        ns.V("/tmp/answer", 42)
        time.sleep(1)
        f("/sbin/killall")()

def killer5(*args):
    f = lf(args[0])
    c = 0
    while True:
        c += 1
        time.sleep(1)
        if c > 5:
            break
    f("/sbin/killall")()

def test_gevt_1():
    ns, f, F = NS()
    f("spawn")("answer", answer)
    f("/bin/loop")()
    assert ns.V("/tmp/answer") == Just(42)

def test_gevt_2():
    ns, f, F = NS()
    f("spawn")("killer", killer)
    f("/bin/loop")()
    assert ns.V("/tmp/answer") == Just(42)

def test_gevt_3():
    ns, f, F = NS()
    f("schedule")(1, "42", answer)
    f("spawn")("killer", killer5)
    f("/sbin/loop")()
    assert ns.V("/tmp/answer") == Just(42)

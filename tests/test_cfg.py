import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *

def test_cfg_1():
    ns, f, F = NS()
    F("C", "[/home> answer <- 42 ;;")
    assert ns.V("/home/answer") == Just(42)

def test_cfg_2():
    ns, f, F = NS()
    F("C", "[/home> answer <- [42,1] ;;")
    assert ns.V("/home/answer").value[0] == 42

def test_cfg_3():
    ns, f, F = NS()
    F("C", '[/home> answer <- { "answer":42, "pi": 3.13} ;;')
    assert ns.V("/home/answer").value["answer"] == 42

def test_cfg_4():
    ns, f, F = NS()
    F("Cfg", "test.cfg")
    assert ns.V('/home/NotAnswer') == Just(41)

def test_cfg_4_1():
    ns, f, F = NS()
    F("Cfg", "test.yaml")
    assert ns.V('/home/NotAnswer') == Just(41)

def test_cfg_5():
    ns, f, F = NS()
    F("C", '("test.cfg">')
    assert ns.V('/home/NotAnswer') == Just(41)

def test_cfg_6():
    ns, f, F = NS()
    F("C", '[/home> Message <- "Hello World!" ;;')
    assert ns.V("/home/Message") == Just("Hello World!")

def test_cfg_7():
    ns, f, F = NS()
    F("C", """[ /home >
    {
        Answer:42,
        "vfs.fs.disk[]" : "u"
    } -> Dict ;;""")
    assert len(ns.V('/home/Dict').value) == 2

def test_cfg_8():
    ns, f, F = NS()
    F("C", '[ /home > Answer <- ( 41 1 + ) ;;')

def test_cfg_9():
    ns, f, F = NS()
    F("C", '~ += === =**= ~+ ~- ~*')

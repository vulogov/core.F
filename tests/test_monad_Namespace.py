import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from oslash import *
from coref import *
from coref.internal.monad import *
from coref.internal.util import partial

def Doubler(ns, path):
    return ns.V(path).value * 2

def test_monad_Namespace_1():
    d = Namespace()
    assert d.null() == False

def test_monad_Namespace_2():
    d = Namespace()
    d.V('/answer', Just(42))
    assert d.V('/answer') == Just(42)

def test_monad_Namespace_2_1():
    d1, d2 = Namespace(), Namespace()
    d1.V('/home/answer', Just(42))
    d2.V('/home/pi', Just(3.14))
    d1.update(d2)
    assert d1.V('/home/pi') == Just(3.14)

def test_monad_Namespace_3():
    d = Namespace()
    assert d.V('/answer') == Nothing()

def test_monad_Namespace_4():
    d = Namespace()
    assert d.Name() == Just("/")

def test_monad_Namespace_5():
    d = Namespace()
    assert d.isDir() == TRUE

def test_monad_Namespace_6():
    d = Namespace()
    d.V('/home/answer', Just(42))
    home = d.cd('/home')
    assert home.Name() == Just("/home")

def test_monad_Namespace_7():
    d = Namespace()
    d.V('/home/answer', Just(42))
    home = d.cd('/home')
    assert home.V("/answer") == Just(42)

def test_monad_Namespace_8():
    d = Namespace()
    home = d.mkdir('/home')
    home = home + Values(answer = 42)
    home.C()
    assert d.V("/home/answer") == Just(42)

def test_monad_Namespace_8_1():
    d = Namespace()
    home = d.mkdir('/home')
    C(home + Values(answer = 42))
    assert d.V("/home/answer") == Just(42)

def test_monad_Namespace_9():
    d = Namespace()
    d.V("/bin/doubler", Doubler)
    d.V("/home/answer", Just(21))
    assert d.V("/bin/doubler") == Just(Doubler)

def test_monad_Namespace_10():
    d = Namespace()
    d.V("/bin/doubler", Doubler)
    d.V("/home/answer", Just(21))
    f = d.V("/bin/doubler").value
    assert f(d, "/home/answer") == 42

def test_monad_Namespace_11():
    d = Namespace()
    d.V("/bin/doubler", partial(Doubler, d))
    d.V("/home/answer", Just(21))
    f = d.V("/bin/doubler").value
    assert f("/home/answer") == 42

def test_monad_Namespace_12():
    d = Namespace()
    assert d.f("/bin/doubler")() == Nothing()

def test_monad_Namespace_13():
    d = Namespace()
    d.V("/bin/doubler", partial(Doubler, d))
    d.V("/home/answer", Just(21))
    assert d.f("doubler")("/home/answer") == 42

def test_monad_Namespace_14():
    d = Namespace()
    d.V('/home/answer', Just(42))
    dir = d.ls("/home", type=(int))
    assert dir.head() == Just(42)

def test_monad_Namespace_15():
    d = Namespace()
    d.stor.mount('home', ':mem:', ['/home/*'])
    d.V('/home/answer', Just(42))
    assert d.V("/home/answer") == Just(42)

def test_monad_Namespace_16():
    d = Namespace()
    d.V('/home/values', [])
    d.V('/home/values').value.append(42)
    assert d.V('/home/values').value[0] == 42

def test_monad_Namespace_17():
    def _divide(ns, x,y):
        return x/y
    d = Namespace()
    nsImport(d, 'coref.stdlib')
    d.V("/bin/divide", partial(_divide, d))
    assert d.F("/bin/divide", 4, 2) == Right(2)

def test_monad_Namespace_18():
    def _divide(ns, x,y):
        return x/y
    ns = Namespace()
    nsImport(ns, 'coref.stdlib')
    ns.V("/bin/divide", partial(_divide, ns))
    v = ns.F("/bin/divide", 4, 0)
    assert  isinstance(v, Left) == True

def test_monad_Namespace_19():
    def _divide(ns, x,y):
        return x/y
    ns = Namespace()
    nsImport(ns, 'coref.stdlib')
    ns.V("/bin/divide", partial(_divide, ns))
    v = ns.F("/bin/divide", 4, 0)
    assert len(ns.V('/sys/traceback/tb').value) == 1

def test_monad_Namespace_20():
    def _divide(ns, x,y):
        return x/y
    ns = Namespace()
    nsImport(ns, 'coref.stdlib')
    ns.V("/bin/divide", partial(_divide, ns))
    v = ns.F("/bin/divide", 4, 2)
    fv = ns.V('/sys/traceback/ftrace').value.pop()
    assert fv.fun == '/bin/divide'

def test_monad_Namespace_21():
    ns, f, F = NS()
    F("V", "/home/answer", 42)
    assert isinstance(F("V", "/home/answer"), Right)

def test_monad_Namespace_21():
    ns, f, F = NS()
    F("V", "/home/answer", 42)
    assert F("V", "/home/answer").value == Just(42)

def test_monad_Namespace_22():
    ns, f, F = NS()
    f = lf(ns)
    assert type(f("/bin/time")()) == float

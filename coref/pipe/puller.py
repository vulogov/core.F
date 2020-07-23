import gevent.time
import zmq.green as zmq
from .loop import *
from coref import *
from coref.gevent import nsSpawn
from gevent.queue import Queue

def nsPullerCreate(ns, name, *addr):
    path = f"/dev/pipe/pull/{name}"
    p_name = f"pipe:pull:{name}"
    _dir = ns.V(path)
    if isNothing(_dir) is False:
        return _dir
    ns.V(f"{path}/in", Queue())
    ns.V(f"{path}/name", name)
    ns.V(f"{path}/callbacks", {})
    ns.V(f"{path}/continue", True)
    nsSpawn(ns, p_name, _recv_loop, ns, path, zmq.PULL, *addr)

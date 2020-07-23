import gevent.time
import zmq.green as zmq
from coref import *
from coref.gevent import nsSpawn
from gevent.queue import Queue

def nsPusherCreate(ns, name, *addr):
    def _loop(ns, path, *addr):
        _in = ns.V(f"{path}/in").value
        _name = ns.V(f"{path}/name").value
        _cb = ns.V(f"{path}/callbacks").value
        ctx = zmq.Context()
        socket = ctx.socket(zmq.PUSH)
        for a in addr:
            socket.connect(a)
        poller = zmq.Poller()
        poller.register(socket, zmq.POLLIN)
        while ns.V(f"{path}/continue").value:
            while len(_in) > 0:
                gevent.time.sleep(0)
                data = _in.get()
                for fun_name in _cb:
                    gevent.time.sleep(0)
                    data = _cb[fun_name](ns, path, data)
                socket.send_multipart([
                    bytes(_name, "utf-8"),
                    data
                ], copy=False)
            gevent.time.sleep(0.5)
        ctx.term()


    path = f"/dev/pipe/push/{name}"
    p_name = f"pipe:push:{name}"
    _dir = ns.V(path)
    if isNothing(_dir) is False:
        return _dir
    ns.V(f"{path}/in", Queue())
    ns.V(f"{path}/name", name)
    ns.V(f"{path}/callbacks", {})
    ns.V(f"{path}/continue", True)
    nsSpawn(ns, p_name, _loop, ns, path, *addr)

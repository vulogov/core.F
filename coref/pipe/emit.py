import gevent.time
import zmq.green as zmq
from coref import *
from coref.gevent import nsSpawn
from gevent.queue import Queue

def nsEmitCreate(ns, name, addr, *cb):
    def _loop(ns, path, addr, cb):
        _out = ns.V(f"{path}/out").value
        _name = ns.V(f"{path}/name").value
        ctx = zmq.Context()
        socket = ctx.socket(zmq.PUB)
        socket.bind(addr)
        while True:
            while len(_out) > 0:
                data = _out.get()
                for fun in cb:
                    data = fun(ns, data)
                socket.send_multipart([
                    bytes(_name, "utf-8"),
                    data
                ], copy=False)
            gevent.time.sleep(0.5)


    path = f"/dev/pipe/emitter/{name}"
    p_name = f"pipe:emitter:{name}"
    _dir = ns.V(path)
    if isNothing(_dir) is False:
        return _dir
    ns.mkdir(path)
    ns.V(f"{path}/out", Queue())
    ns.V(f"{path}/name", name)
    nsSpawn(ns, p_name, _loop, ns, path, addr, cb)

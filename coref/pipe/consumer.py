import gevent.time
import zmq.green as zmq
from coref import *
from coref.gevent import nsSpawn
from gevent.queue import Queue

def nsConsumerCreate(ns, name, *addr):
    def _loop(ns, path, *addr):
        _in = ns.V(f"{path}/in").value
        _name = ns.V(f"{path}/name").value
        _cb = ns.V(f"{path}/callbacks").value
        ctx = zmq.Context()
        socket = ctx.socket(zmq.SUB)
        for a in addr:
            socket.connect(a)
        poller = zmq.Poller()
        poller.register(socket, zmq.POLLIN)
        socket.subscribe(bytes(_name, "utf-8"))
        while ns.V(f"{path}/continue").value:
            while True:
                gevent.time.sleep(0)
                s = dict(poller.poll(1.0))
                if socket in s and s[socket] == zmq.POLLIN:
                    data = socket.recv_multipart()
                    for fun_name in _cb:
                        gevent.time.sleep(0)
                        data = _cb[fun_name](ns, path, data)
                    _in.put(data)
                else:
                    break
            gevent.time.sleep(0.5)
        ctx.term()


    path = f"/dev/pipe/consumer/{name}"
    p_name = f"pipe:consumer:{name}"
    _dir = ns.V(path)
    if isNothing(_dir) is False:
        return _dir
    ns.V(f"{path}/in", Queue())
    ns.V(f"{path}/name", name)
    ns.V(f"{path}/callbacks", {})
    ns.V(f"{path}/continue", True)
    nsSpawn(ns, p_name, _loop, ns, path, *addr)

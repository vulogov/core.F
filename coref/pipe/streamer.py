import gevent.time
import zmq.green as zmq
from .device import *
from coref import *
from coref.gevent import nsSpawn
from gevent.queue import Queue

def nsStreamerCreate(ns, name, fe_addr, be_addr, *_cb):
    path = f"/dev/pipe/streamer/{name}"
    p_name = f"pipe:streamer:{name}"
    _dir = ns.V(path)
    if isNothing(_dir) is False:
        return _dir
    ns.V(f"{path}/name", name)
    ns.V(f"{path}/fe_addr", fe_addr)
    ns.V(f"{path}/be_addr", be_addr)
    # dev_type, fe_addr, fe_type, be_addr, be_type, *_cb
    nsSpawn(ns, p_name, pipeDevice, path, zmq.STREAMER, fe_addr, zmq.PULL, be_addr, zmq.PUSH, *_cb)

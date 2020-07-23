def _recv_loop(ns, path, sock_type, *addr):
    _in = ns.V(f"{path}/in").value
    _name = ns.V(f"{path}/name").value
    _cb = ns.V(f"{path}/callbacks").value
    ctx = zmq.Context()
    socket = ctx.socket(sock_type)
    for a in addr:
        socket.connect(a)
    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)
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

def _send_loop(ns, path, sock_type, *addr):
    _in = ns.V(f"{path}/in").value
    _name = ns.V(f"{path}/name").value
    _cb = ns.V(f"{path}/callbacks").value
    ctx = zmq.Context()
    socket = ctx.socket(sock_type)
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

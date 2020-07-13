import uuid
from coref import *
from .gevent import nsSpawn
from gevent.server import StreamServer
from gevent.queue import Queue

def nsTcpLoop(ns, server):
    server.serve_forever()

def nsTcpCreate(ns, listen, port, callback):
    def _callback(ns, path, callback, _socket, _addr):
        def recvall(sock):
            BUFF_SIZE = 4096 # 4 KiB
            data = b''
            while True:
                part = sock.recv(BUFF_SIZE)
                data += part
                if len(part) < BUFF_SIZE:
                    break
            return data
        _id = str(uuid.uuid4())
        cpath = f"{path}/{_id}"
        ns.mkdir(cpath)
        ns.V(f"{cpath}/in", Queue)
        ns.V(f"{cpath}/out", Queue)
        print("AAA")
        while callback(ns, cpath, _socket, _addr):
            print("BBB")
            while len(ns.V(f"{cpath}/out").value) > 0:
                data = ns.V(f"{cpath}/out").value.get()
                _socket.sendall(data)
                data = recvall(_socket)
                ns.V(f"{cpath}/in").value.put(data)


    path = f"/dev/tcp/server/{listen}/{port}"
    if ns.V(f"{path}/serverInitialized") == TRUE:
        return FALSE
    ns.mkdir(path)
    ns.V(f"{path}/callback", callback)
    ns.V(f"{path}/serverInitialized", True)

    server = StreamServer((listen, port), partial(_callback, ns, path, callback))
    server.start()
    nsSpawn(ns, path, nsTcpLoop, ns, server)
    return TRUE

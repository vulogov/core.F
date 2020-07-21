import uuid
from coref import *
from .gevent import nsSpawn
from gevent.server import StreamServer
from gevent.select import select
from gevent.queue import Queue

def nsTcpLoop(ns, server):
    server.serve_forever()

def nsTcpCreate(ns, listen, port, callback):
    class CoreTcpServer(StreamServer):
        def do_close(self, sock, *args):
            StreamServer.do_close(self, sock, *args)
    def _close(ns, path):
        ns.rmdir(path)
        return
    def _callback(ns, path, callback, _socket, _addr):
        def recvall(sock, buf_size, tmout):
            BUFF_SIZE = buf_size
            data = b''
            while True:
                try:
                    _r, _w, _x = select([sock.fileno()], [], [], tmout)
                except ValueError:
                    break
                if len(_r) == 0:
                    break
                part = sock.recv(BUFF_SIZE)
                if len(part) == 0:
                    break
                data += part
                if len(part) < BUFF_SIZE:
                    break
            return data
        _id = str(uuid.uuid4())
        cpath = f"{path}/{_id}"
        ns.mkdir(cpath)
        ns.V(f"{cpath}/in", Queue())
        ns.V(f"{cpath}/out", Queue())
        idle = ns.V(f"{path}/idleLoops").value
        tmout = ns.V(f"{path}/waitForData").value
        buf_size = ns.V("/etc/tcpBufSize").value
        try:
            _r, _w, _x = select([_socket.fileno()], [], [], tmout)
        except ValueError:
            _close(ns, cpath)
            return
        if len(_r) > 0:
            data = recvall(_socket, buf_size, tmout)
            if len(data) == 0:
                _close(ns, cpath)
                return
            ns.V(f"{cpath}/in").value.put(data)
        c = 0
        while callback(ns, cpath, _socket, _addr) or c < idle:
            while len(ns.V(f"{cpath}/out").value) > 0:
                data = ns.V(f"{cpath}/out").value.get()
                _socket.sendall(data)
            try:
                _r, _w, _x = select([_socket.fileno()], [], [], tmout)
            except:
                _close(ns, path)
                break
            if len(_r) > 0:
                data = recvall(_socket, buf_size, tmout)
                if len(data) == 0:
                    break
                ns.V(f"{cpath}/in").value.put(data)
                c = 0
            else:
                c += 1
                #print(c,idle)
        _close(ns, cpath)


    path = f"/dev/tcp/server/{listen}/{port}"
    if ns.V(f"{path}/serverInitialized") == TRUE:
        return FALSE
    ns.mkdir(path)
    ns.V(f"{path}/callback", callback)
    ns.V(f"{path}/serverInitialized", True)
    ns.V(f"{path}/waitForData", 3)
    ns.V(f"{path}/idleLoops", 10)
    server = CoreTcpServer((listen, port), partial(_callback, ns, path, callback))
    server.start()
    nsSpawn(ns, path, nsTcpLoop, ns, server)
    return TRUE

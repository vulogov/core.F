import gevent.time
import zmq.green as zmq

def pipeDevice(ns, path, dev_type, fe_addr, fe_type, be_addr, be_type, *_cb):
    try:
        context = zmq.Context(1)
        frontend = context.socket(fe_type)
        frontend.bind(fe_addr)
        backend = context.socket(be_type)
        backend.bind(be_addr)
        for c in _cb:
            c(ns, path, context, frontend, backend)
        zmq.device(dev_type, frontend, backend)
    except Exception as e:
        print(e)
        ns.F("/bin/registerException")
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()

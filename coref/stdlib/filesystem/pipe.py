from coref.mod import nsValues, nsList
from coref.pipe.emit import nsEmitCreate
from coref.pipe.consumer import nsConsumerCreate

def pipeRegisterCallback(ns, path, name, fun):
    _cb = ns.V(f"{path}/callbacks").value
    if _cb is None:
        return False
    if name in _cb:
        return True
    _cb[name] = fun
    return True

_lib = {
    '/bin/pipeEmitter': nsEmitCreate,
    '/bin/pipeConsumer': nsConsumerCreate,
    '/bin/pipePush': nsPusherCreate,
    '/bin/pipePull': nsPullerCreate,
    '/bin/pipeStreamer': nsStreamerCreate,
    '/bin/pipeRegisterCallback': pipeRegisterCallback,
}

_mkdir = [
    '/dev/pipe',
    '/dev/pipe/emitter',
    '/dev/pipe/consumer',
    '/dev/pipe/push',
    '/dev/pipe/pull',
    '/dev/pipe/streamer',
]

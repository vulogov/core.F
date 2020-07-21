from coref.mod import nsValues, nsList
from coref.pipe.emit import nsEmitCreate

_lib = {
    '/bin/pipeEmitter': nsEmitCreate
}

_mkdir = [
    '/dev/pipe',
    '/dev/pipe/emitter',
]

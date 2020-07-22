from coref.mod import nsValues, nsList
from coref.pipe.emit import nsEmitCreate
from coref.pipe.consumer import nsConsumerCreate


_lib = {
    '/bin/pipeEmitter': nsEmitCreate,
    '/bin/pipeConsumer': nsConsumerCreate,
}

_mkdir = [
    '/dev/pipe',
    '/dev/pipe/emitter',
    '/dev/pipe/consumer',
]

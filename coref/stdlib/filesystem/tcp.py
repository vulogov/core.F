from coref.mod import nsValues, nsList
from coref.tcpserver import nsTcpCreate

_set = nsValues(
    {
        '/etc/tcpBufSize': 512,
    }
)

_lib = {
    '/bin/tcpServer': nsTcpCreate
}

_mkdir = [
    '/dev/tcp',
    '/dev/tcp/server',
]

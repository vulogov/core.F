from coref.mod import nsValues, nsList

_set = nsValues(
    {
        '/etc/library': [],
        '/config/user.library': [],
        '/etc/answer': 42,
        '/config/var.redefine': True,
        '/etc/daemonize': False,
        '/etc/flags/truename': False,
        '/sys/hylang.enabled': False,
        '/config/cfg.files': [],
    }
)

_mkdir = [
    '/bin',
    '/home',
    '/tmp',
    '/etc',
    '/config',
    '/sys',
    '/usr',
    '/usr/local',
    '/usr/local/bin',
    '/proc',
    '/dev',
    '/templates',
    '/etc/corens',
]

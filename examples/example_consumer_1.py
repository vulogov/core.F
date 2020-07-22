import sys
import os
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *

def appconfig(ns):
    print("Application config")

def pull(ns):
    q = ns.V("/dev/pipe/consumer/test/in").value
    while True:
        while len(q) > 0:
            data = q.get()
            print(data)
        time.sleep(0)

ns, f, F = NS()
F("/bin/initAppRegister", appconfig, level=1, action='start')
F("/bin/pipeConsumer", "test", "tcp://127.0.0.1:60000")
F("/bin/spawn", "puller", pull)
F("/bin/main")
F("/usr/local/bin/daemon")
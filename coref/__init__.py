from gevent import monkey
monkey.patch_all()
import gevent

from oslash import Monad, Just, Nothing
from coref.internal.monad import *
from coref.internal.monad.internal import *
from coref.ns import *
from coref.mod import *
from coref.internal.util import partial

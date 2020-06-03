from oslash import Just
from coref.mod import nsValues, nsList
from coref.internal.monad.Namespace import C, f, F


_lib = nsValues(
    {
        '/bin/F': F,
        '/bin/f': f,
        '/bin/C': C,
    }
)

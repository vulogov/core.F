from oslash import Just
from coref.mod import nsValues, nsList
from coref.init import nsInitRegister


_lib = nsValues(
    {
        '/bin/initRegister': nsInitRegister,
    }
)

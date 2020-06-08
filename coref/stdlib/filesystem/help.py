from coref.mod import nsValues, nsList

_set = nsValues(
    {
        '/help/cmd/default': """
# THE HELP
This is a default HELP page for the core.F application command-line.

## BASICS OF core.F CLI interface
    core.F CLI interface consists of two parts: Setting the global flags and
calling for the pre-configured *commands*. You do have a help, available to you
within context when you will specify __--help__ after the command.

### Setting of the global flags

### Calling preconfigured commands

Keep exploring ! 73 !
        """,
    }
)

_mkdir = [
    '/help',
    '/help/cmd',
]

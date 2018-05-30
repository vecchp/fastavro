PRIMITIVES = set([
    'boolean',
    'bytes',
    'double',
    'float',
    'int',
    'long',
    'null',
    'string',
])

SCHEMA_DEFS = {
    'boolean': 'boolean',
    'bytes': 'bytes',
    'double': 'double',
    'float': 'float',
    'int': 'int',
    'long': 'long',
    'null': 'null',
    'string': 'string',
}

CACHED_SCHEMAS = {
    'READERS': set(),
    'WRITERS': set(),
}


class UnknownType(ValueError):
    def __init__(self, name):
        super(UnknownType, self).__init__(name)
        self.name = name

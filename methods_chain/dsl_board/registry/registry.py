

registry = {}


def register_class(klass):
    registry[klass.__name__] = klass


def from_registry(name):
    return registry.get(name, None)


class ComputerComponent(object):

    field_names = ()

    def __eq__(self, other):
        objs = [(self, other)]
        return all(all(getattr(s, name) == getattr(o, name) for (s, o) in objs) for name in self.field_names)


class Computer(ComputerComponent):

    field_names = ('processor', 'discs')

    def __init__(self):
        self.processor = None
        self.discs = []

    def add_disc(self, disc):
        self.discs.append(disc)

    def add_processor(self, processor):
        self.processor = processor

    @classmethod
    def from_dict(cls, dict_):
        result = Computer()

        processor = Processor.from_dict(dict_.get('processor', {}))
        result.add_processor(processor)

        discs = [Disk.from_dict(d) for d in dict_.get('discs', [])]
        for d in discs:
            result.add_disc(d)

        return result


class Processor(ComputerComponent):

    field_names = ('cores', 'speed', 'type')

    def __init__(self, cores, speed, type):
        self.cores = cores
        self.speed = speed
        self.type = type

    @classmethod
    def from_dict(cls, dict_):
        cores = dict_.get('cores', 0)
        speed = dict_.get('speed', 0)
        type = dict_.get('type', '')
        result = Processor(cores, speed, type)
        return result


class Disk(ComputerComponent):

    field_names = ('size', 'speed', 'serial')

    def __init__(self, size=0, speed=0, serial=''):
        self.size = size
        self.speed = speed
        self.serial = serial

    @classmethod
    def from_dict(cls, dict_):
        size = dict_.get('size', 0)
        speed = dict_.get('speed', 0)
        serial = dict_.get('serial', '')
        result = Disk(size, speed, serial)
        return result

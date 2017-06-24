from examples.function_sequence.computer_model import Computer, Processor, Disk


class ComputerBuilder:
    """ Construction builder for Computer """

    def __init__(self):
        self.computer = Computer()

    def build(self):
        return self.computer

    def add_processor(self, cores, speed, type):
        self.computer.add_processor(Processor(cores, speed, type))

    def add_disk(self, size=0, speed=0, serial=''):
        self.computer.add_disc(Disk(size, speed, serial))

    def from_dict(self, dict_):
        self.computer = Computer.from_dict(dict_)
        return self.computer

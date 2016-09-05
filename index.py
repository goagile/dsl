class AbstractEvent:

	def __init__(self, name, code):
		self.name = name
		self.code = code

class Command(AbstractEvent):
	pass

class Event(AbstractEvent):
	pass

# ------------------------------------------

class State:

	def __init__(self, name):
		self.name = name
		actions = []
		transitions = {}

	def add_transition(event, target_state):
		assert null != target_state
		transitions[event.code] = Transition(self, event, target_state)


class Transition:

	def __init__(source, trigger, target):
		self.source = source
		self.trigger = trigger
		self.target = target


if __name__ == '__main__':
	print('Hello')

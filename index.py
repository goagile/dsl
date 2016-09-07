# 


class AbstractEvent:

	def __init__(self, name, code):
		self.name = name
		self.code = code


class Command(AbstractEvent):
	pass


class Event(AbstractEvent):
	pass


class State:

	def __init__(self, name):
		self.name = name
		self.actions = []
		self.transitions = {}

	def add_transition(self, event, target_state):
		assert target_state
		self.transitions[event.code] = Transition(self, event, target_state)

	def get_all_targets(self):
		result = []
		for key in self.transitions:
			result.append(self.transitions[key].target)
		return result

	def execute_actions(self, commands_channel):
		for c in self.actions:
			commands_channel.send(c.code)

	def has_transition(self, event_code):
		return event_code in self.transitions

	def target_state(self, event_code):
		return self.transitions.get(event_code).target


class Transition:

	def __init__(self, source, trigger, target):
		self.source = source
		self.trigger = trigger
		self.target = target

	def get_event_code(self):
		return self.trigger.code


class StateMachine:

	def __init__(self, start):
		self.start = start

	def get_states(self):
		result = []
		self.collect_states(result, self.start)
		return result

	def collect_states(self, result, start):
		if start in result:
			return
		result.append(start)
		for next_ in start.get_all_targets():
			self.collect_states(result, next_)

	def add_reset_events(self, events):
		for e in events:
			self.reset_events.append(e)

	def is_reset_event(self, event_code):
		return event_code in self.reset_event_codes()

	def reset_event_codes(self):
		result = []
		for e in self.reset_events:
			result.append(e.code)
		return result


class Controller:

	def __init__(self):
		self.commands_channel = None
		self.current_state = None
		self.machine = None

	def handle(self, event_code):
		if current_state.has_transition(event_code):
			self.transition_to(current_state.target_state(event_code))
		else if self.machine.is_reset_event(event_code):
			self.transition_to(self.machine.get_start())

	def transition_to(self, target):
		self.current_state = target
		self.current_state.execute_actions(self.commands_channel)


if __name__ == '__main__':
	print('Hello')

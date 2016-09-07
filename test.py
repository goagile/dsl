import unittest
from index import (
	Command,
	Event,
	State,
	Transition,
	StateMachine,
	State,
	Controller,
)


class TestCase(unittest.TestCase):

	def test_command_and_event(self):
		c = Command('open_door_1', 'OPD1')
		e = Event('door_1_open', 'D1OP')
		
		self.assertEquals(c.name, 'open_door_1')
		self.assertEquals(c.code, 'OPD1')

	def test_state(self):
		state = State('door_1_closed')
		target_state = State('door_1_opened')
		event = Event('door_1_open', 'D1OP')
		state.add_transition(event, target_state)
		
		self.assertIn(event.code, state.transitions)
		transition = state.transitions[event.code]
		self.assertIsInstance(transition, Transition)

	def test_get_all_targets(self):
		d1cl = State('door_1_closed')
		walg = State('wait_light')
		lgon = State('light_on')
		
		door_1_open = Event('door_1_open', 'D1OP')
		light_on = Event('light_on', 'LGON')
		
		d1cl.add_transition(door_1_open, walg)
		walg.add_transition(light_on, lgon)

		self.assertEquals([walg], d1cl.get_all_targets())

	def test_transition(self):
		source = State('s1')
		trigger = Event('s1_to_s2', 's12')
		target = State('s2')
		t = Transition(source, trigger, target)

		self.assertEquals(source, t.source)
		self.assertEquals(trigger, t.trigger)
		self.assertEquals(target, t.target)

	def test_machine(self):
		start = State('s1')
		sm = StateMachine(start)
		
		states = sm.get_states()
		self.assertEquals(1, len(states))
		self.assertIn(start, states)


class TestController(unittest.TestCase):

	def test_transition_to(self):
		c = Controller()
		target = State('s1')

		self.assertTrue(c)
		c.transition_to(target)
		self.assertEquals(target, c.current_state)

	def test_handle(self):
		c = Controller()
		target = State('state1')
		event = Event('event1', 'e1')

		c.handle('e1')

if __name__ == '__main__':
	unittest.main()

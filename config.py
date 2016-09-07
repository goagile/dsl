from index import (
	Command,
	Event,
	State,
	StateMachine,
)


door_closed = Event('door_closed', 		'D1CL')
drawer_opened = Event('drawer_opened', 	'D2OP')
light_on = Event('light_on', 			'L1ON')
door_opened = Event('door_opened', 		'D1OP')
panel_closed = Event('panel_closed', 	'PNCL')

unlock_panel_cmd = Command('unlock_panel', 	'PNUL')
lock_panel_cmd = Command('lock_panel', 		'PNLK')
lock_door_cmd = Command('lock_door', 		'D1LK')
unlock_door_cmd = Command('unlock_door', 	'D1UL')

idle = State('idle')
active_state = State('active')
waiting_for_light_state = State('waiting_for_light')
waiting_for_drawer_state = State('waiting_for_drawer')
unlocked_panel_state = State('unlocked_panel')

machine = StateMachine(idle)

idle.add_transition(door_closed, active_state)
idle.add_action(unlock_door_cmd)
idle.add_action(lock_panel_cmd)

active_state.add_transition(drawer_opened, waiting_for_light_state)
active_state.add_transition(light_on, waiting_for_drawer_state)

waiting_for_light_state.add_transition(light_on, unlocked_panel_state)

waiting_for_drawer_state.add_transition(drawer_opened, unlocked_panel_state)

unlocked_panel_state.add_transition(panel_closed, idle)
unlocked_panel_state.add_action(unlock_panel_cmd)
unlocked_panel_state.add_action(lock_door_cmd)

machine.add_reset_events(door_opened)
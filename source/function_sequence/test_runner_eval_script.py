import unittest

from examples.function_sequence.constants import EXAMPLE_PATH
from examples.function_sequence.runner import Runner


class TestRunnerRun(unittest.TestCase):

    def test(self):
        expected = {
            'processor': {'cores': 2, 'speed': 2500, 'type': 'i386'},
            'discs': [
                {'size': 150},
                {'size': 75, 'speed': 7200, 'serial': 'SATA'}
            ]
        }
        runner = Runner(
            path=EXAMPLE_PATH,
            runner_template_filename='runner_template.js',
            script_filename='script.js'
        )

        result = runner.eval_script()

        self.assertEqual(expected, result)

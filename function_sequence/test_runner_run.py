import unittest

from examples.function_sequence.computer_builder import ComputerBuilder
from examples.function_sequence.constants import EXAMPLE_PATH
from examples.function_sequence.runner import Runner


class TestRunnerRun(unittest.TestCase):

    def test(self):
        builder = ComputerBuilder()
        builder.add_processor(cores=2, speed=2500, type='i386')
        builder.add_disk(size=150)
        builder.add_disk(size=75, speed=7200, serial='SATA')
        expected = builder.build()
        runner = Runner(
            path=EXAMPLE_PATH,
            runner_template_filename='runner_template.js',
            script_filename='script.js',
            model_builder=ComputerBuilder
        )

        result = runner.run()

        self.assertEqual(expected, result)

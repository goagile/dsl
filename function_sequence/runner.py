import os

import execjs


class Runner:

    def __init__(self, path, runner_template_filename, script_filename, model_builder=None):
        self.path = path
        self.runner_template_filename = runner_template_filename
        self.script_filename = script_filename
        self.model_builder = model_builder

    def run(self):
        dict_ = self.eval_script()
        result = self.model_builder().from_dict(dict_)
        return result

    def eval_script(self):
        template = self._load_runner()
        script = self._load_script()
        return execjs.eval(template % script)

    def _load_runner(self):
        return self._load_from_js(self.runner_template_filename)

    def _load_script(self):
        return self._load_from_js(self.script_filename)

    def _load_from_js(self, filename):
        path = os.path.join(self.path, filename)
        with open(path, 'r') as file:
            result = file.read()
        return result

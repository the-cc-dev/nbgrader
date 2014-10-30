from IPython.config.loader import Config
from IPython.config.application import catch_config_error
from IPython.utils.traitlets import Unicode
from nbgrader.apps.customnbconvertapp import CustomNbConvertApp
from nbgrader.apps.customnbconvertapp import aliases as base_aliases
from nbgrader.apps.customnbconvertapp import flags as base_flags


aliases = {}
aliases.update(base_aliases)
aliases.update({
    'regexp': 'FindStudentID.regexp',
    'assignment': 'SaveAutoGrades.assignment_id'
})

flags = {}
flags.update(base_flags)
flags.update({
})


class AutogradeApp(CustomNbConvertApp):
    
    name = Unicode(u'nbgrader-autograde')
    description = Unicode(u'Autograde a notebook by running it')
    aliases = aliases
    flags = flags

    student_id = Unicode(u'', config=True)

    def _export_format_default(self):
        return 'notebook'

    def build_extra_config(self):
        self.extra_config = Config()
        self.extra_config.Exporter.preprocessors = [
            'nbgrader.preprocessors.FindStudentID',
            'IPython.nbconvert.preprocessors.ClearOutputPreprocessor',
            'IPython.nbconvert.preprocessors.ExecutePreprocessor',
            'nbgrader.preprocessors.SaveAutoGrades'
        ]
        self.config.merge(self.extra_config)

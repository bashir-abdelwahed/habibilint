from unittest import TestCase

from flake8.options.manager import OptionManager

from habibilint.config import get_config
from habibilint.docstring.style import DocstringStyle
from habibilint.flake8_entry import HabibilintChecker
from habibilint.strictness import Strictness


class Flake8TestCase(TestCase):
    """Tests that flake8 config is parsed correctly."""

    def test_config_parsed(self):
        default_config = get_config().get_default_instance()
        parser = OptionManager("", "")
        HabibilintChecker.add_options(parser)

        options, args = parser.parse_args([])
        HabibilintChecker.parse_options(options)
        self.assertEqual(default_config.style, HabibilintChecker.config.style)

        argv = ["--docstring-style=numpy", "--strictness=short"]
        options, args = parser.parse_args(argv)

        HabibilintChecker.config = default_config
        HabibilintChecker.parse_options(options)
        self.assertEqual(HabibilintChecker.config.style, DocstringStyle.NUMPY)
        self.assertEqual(
            HabibilintChecker.config.strictness, Strictness.SHORT_DESCRIPTION
        )

#!/usr/bin/env python

"""Tests for `gps_demo` package."""


import unittest
from click.testing import CliRunner

from gps_demo import gps_demo
from gps_demo import cli


class TestGps_demo(unittest.TestCase):
    """Tests for `gps_demo` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'gps_demo.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

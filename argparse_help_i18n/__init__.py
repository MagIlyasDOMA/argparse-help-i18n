import locale
from argparse import ArgumentParser
from pathlib import Path
from locale_plus import Internationalizator

__all__ = ['HelpI18nMixin']

locale.setlocale(locale.LC_ALL, '')
gettext = Internationalizator(Path(__file__).parent / 'locale', domain='argparse-help').gettext


class HelpI18nMixin(ArgumentParser):
    def __init__(self, *args, add_help: bool = True, add_version: bool = True, **kwargs):
        super().__init__(*args, add_help=False, **kwargs)
        if add_help:
            self.add_argument('--help', '-h', action='help',
                              help=gettext("Show this help message and exit"))
        if add_version:
            self.add_argument('--version', '-v', action='version',
                              help=gettext("Show program's version and exit"))

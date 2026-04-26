import locale
from argparse import ArgumentParser
from pathlib import Path
from typing import Optional
from locale_plus import Internationalizator

__all__ = ['HelpI18nMixin', 'get_help_message', 'get_version_message']

locale.setlocale(locale.LC_ALL, '')
gettext = Internationalizator(Path(__file__).parent / 'locale', domain='argparse-help').gettext


def get_help_message(): return gettext("Show this help message and exit")

def get_version_message(): return gettext("Show program's version and exit")


class HelpI18nMixin(ArgumentParser):
    @staticmethod
    def get_help_message(): return get_help_message()

    @staticmethod
    def get_version_message(): return get_version_message()

    def __init__(self, *args, add_help: bool = True, add_version: bool = True,
                 version: Optional[str] = None, **kwargs):
        super().__init__(*args, add_help=False, **kwargs)
        if add_help:
            self.add_argument('--help', '-h', action='help', help=get_help_message())
        if add_version:
            self.add_argument('--version', '-v', action='version', help=get_version_message())

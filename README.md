# argparse-help-i18n

[English](#english) | [Русский](#русский) | [Español](#español) | [Français](#français) | [Italiano](#italiano) | [中文](#中文) | [العربية](#العربية)

---

## English

**argparse-help-i18n** is a lightweight Python package that adds internationalization (i18n) support to `argparse` help messages.

It provides a `HelpI18nMixin` class that automatically translates `--help` / `-h` and `--version` / `-v` option descriptions using `locale-plus` and GNU Gettext.

### Features
- Automatic translation of help and version option descriptions
- Uses system locale settings (`locale.setlocale(locale.LC_ALL, '')`)
- Built on `locale-plus` for reliable locale handling
- Easy to integrate with existing `argparse` code

### Installation
```bash
pip install argparse-help-i18n
```

### Usage
```python
from argparse import ArgumentParser
from argparse_help_i18n import HelpI18nMixin

class MyParser(HelpI18nMixin, ArgumentParser):
    pass

parser = MyParser(description="My app description")
parser.add_argument("--input", help="Input file")
parser.parse_args()
```

### Translation Files
Place `.mo` files in argparse_help_i18n/locale/{lang}/LC_MESSAGES/argparse-help.mo

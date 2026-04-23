# argparse-help-i18n

[English](#english) | [Русский](#русский) | [Español](#español) | [Français](#français) | [Italiano](#italiano) | [中文](#中文) | [العربية](#العربية)

---

## English

**argparse-help-i18n** is a lightweight Python package that adds
internationalization (i18n) support to `argparse` help messages.

It provides a `HelpI18nMixin` class that automatically translates `--help` /
`-h` and `--version` / `-v` option descriptions using `locale-plus` and GNU
Gettext.

### Features
- Automatic translation of help and version option descriptions
- Uses system locale settings (`locale.setlocale(locale.LC_ALL, '')`)
- Built on `locale-plus` for reliable locale handling
- Easy to integrate with existing `argparse` code

### Installation
```shell
pip install argparse-help-i18n
```

### Usage
```python
from argparse_help_i18n import HelpI18nMixin

parser = HelpI18nMixin(description="My app description")
parser.add_argument("--input", help="Input file")
parser.parse_args()
```

### Translation Files

Place `.mo` files in `argparse_help_i18n/locale/{lang}/LC_MESSAGES/argparse-
help.mo`

### Development
```shell
uv sync --group dev
devscript generate  # Extract strings
devscript compile   # Compile translations
```

### License
MIT

---

## Русский
**argparse-help-i18n** — это лёгкий пакет Python, добавляющий
интернационализацию (i18n) в справочные сообщения `argparse`.

Он предоставляет класс `HelpI18nMixin`, который автоматически переводит
описания опций `--help` / `-h` и `--version` / `-v` с помощью `locale-plus` и
GNU Gettext.

### Возможности
- Автоматический перевод описаний опций помощи и версии
- Использует системные настройки локали (`locale.setlocale(locale.LC_ALL, '')`)
- Построен на `locale-plus` для надёжной обработки локали
- Лёгкая интеграция с существующим кодом `argparse`

### Установка
```shell
pip install argparse-help-i18n
```

### Использование
```python
from argparse_help_i18n import HelpI18nMixin

parser = HelpI18nMixin(description="Описание моего приложения")
parser.add_argument("--input", help="Входной файл")
parser.parse_args()
```

### Файлы переводов

Разместите файлы `.mo` в
`argparse_help_i18n/locale/{lang}/LC_MESSAGES/argparse-help.mo`

### Разработка 
```shell
uv sync --group dev
devscript generate  # Извлечение строк
devscript compile   # Компиляция переводов
```

### Лицензия
MIT

---

## Español

**argparse-help-i18n** es un paquete ligero de Python que añade
internacionalización (i18n) a los mensajes de ayuda de `argparse`.

Proporciona una clase `HelpI18nMixin` que traduce automáticamente las
descripciones de las opciones `--help` / `-h` y `--version` / `-v` usando
`locale-plus` y GNU Gettext.

### Características

- Traducción automática de las descripciones de ayuda y versión
- Utiliza la configuración regional del sistema (`locale.setlocale(locale.LC_ALL, '')`)
- Basado en `locale-plus` para un manejo fiable de la configuración regional
- Fácil integración con código `argparse` existente

### Instalación
```shell
pip install argparse-help-i18n
```

### Uso
```python
from argparse_help_i18n import HelpI18nMixin

parser = HelpI18nMixin(description="Descripción de mi aplicación")
parser.add_argument("--input", help="Archivo de entrada")
parser.parse_args()
```

### Archivos de traducción

Coloque los archivos `.mo` en
`argparse_help_i18n/locale/{lang}/LC_MESSAGES/argparse-help.mo`

### Desarrollo
```shell 
uv sync --group dev
devscript generate  # Extraer cadenas
devscript compile   # Compilar traducciones
```

### Licencia

MIT

---

## Français

**argparse-help-i18n** est un package Python léger qui ajoute la prise en
charge de l'internationalisation (i18n) aux messages d'aide d'`argparse`.

Il fournit une classe `HelpI18nMixin` qui traduit automatiquement les
descriptions des options `--help` / `-h` et `--version` / `-v` en utilisant
`locale-plus` et GNU Gettext.

### Fonctionnalités
- Traduction automatique des descriptions d'aide et de version
- Utilise les paramètres régionaux du système (`locale.setlocale(locale.LC_ALL, '')`)
- Basé sur `locale-plus` pour une gestion fiable des locales
- Intégration facile avec le code `argparse` existant

### Installation
```shell
pip install argparse-help-i18n
```

### Utilisation
```python
from argparse_help_i18n import HelpI18nMixin

parser = HelpI18nMixin(description="Description de mon application")
parser.add_argument("--input", help="Fichier d'entrée")
parser.parse_args()
```

### Fichiers de traduction

Placez les fichiers `.mo` dans
`argparse_help_i18n/locale/{lang}/LC_MESSAGES/argparse-help.mo`

### Développement
```shell
uv sync --group dev
devscript generate  # Extraire les chaînes
devscript compile   # Compiler les traductions
```

### Licence
MIT

---

## Italiano

**argparse-help-i18n** è un pacchetto Python leggero che aggiunge il supporto
all'internazionalizzazione (i18n) per i messaggi di aiuto di `argparse`.

Fornisce una classe `HelpI18nMixin` che traduce automaticamente le descrizioni
delle opzioni `--help` / `-h` e `--version` / `-v` utilizzando `locale-plus` e
GNU Gettext.

### Caratteristiche

- Traduzione automatica delle descrizioni delle opzioni di aiuto e versione
- Utilizza le impostazioni locali di sistema (`locale.setlocale(locale.LC_ALL, '')`)
- Basato su `locale-plus` per una gestione affidabile delle impostazioni locali
- Facile integrazione con codice `argparse` esistente

### Installazione
```shell
pip install argparse-help-i18n
```

### Utilizzo
```python    
from argparse_help_i18n import HelpI18nMixin

parser = HelpI18nMixin(description="Descrizione della mia applicazione")
parser.add_argument("--input", help="File di input")
parser.parse_args()
```

### File di traduzione

Posiziona i file `.mo` in
`argparse_help_i18n/locale/{lang}/LC_MESSAGES/argparse-help.mo`

### Sviluppo
```shell
uv sync --group dev
devscript generate  # Estrai stringhe
devscript compile   # Compila traduzioni
```

### Licenza
MIT

---

## 中文

**argparse-help-i18n** 是一个轻量级的 Python 包，为 `argparse` 的帮助消息添加国际化（i18n）支持。

它提供了一个 `HelpI18nMixin` 类，使用 `locale-plus` 和 GNU Gettext 自动翻译 `--help` / `-h` 和
`--version` / `-v` 选项的描述。

### 特性

- 自动翻译帮助和版本选项的描述
- 使用系统区域设置（`locale.setlocale(locale.LC_ALL, '')`）
- 基于 `locale-plus` 实现可靠的区域处理
- 易于集成到现有的 `argparse` 代码中

### 安装
```shell
pip install argparse-help-i18n
```

### 使用
```python
from argparse_help_i18n import HelpI18nMixin

parser = HelpI18nMixin(description="我的应用程序描述")
parser.add_argument("--input", help="输入文件")
parser.parse_args()
```

### 翻译文件

将 `.mo` 文件放置在 `argparse_help_i18n/locale/{lang}/LC_MESSAGES/argparse-help.mo`

### 开发
```shell
uv sync --group dev
devscript generate  # 提取字符串
devscript compile   # 编译翻译
```

### 许可证
MIT

---

## العربية

**argparse-help-i18n** هي حزمة Python خفيفة الوزن تضيف دعم التدويل (i18n)
لرسائل المساعدة في `argparse`.

توفر class `HelpI18nMixin` والذي يترجم تلقائيًا أوصاف الخيارين `--help` / `-h`
و `--version` / `-v` باستخدام `locale-plus` و GNU Gettext.

### الميزات

- ترجمة تلقائية لأوصاف خيارات المساعدة والإصدار
- يستخدم إعدادات اللغة الإقليمية للنظام (`locale.setlocale(locale.LC_ALL, '')`)
- مبني على `locale-plus` للتعامل الموثوق مع اللغة الإقليمية
- سهل الدمج مع كود `argparse` الحالي

### التثبيت
```shell
pip install argparse-help-i18n
```

### الاستخدام
```python
from argparse_help_i18n import HelpI18nMixin

parser = HelpI18nMixin(description="وصف تطبيقي")
parser.add_argument("--input", help="ملف الإدخال")
parser.parse_args()
```

### ملفات الترجمة

ضع ملفات `.mo` في المسار
`argparse_help_i18n/locale/{lang}/LC_MESSAGES/argparse-help.mo`

### التطوير
```shell
uv sync --group dev
devscript generate  # استخراج النصوص
devscript compile   # ترجمة الملفات
```

### الترخيص
MIT

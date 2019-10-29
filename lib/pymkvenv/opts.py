import argparse
from typing import cast


def VERSION() -> str: return '1.5'


class Args:
  noGitignore: bool
  noReq: bool
  venvDir: str
  displayVersion: bool
  projectDir: str


def parseArgs() -> Args:
  parser = argparse.ArgumentParser(
    description = 'Automate creation of virtual environments in Python 3 projects',
    formatter_class = argparse.RawDescriptionHelpFormatter,
    epilog = f"""
Creates a Python virtual environment directory in a new or existing project
using `python3 -m venv`. After the environment is created, this tool will
update `pip`, `setuptools` and `wheel`. Finally, it will detect a
`requirements.txt` file and `pip install -r` it.

This tool will also create a `.gitignore` file if none is present.

After your environment is created, don't forget to activate

  $ . ./.venv/bin/activate

If you add more packages, consider refreshing the `requirements.txt` file

  $ pip install SOME_PYTHON_PACKAGE
  $ pip freeze > requirements.txt

To leave the environment, deactivate

  $ deactivate

v{VERSION()}  Dino Morelli <dino@ui3.info>"""
    )

  parser.add_argument(
    '-G', '--no-gitignore',
    dest = 'noGitignore',
    action = 'store_true',
    help = "Suppress creation of `.gitignore` file"
    )

  parser.add_argument(
    '-R', '--no-req',
    dest = 'noReq',
    action = 'store_true',
    help = "Suppress installation of dependencies in `requirements.txt`"
    )

  venvDefault = '.venv'
  parser.add_argument(
    '-v', '--venv-dir',
    dest = 'venvDir',
    metavar = 'DIR',
    default = venvDefault,
    help = f"Directory under the project to create the virtual environment [default: {venvDefault}]"
    )

  parser.add_argument(
    '--version',
    dest = 'displayVersion',
    action = 'store_true',
    help = "Show version info and exit"
    )

  projectDirDefault = '.'
  parser.add_argument(
    'projectDir',
    metavar = 'PROJECT_DIR',
    nargs = '?',
    default = projectDirDefault,
    help = f"Project directory, specifying this will create a new project directory and environment within it [default: {projectDirDefault}]"
    )

  return cast(Args, parser.parse_args())

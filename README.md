# py3-mkvenv


## Synopsis

Automate creation of virtual environments in Python 3 projects


## Description

Create a Python virtual environment directory in a new or existing project
using `python -m venv`. After the environment is created, this tool will update
pip, setuptools and wheel. Finally, it will detect a `requirements.txt` file
and `pip install -r` it.

This tool will also create a .gitignore file if none is present.


## Development

### Setting up your development environment

Source code is available from github at the
[py3-mkvenv](https://github.com/dino-/py3-mkvenv) project page. This directory
will of course have no virtual environment specific to your system.

This tool exists to perform most of the following steps, but if you don't have
it operational yet, you'll need to manually bootstrap the virtual environment.
Here's how:

From within the `py3-mkvenv` directory, set up the venv

    $ cd py3-mkvenv
    $ python3 -m venv .venv

From here on out, make sure you're working in the environment

    $ source ./.venv/bin/activate

Update the tools

    $ python -m pip install --upgrade pip setuptools wheel

Install the project's dependencies using the `requirements.txt` file

    $ pip install -r requirements.txt

Over time, you may install more libraries using `pip install`. Get a list of
those and check these changes into source control if necessary.

    $ pip freeze > requirements.txt

If desired, deactivate the virtual environment in your shell

    $ deactivate

### Issue tracking

We are tracking tasks and progress on a public [py3-mkvenv Trello
board](https://trello.com/b/hkjMdAbG/py3-mkvenv)


## Contact

Dino Morelli <dino@ui3.info>

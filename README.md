# py-mkvenv


## Synopsis

Automate creation of virtual environments in Python 3 projects


## Description

Creates a Python virtual environment directory in a new or existing project
using `python3 -m venv`. After the environment is created, this tool will
update `pip`, `setuptools` and `wheel`. Finally, it will detect a
`requirements.txt` file and `pip install -r` it.

This tool will also create a `.gitignore` file if none is present.


## Getting binaries

py-mkvenv is available for Linux in AppImage form [from github](https://github.com/dino-/py-mkvenv/releases)


## Development

### Setting up your development environment

Source code is available from github at the
[py-mkvenv](https://github.com/dino-/py-mkvenv) project page. This directory
will of course have no virtual environment specific to your system.

This tool exists to perform most of the following steps, but if you don't have
it operational yet, you'll need to manually bootstrap the virtual environment.
Here's how:

From within the `py-mkvenv` directory, set up the venv

    $ cd py-mkvenv
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

### Building a release AppImage

It's important to build the [AppImage](https://appimage.org/) on an older
distribution so it's compatible with many systems. In practical terms Ubuntu
14.04 is a good choice for this.

The stock version of Python 3 on Ubuntu 14.04 is 3.4 but we need a higher
version.

So, install Python 3.6:

    # add-apt-repository ppa:deadsnakes/ppa
    # apt-update
    # apt install python3.6 python3.6-dev python3.6-venv

Use an earlier version of py-mkvenv to make the virtual environment or, if that isn't possible:

    $ python3.6 -m venv .venv
    $ ./.venv/bin/python -m pip install --upgrade pip setuptools wheel
    $ . ./.venv/bin/activate
    $ pip install -r requirements.txt

`python3` on a Ubuntu 14.04 system will point to Python 3.4 so you must edit the #! line in `py-mkvenv` to point to `python3.6` instead of `python3`

You should now be able to run it, type check it with mypy, etc.

You will need the AppDir tool [linuxdeploy](https://github.com/linuxdeploy/linuxdeploy)
and the AppImage plugin [linuxdeploy-plugin-appimage](https://github.com/linuxdeploy/linuxdeploy-plugin-appimage).
These need to be set executable and must be on your PATH.

The project's `requirements.txt` will pull in `pyinstaller` which will be used
to build a distributable standalone directory in `dist`

First, prep the AppDir with one provided for this project like this:

    $ cp -r util/resources/AppDir .

Next, build a standalone distributable directory with `pyinstaller`.

    $ pyinstaller py-mkvenv.spec

Move those build artifacts into the AppDir directory.

    $ mv dist/py-mkvenv AppDir/usr/share

Finally, run `linuxdeploy` to complete the process of creating the AppImage

    $ linuxdeploy-x86_64.AppImage --appdir=AppDir --output=appimage

You should now have a binary named something like `py-mkvenv-75d2222-x86_64.AppImage`.

This binary could be renamed to something like `py-mkvenv-1.4-x86_64.AppImage` if you
wish the version number to be explicit in the filename.

These steps will likely be automated in the future.

### Updating the libraries

Replace all `==` with `>=` in `requirements.txt, then

    $ pip install --upgrade --force-reinstall -r requirements.txt
    $ pip freeze > requirements.txt

And check this new version of `requirements.txt` into source control.


## Contact

Dino Morelli <dino@ui3.info>

Detect Chinese characters in image captcha via opencv


## Getting Started

The project is ready to run as is. You will need Python 3.0 or later.

### Create a Virtual Environment

After cloning or downloading the repo, create a Python virtual environment with:

```
python -m venv .virtualenv
```

if the `pyvenv` command does not exist on your system.

### Activate the Virtual Environment

Now activate the virtual environment. on macOS, Linux and Unix systems, use:

```
source .virtualenv/bin/activate
```

On Windows:

```
.virtualenv\Scripts\activate.bat
```

### Install the Development Environment

Now run:

```
pip install --upgrade pip setuptools wheel # you will need this if you saw the error like ERROR: Failed building wheel for cmake
pip install -e .[dev]
```

This will install the packages the project depends on in production as well as packages needed during development.

At this point, you are ready to start modifying to template for your own needs.

## Run the program
```
python detect/main.py images/p8.jpg
```

## Testing

You can run unit tests through setup.py with:

```
python setup.py test
```

or just run pytest directly:

```
pytest
```





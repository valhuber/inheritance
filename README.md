# Inheritance Test
Explore inheritance of base/sub in same package on PyPi.  Posted to [StackOverflow](https://stackoverflow.com/questions/63363476/pypi-installed-app-fails-with-modulenotfound).

## Install (VSCode)
Source Control view, clone: https://github.com/valhuber/inheritance.git.
```
cd inheritance
virtualenv venv
# windows: .\venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
```

## Run Locally

VSCode: F5 for `run.py`. Should print:
```
super
Sub here
```

## Deploy to Pypi
Since fab-quickstart is normally run via the command line, we must deploy to the PyPi site.

Using [this reference](https://packaging.python.org/tutorials/packaging-projects/)...

Acquire the setup software (initial, 1-time setup):
```
cd inheritance
deactivate
python setup.py install
python3 -m pip install --user --upgrade twine
python3 -m pip install --user --upgrade setuptools wheel
```

Creating the `dist`, **first time**
Get a [Saved API Key](https://test.pypi.org/manage/account/#api-tokens)

```
python3 setup.py sdist bdist_wheel  # verify this produces the dist folder
python3 -m twine upload --repository testpypi dist/*  # upload to test Pypi
```
User is `__token__`, pwd is **Saved API Key** (from above).

This should upload to the [Pypi site](https://test.pypi.org/project/Inheritance-Test/)

To **re-upload:**
1. Delete the `dist` folder (and `build`, and `.egg`)
2. Alter the version number in `__init__`
```
python3 setup.py sdist bdist_wheel
python3 -m twine upload  --skip-existing --repository testpypi dist/*
```

To install (beware - may require 15 mins until new version is active.  You may want to `pip uninstall Inheritance-Test` before the upload to be sure you have the latest.)

```
# windows: .\venv\Scripts\activate
source venv/bin/activate
pip install -i https://test.pypi.org/simple/ Inheritance-Test
inheritance-run
```

Currently failing:

```
Traceback (most recent call last):
  File "/Users/val/python/vscode/inheritance/venv/bin/inheritance-run", line 5, in <module>
    from src.inheritance_pkg.run_local import start
  File "/Users/val/python/vscode/inheritance/venv/lib/python3.8/site-packages/src/__init__.py", line 1, in <module>
    import inheritance_pkg  # attempting to force pkging of code
ModuleNotFoundError: No module named 'inheritance_pkg'
(venv) val@valMbp inheritance % 
```

The current structure built the src into an unexpected location in the ```env``` folder:

![generated page](https://drive.google.com/uc?export=view&id=1ZrzBRsUmc3A8AZY9RB-QvbQ0WXLma84w)

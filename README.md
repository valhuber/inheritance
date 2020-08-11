# Inheritance Test
Explore inheritance of base/sub in same package on PyPi.

```
pip install -i https://test.pypi.org/simple/ Inheritance-Test
inheritance-run
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
pip install -i https://test.pypi.org/simple/ Inheritance-Test
val@valMbp nw-app % inheritance-run
```

Currently failing:
```
Traceback (most recent call last):
  File "/Users/val/.pyenv/versions/3.8.3/bin/fab-quickstart", line 6, in <module>
    from fab_quickstart.cli import start
  File "/Users/val/.pyenv/versions/3.8.3/lib/python3.8/site-packages/fab_quickstart/cli.py", line 2, in <module>
    from base import FabQuickStart
ModuleNotFoundError: No module named 'base'
val@valMbp nw-app % 
```

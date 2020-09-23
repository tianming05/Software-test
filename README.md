# test-environment-template

Template for basic test environment.

## Things to install before you start

**Python 3**

Often included with your operating system, but you can also install it from https://www.python.org/

**Venv and Pip**

Venv keeps your system clean by installing Python modules in a specific directory in your working directory. Pip is the Python package manager that allows you to install modules in your venv directory.

Once you have venv (make sure you have the versions for Python 3), create a virtualenv directory in your working directory and activate the virtual environment:

```
$ cd YOUR_WORKING_DIRECTORY
$ python3 -m venv venv
$ source venv/bin/activate
```

Current versions of venv automatically install pip.

**Robot Framework**

Once you have Python3, venv and pip installed, you can install Robot Framework using pip:

```
$ pip install robotframework
```

You can also install Selenium for Robot Framework, which allows you to control a web browser to perform tests. This requires that you also install a driver manager that communicates with the browser. Here is how to install it for Chrome:

```
pip install robotframework-seleniumlibrary
pip install webdrivermanager
webdrivermanager chrome
```

You can install a driver manager for several other browsers as well. You need a recent version of the browser!

## What you can do

**Play with the `Hello` class**

```
$ python3 -i hello.py 
>>> hello = Hello()
>>> print(hello)
Hello, World!
>>> hello.name = "Yourname"
>>> print(hello)
Hello, Yourname!
```

**Run the unit test**

```
$ python3 tests.py 
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

**Run the Robot test**

```
$ robot browse.robot
==============================================================================
Browse                                                                        
==============================================================================
Site Language Is Set By URL                                           | PASS |
------------------------------------------------------------------------------
Browse                                                                | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
```

You can find the detailed test results in the files `output.xml`, `log.html`, and `report.html`.

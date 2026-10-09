# ContextFit annotation review

## dev_001 — direct

Why use separate virtual environments for applications?
- Expected: They isolate dependencies so applications can use conflicting package versions.

### python_venv_chunk001

12. Virtual Environments and Packages

12.1. Introduction

Python applications will often use packages and modules that don’t
come as part of the standard library.  Applications will sometimes
need a specific version of a library, because the application may
require that a particular bug has been fixed or the application may be
written using an obsolete version of the library’s interface.

This means it may not be possible for one Python installation to meet
the requirements of every application.  If application A needs version
1.0 of a particular module but application B needs version 2.0, then
the requirements are in conflict and installing either version 1.0 or 2.0
will leave one application unable to run.

The solution for this problem is to create a virtual environment , a
self-contained directory tree that contains a Python installation for a
particular version of Python, plus a number of additional packages.

Different applications can then use different virtual environments.
To resolve the earlier example of conflicting requirements,
application A can have its own virtual environment with version 1.0
installed while application B has another virtual environment with version 2.0.
If application B requires a library be upgraded to version 3.0, this will
not affect application A’s environment.

12.2. Creating Virtual Environments

## dev_002 — direct

What does the PYTHONPATH variable do?
- Expected: It supplies directories used to initialize the module search path.

### python_modules_chunk007

If the module is imported, the code is not run:

>>> import fibo
>>>

This is often used either to provide a convenient user interface to a module, or
for testing purposes (running the module as a script executes a test suite).

6.1.2. The Module Search Path

When a module named spam is imported, the interpreter first searches for
a built-in module with that name. These module names are listed in sys.builtin_module_names . If not found, it then searches for a file
named spam.py in a list of directories given by the variable sys.path . sys.path is initialized from these locations:

The directory containing the input script (or the current directory when no
file is specified).

PYTHONPATH (a list of directory names, with the same syntax as the
shell variable PATH ).

The installation-dependent default (by convention including a site-packages directory, handled by the site module).

More details are at The initialization of the sys.path module search path .

Note

On file systems which support symlinks, the directory containing the input
script is calculated after the symlink is followed. In other words the
directory containing the symlink is not added to the module search path.

## dev_003 — direct

When is the finally clause executed?
- Expected: It executes before the try statement completes, whether or not an exception occurs.

### python_errors_chunk011

Exception classes can be defined which do anything any other class can do, but
are usually kept simple, often only offering a number of attributes that allow
information about the error to be extracted by handlers for the exception.

Most exceptions are defined with names that end in “Error”, similar to the
naming of the standard exceptions.

Many standard modules define their own exceptions to report errors that may
occur in functions they define.

8.7. Defining Clean-up Actions

The try statement has another optional clause which is intended to
define clean-up actions that must be executed under all circumstances.  For
example:

>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt

If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or
not the try statement produces an exception. The following
points discuss more complex cases when an exception occurs:

If an exception occurs during execution of the try clause, the exception may be handled by an except clause. If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been executed.

## dev_004 — direct

Which command leaves an active virtual environment?
- Expected: Run deactivate.

### python_venv_chunk003

Activating the virtual environment will change your shell’s prompt to show what
virtual environment you’re using, and modify the environment so that running python will get you that particular version and installation of Python.
For example:

$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>

Note that the activated virtual environment does not alter the PYTHONPATH variable in any way.
This may lead to unexpected results if the path includes references to code which is incompatible with
the Python version the virtual environment is using. The best practice is to unset PYTHONPATH in bash or the equivalent for the shell you are using.

To deactivate a virtual environment, type:

deactivate

into the terminal.

12.3. Managing Packages with pip

You can install, upgrade, and remove packages using a program called pip .  By default pip will install packages from the Python
Package Index .  You can browse the Python
Package Index by going to it in your web browser.

## dev_005 — multi

How can I inspect an installed package and export installed versions for another environment?
- Expected: Use python -m pip show PACKAGE to inspect a package.
- Expected: Use python -m pip freeze to produce requirements-format output.

### python_venv_chunk005

(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0

python -m pip uninstall followed by one or more package names will
remove the packages from the virtual environment.

python -m pip show will display information about a particular package:

(tutorial-env) $ python -m pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:

python -m pip list will display all of the packages installed in
the virtual environment:

(tutorial-env) $ python -m pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)

### python_venv_chunk006

python -m pip freeze will produce a similar list of the installed packages,
but the output uses the format that python -m pip install expects.
A common convention is to put this list in a requirements.txt file:

(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0

The requirements.txt can then be committed to version control and
shipped as part of an application.  Users can then install all the
necessary packages with install -r :

(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0

## dev_006 — unanswerable

What monthly fee does the documentation specify for a hosted virtual-environment service?
- Expected: State that the supplied documentation does not specify this fee.

Check the entire corpus: no passage should supply the requested answer. Do not confuse an absent answer with a retrieval failure.

## test_001 — direct

Which Python version is installed in an environment created by python3.12 -m venv?
- Expected: Python 3.12, because venv uses the interpreter that runs the command.

### python_venv_chunk002

The module used to create and manage virtual environments is called venv . venv will install the Python version from which
the command was run (as reported by the --version option).
For instance, executing the command with python3.12 will install
version 3.12.

To create a virtual environment, decide upon a directory where you want to
place it, and run the venv module as a script with the directory path:

python -m venv tutorial-env

This will create the tutorial-env directory if it doesn’t exist,
and also create directories inside it containing a copy of the Python
interpreter and various supporting files.

A common directory location for a virtual environment is .venv .
This name keeps the directory typically hidden in your shell and thus
out of the way while giving it a name that explains why the directory
exists. It also prevents clashing with .env environment variable
definition files that some tooling supports.

Once you’ve created a virtual environment, you may activate it.

On Windows, run:

tutorial-env\Scripts\activate

On Unix or MacOS, run:

source tutorial-env/bin/activate

(This script is written for the bash shell.  If you use the csh or fish shells, there are alternate activate.csh and activate.fish scripts you should use
instead.)

## test_002 — direct

How do I install exactly version 2.6.0 of requests using pip?
- Expected: Run python -m pip install requests==2.6.0.

### python_venv_chunk004

pip has a number of subcommands: “install”, “uninstall”,
“freeze”, etc.  (Consult the Installing Python modules guide for
complete documentation for pip .)

You can install the latest version of a package by specifying a package’s name:

(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3

You can also install a specific version of a package by giving the
package name  followed by == and the version number:

(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0

If you re-run this command, pip will notice that the requested
version is already installed and do nothing.  You can supply a
different version number to get that version, or you can run python -m pip install --upgrade to upgrade the package to the latest version:

## test_003 — direct

What does pip do if I repeat the installation command for an already installed requested version?
- Expected: It notices that the requested version is installed and does nothing.

### python_venv_chunk004

pip has a number of subcommands: “install”, “uninstall”,
“freeze”, etc.  (Consult the Installing Python modules guide for
complete documentation for pip .)

You can install the latest version of a package by specifying a package’s name:

(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3

You can also install a specific version of a package by giving the
package name  followed by == and the version number:

(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0

If you re-run this command, pip will notice that the requested
version is already installed and do nothing.  You can supply a
different version number to get that version, or you can run python -m pip install --upgrade to upgrade the package to the latest version:

## test_004 — direct

How can another developer install the packages listed in requirements.txt?
- Expected: Run python -m pip install -r requirements.txt.

### python_venv_chunk006

python -m pip freeze will produce a similar list of the installed packages,
but the output uses the format that python -m pip install expects.
A common convention is to put this list in a requirements.txt file:

(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0

The requirements.txt can then be committed to version control and
shipped as part of an application.  Users can then install all the
necessary packages with install -r :

(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0

## test_005 — direct

Does import fibo directly add fib and fib2 to the current namespace?
- Expected: No. It adds the module name fibo; access its functions through that module.

### python_modules_chunk002

# Fibonacci numbers module

def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

Now enter the Python interpreter and import this module with the following
command:

>>> import fibo

This does not add the names of the functions defined in fibo directly to
the current namespace (see Python Scopes and Namespaces for more details);
it only adds the module name fibo there. Using
the module name you can access the functions:

## test_006 — direct

How can I reload a changed module during an interactive interpreter session?
- Expected: Use importlib.reload(modulename), after importing importlib.

### python_modules_chunk006

>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

Note

For efficiency reasons, each module is only imported once per interpreter
session.  Therefore, if you change your modules, you must restart the
interpreter – or, if it’s just one module you want to test interactively,
use importlib.reload() , e.g. import importlib; importlib.reload(modulename) .

6.1.1. Executing modules as scripts

When you run a Python module with

python fibo.py <arguments>

the code in the module will be executed, just as if you imported it, but with
the __name__ set to "__main__" .  That means that by adding this code at
the end of your module:

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

you can make the file usable as a script as well as an importable module,
because the code that parses the command line only runs if the module is
executed as the “main” file:

$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34

## test_007 — direct

Where does Python cache compiled modules, and how does it detect stale cached code?
- Expected: It stores compiled modules in __pycache__ using version-tagged .pyc names.
- Expected: It checks the source modification date against the compiled version.

### python_modules_chunk008

After initialization, Python programs can modify sys.path .  The
directory containing the script being run is placed at the beginning of the
search path, ahead of the standard library path. This means that scripts in that
directory will be loaded instead of modules of the same name in the library
directory. This is an error unless the replacement is intended.  See section Standard Modules for more information.

6.1.3. “Compiled” Python files

To speed up loading modules, Python caches the compiled version of each module
in the __pycache__ directory under the name module. version .pyc ,
where the version encodes the format of the compiled file; it generally contains
the Python version number.  For example, in CPython release 3.3 the compiled
version of spam.py would be cached as __pycache__/spam.cpython-33.pyc .  This
naming convention allows compiled modules from different releases and different
versions of Python to coexist.

Python checks the modification date of the source against the compiled version
to see if it’s out of date and needs to be recompiled.  This is a completely
automatic process.  Also, the compiled modules are platform-independent, so the
same library can be shared among systems with different architectures.

## test_008 — direct

Does reading a program from a .pyc file make its execution faster than reading it from .py?
- Expected: No. Compiled files load faster, but the program itself does not run faster for that reason.

### python_modules_chunk009

Python does not check the cache in two circumstances.  First, it always
recompiles and does not store the result for the module that’s loaded directly
from the command line.  Second, it does not check the cache if there is no
source module.  To support a non-source (compiled only) distribution, the
compiled module must be in the source directory, and there must not be a source
module.

Some tips for experts:

You can use the -O or -OO switches on the Python command
to reduce the size of a compiled module.  The -O switch removes assert
statements, the -OO switch removes both assert statements and __doc__
strings.  Since some programs may rely on having these available, you should
only use this option if you know what you’re doing.  “Optimized” modules have
an opt- tag and are usually smaller.  Future releases may
change the effects of optimization.

A program doesn’t run any faster when it is read from a .pyc file than when it is read from a .py file; the only thing that’s faster
about .pyc files is the speed with which they are loaded.

The module compileall can create .pyc files for all modules in a
directory.

There is more detail on this process, including a flow chart of the
decisions, in PEP 3147 .

6.2. Standard Modules

## test_009 — direct

What happens if an exception in a try clause matches none of its except clauses?
- Expected: It propagates to outer handlers; if none handles it, execution stops with an error.

### python_errors_chunk004

>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...

The try statement works as follows.

First, the try clause (the statement(s) between the try and except keywords) is executed.

If no exception occurs, the except clause is skipped and execution of the try statement is finished.

If an exception occurs during execution of the try clause, the rest of the
clause is skipped.  Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution
continues after the try/except block.

If an exception occurs which does not match the exception named in the except
clause , it is passed on to outer try statements; if no handler is
found, it is an unhandled exception and execution stops with an error message.

A try statement may have more than one except clause , to specify
handlers for different exceptions.  At most one handler will be executed.
Handlers only handle exceptions that occur in the corresponding try clause ,
not in other handlers of the same try statement.  An except clause may name multiple exceptions as a parenthesized tuple, for example:

... except (RuntimeError, TypeError, NameError):
...     pass

## test_010 — direct

If several except clauses could match an exception, which one runs?
- Expected: The first matching except clause runs.

### python_errors_chunk005

A class in an except clause matches exceptions which are instances of the
class itself or one of its derived classes (but not the other way around — an except clause listing a derived class does not match instances of its base classes).
For example, the following code will print B, C, D in that order:

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

Note that if the except clauses were reversed (with except B first), it
would have printed B, B, B — the first matching except clause is triggered.

When an exception occurs, it may have associated values, also known as the
exception’s arguments . The presence and types of the arguments depend on the
exception type.

The except clause may specify a variable after the exception name.  The
variable is bound to the exception instance which typically has an args attribute that stores the arguments. For convenience, builtin exception
types define __str__() to print all the arguments without explicitly
accessing .args .

## test_011 — direct

Why put successful follow-up work in a try statement's else clause?
- Expected: It runs when the try clause raises no exception.
- Expected: It avoids accidentally catching exceptions from follow-up work in the original handlers.

### python_errors_chunk007

The most common pattern for handling Exception is to print or log
the exception and then re-raise it (allowing a caller to handle the
exception as well):

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

The try … except statement has an optional else
clause , which, when present, must follow all except clauses .  It is useful
for code that must be executed if the try clause does not raise an exception.
For example:

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

The use of the else clause is better than adding additional code to
the try clause because it avoids accidentally catching an exception
that wasn’t raised by the code being protected by the try … except statement.

Exception handlers do not handle only exceptions that occur immediately in the try clause , but also those that occur inside functions that are called (even
indirectly) in the try clause . For example:

## test_012 — direct

How can I add explanatory notes to a caught exception, and where are those notes displayed?
- Expected: Call add_note with a string.
- Expected: The standard traceback displays the notes after the exception in insertion order.

### python_errors_chunk018

Note that the exceptions nested in an exception group must be instances,
not types. This is because in practice the exceptions would typically
be ones that have already been raised and caught by the program, along
the following pattern:

>>> excs = []
... for test in tests:
...     try:
...         test.run()
...     except Exception as e:
...         excs.append(e)
...
>>> if excs:
...    raise ExceptionGroup("Test Failures", excs)
...

8.10. Enriching Exceptions with Notes

When an exception is created in order to be raised, it is usually initialized
with information that describes the error that has occurred. There are cases
where it is useful to add information after the exception was caught. For this
purpose, exceptions have a method add_note(note) that accepts a string and
adds it to the exception’s notes list. The standard traceback rendering
includes all notes, in the order they were added, after the exception.

>>> try:
...     raise TypeError('bad type')
... except Exception as e:
...     e.add_note('Add some information')
...     e.add_note('Add some more information')
...     raise
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise TypeError('bad type')
TypeError: bad type
Add some information
Add some more information
>>>

## test_013 — multi

How can I create a virtual environment named tutorial-env and then install dependencies from requirements.txt into it?
- Expected: Create it with python -m venv tutorial-env and activate it.
- Expected: Then run python -m pip install -r requirements.txt.

### python_venv_chunk002

The module used to create and manage virtual environments is called venv . venv will install the Python version from which
the command was run (as reported by the --version option).
For instance, executing the command with python3.12 will install
version 3.12.

To create a virtual environment, decide upon a directory where you want to
place it, and run the venv module as a script with the directory path:

python -m venv tutorial-env

This will create the tutorial-env directory if it doesn’t exist,
and also create directories inside it containing a copy of the Python
interpreter and various supporting files.

A common directory location for a virtual environment is .venv .
This name keeps the directory typically hidden in your shell and thus
out of the way while giving it a name that explains why the directory
exists. It also prevents clashing with .env environment variable
definition files that some tooling supports.

Once you’ve created a virtual environment, you may activate it.

On Windows, run:

tutorial-env\Scripts\activate

On Unix or MacOS, run:

source tutorial-env/bin/activate

(This script is written for the bash shell.  If you use the csh or fish shells, there are alternate activate.csh and activate.fish scripts you should use
instead.)

### python_venv_chunk006

python -m pip freeze will produce a similar list of the installed packages,
but the output uses the format that python -m pip install expects.
A common convention is to put this list in a requirements.txt file:

(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0

The requirements.txt can then be committed to version control and
shipped as part of an application.  Users can then install all the
necessary packages with install -r :

(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0

## test_014 — multi

How can I upgrade requests and record the resulting installed package versions for sharing?
- Expected: Run python -m pip install --upgrade requests.
- Expected: Export versions with python -m pip freeze > requirements.txt.

### python_venv_chunk005

(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0

python -m pip uninstall followed by one or more package names will
remove the packages from the virtual environment.

python -m pip show will display information about a particular package:

(tutorial-env) $ python -m pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:

python -m pip list will display all of the packages installed in
the virtual environment:

(tutorial-env) $ python -m pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)

### python_venv_chunk006

python -m pip freeze will produce a similar list of the installed packages,
but the output uses the format that python -m pip install expects.
A common convention is to put this list in a requirements.txt file:

(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0

The requirements.txt can then be committed to version control and
shipped as part of an application.  Users can then install all the
necessary packages with install -r :

(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0

## test_015 — multi

How can I import fibo under the name fib and reload that module after editing it?
- Expected: Use import fibo as fib.
- Expected: After importing importlib, call importlib.reload(fib).

### python_modules_chunk005

>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This imports all names except those beginning with an underscore ( _ ).
In most cases Python programmers do not use this facility since it introduces
an unknown set of names into the interpreter, possibly hiding some things
you have already defined.

Note that in general the practice of importing * from a module or package is
frowned upon, since it often causes poorly readable code. However, it is okay to
use it to save typing in interactive sessions.

If the module name is followed by as , then the name
following as is bound directly to the imported module.

>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This is effectively importing the module in the same way that import fibo will do, with the only difference of it being available as fib .

It can also be used when utilising from with similar effects:

### python_modules_chunk006

>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

Note

For efficiency reasons, each module is only imported once per interpreter
session.  Therefore, if you change your modules, you must restart the
interpreter – or, if it’s just one module you want to test interactively,
use importlib.reload() , e.g. import importlib; importlib.reload(modulename) .

6.1.1. Executing modules as scripts

When you run a Python module with

python fibo.py <arguments>

the code in the module will be executed, just as if you imported it, but with
the __name__ set to "__main__" .  That means that by adding this code at
the end of your module:

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

you can make the file usable as a script as well as an importable module,
because the code that parses the command line only runs if the module is
executed as the “main” file:

$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34

## test_016 — multi

What does Python's compiled-module cache help with, and can compileall generate these files for a directory?
- Expected: The cache speeds up module loading.
- Expected: compileall can create .pyc files for modules in a directory.

### python_modules_chunk008

After initialization, Python programs can modify sys.path .  The
directory containing the script being run is placed at the beginning of the
search path, ahead of the standard library path. This means that scripts in that
directory will be loaded instead of modules of the same name in the library
directory. This is an error unless the replacement is intended.  See section Standard Modules for more information.

6.1.3. “Compiled” Python files

To speed up loading modules, Python caches the compiled version of each module
in the __pycache__ directory under the name module. version .pyc ,
where the version encodes the format of the compiled file; it generally contains
the Python version number.  For example, in CPython release 3.3 the compiled
version of spam.py would be cached as __pycache__/spam.cpython-33.pyc .  This
naming convention allows compiled modules from different releases and different
versions of Python to coexist.

Python checks the modification date of the source against the compiled version
to see if it’s out of date and needs to be recompiled.  This is a completely
automatic process.  Also, the compiled modules are platform-independent, so the
same library can be shared among systems with different architectures.

### python_modules_chunk009

Python does not check the cache in two circumstances.  First, it always
recompiles and does not store the result for the module that’s loaded directly
from the command line.  Second, it does not check the cache if there is no
source module.  To support a non-source (compiled only) distribution, the
compiled module must be in the source directory, and there must not be a source
module.

Some tips for experts:

You can use the -O or -OO switches on the Python command
to reduce the size of a compiled module.  The -O switch removes assert
statements, the -OO switch removes both assert statements and __doc__
strings.  Since some programs may rely on having these available, you should
only use this option if you know what you’re doing.  “Optimized” modules have
an opt- tag and are usually smaller.  Future releases may
change the effects of optimization.

A program doesn’t run any faster when it is read from a .pyc file than when it is read from a .py file; the only thing that’s faster
about .pyc files is the speed with which they are loaded.

The module compileall can create .pyc files for all modules in a
directory.

There is more detail on this process, including a flow chart of the
decisions, in PEP 3147 .

6.2. Standard Modules

## test_017 — multi

How do I explicitly link a new exception to its cause, and how do I suppress automatic exception chaining?
- Expected: Use raise NewException from original_exception to indicate the cause.
- Expected: Use raise NewException from None to suppress automatic chaining.

### python_errors_chunk009

>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise NameError('HiThere')
NameError: HiThere

8.5. Exception Chaining

If an unhandled exception occurs inside an except section, it will
have the exception being handled attached to it and included in the error
message:

>>> try:
...     open("database.sqlite")
... except OSError:
...     raise RuntimeError("unable to handle error")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    open("database.sqlite")
    ~~~~^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError("unable to handle error")
RuntimeError: unable to handle error

To indicate that an exception is a direct consequence of another, the raise statement allows an optional from clause:

# exc must be exception instance or None.
raise RuntimeError from exc

This can be useful when you are transforming exceptions. For example:

### python_errors_chunk010

>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    func()
    ~~~~^^
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database

It also allows disabling automatic exception chaining using the from None idiom:

>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError from None
RuntimeError

For more information about chaining mechanics, see Built-in Exceptions .

8.6. User-defined Exceptions

Programs may name their own exceptions by creating a new exception class (see Classes for more about Python classes).  Exceptions should typically
be derived from the Exception class, either directly or indirectly.

## test_018 — multi

How can several exception instances be raised together and only those of a chosen type handled?
- Expected: Wrap exception instances in an ExceptionGroup and raise it.
- Expected: Use except* to handle matching types within the group.

### python_errors_chunk015

The builtin ExceptionGroup wraps a list of exception instances so
that they can be raised together. It is an exception itself, so it can be
caught like any other exception.

>>> def f():
...     excs = [OSError('error 1'), SystemError('error 2')]
...     raise ExceptionGroup('there were problems', excs)
...
>>> f()
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 3, in f
  |     raise ExceptionGroup('there were problems', excs)
  | ExceptionGroup: there were problems (2 sub-exceptions)
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
>>> try:
...     f()
... except Exception as e:
...     print(f'caught {type(e)}: {e}')
...
caught <class 'ExceptionGroup'>: there were problems (2 sub-exceptions)
>>>

### python_errors_chunk016

By using except* instead of except , we can selectively
handle only the exceptions in the group that match a certain
type. In the following example, which shows a nested exception
group, each except* clause extracts from the group exceptions
of a certain type while letting all other exceptions propagate to
other clauses and eventually to be reraised.

## test_019 — unanswerable

What exact maximum disk space can a Python virtual environment occupy?
- Expected: State that the answer cannot be determined from the supplied documentation.

Check the entire corpus: no passage should supply the requested answer. Do not confuse an absent answer with a retrieval failure.

## test_020 — unanswerable

What pip version is currently installed on my laptop?
- Expected: State that the answer cannot be determined from the supplied documentation.

Check the entire corpus: no passage should supply the requested answer. Do not confuse an absent answer with a retrieval failure.

## test_021 — unanswerable

Which private package-index URL does our company require?
- Expected: State that the answer cannot be determined from the supplied documentation.

Check the entire corpus: no passage should supply the requested answer. Do not confuse an absent answer with a retrieval failure.

## test_022 — unanswerable

What numerical speedup is guaranteed when loading a cached .pyc module?
- Expected: State that the answer cannot be determined from the supplied documentation.

Check the entire corpus: no passage should supply the requested answer. Do not confuse an absent answer with a retrieval failure.

## test_023 — unanswerable

What maximum number of exception notes does this documentation specify?
- Expected: State that the answer cannot be determined from the supplied documentation.

Check the entire corpus: no passage should supply the requested answer. Do not confuse an absent answer with a retrieval failure.

## test_024 — unanswerable

What is the current latest requests release on PyPI?
- Expected: State that the answer cannot be determined from the supplied documentation.

Check the entire corpus: no passage should supply the requested answer. Do not confuse an absent answer with a retrieval failure.

# Test answer review — assistant proposals

72 distinct answers. Read the rubric before reviewing. All human review fields are initially empty.

## test_001 / budget_900

Which Python version is installed in an environment created by python3.12 -m venv?

Expected: Python 3.12, because venv uses the interpreter that runs the command.

**Generated answer:**

The Python version installed in an environment created by `python3.12 -m venv` is 3.12.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly identifies Python 3.12; the question asks for the version, so a causal explanation is not required.

Borderline: False. Full annotated evidence: True. Output tokens: 28. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

</details>

## test_001 / top_k_2

Which Python version is installed in an environment created by python3.12 -m venv?

Expected: Python 3.12, because venv uses the interpreter that runs the command.

**Generated answer:**

The Python version installed in an environment created by `python3.12 -m venv` is 3.12.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly identifies Python 3.12; the question asks for the version, so a causal explanation is not required.

Borderline: False. Full annotated evidence: True. Output tokens: 28. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

</details>

## test_001 / top_k_8

Which Python version is installed in an environment created by python3.12 -m venv?

Expected: Python 3.12, because venv uses the interpreter that runs the command.

**Generated answer:**

The Python version installed in an environment created by `python3.12 -m venv` is 3.12.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly identifies Python 3.12; the question asks for the version, so a causal explanation is not required.

Borderline: False. Full annotated evidence: True. Output tokens: 28. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_venv_chunk001] 12. Virtual Environments and Packages

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

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_modules_chunk010] Python comes with a library of standard modules, described in a separate
document, the Python Library Reference (“Library Reference” hereafter).  Some
modules are built into the interpreter; these provide access to operations that
are not part of the core of the language but are nevertheless built in, either
for efficiency or to provide access to operating system primitives such as
system calls.  The set of such modules is a configuration option which also
depends on the underlying platform.  For example, the winreg module is only
provided on Windows systems. One particular module deserves some attention: sys , which is built into every Python interpreter.  The variables sys.ps1 and sys.ps2 define the strings used as primary and secondary
prompts:

>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>

These two variables are only defined if the interpreter is in interactive mode.

The variable sys.path is a list of strings that determines the interpreter’s
search path for modules. It is initialized to a default path taken from the
environment variable PYTHONPATH , or from a built-in default if PYTHONPATH is not set.  You can modify it using standard list
operations:

>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')

6.3. The dir() Function

</details>

## test_002 / budget_900

How do I install exactly version 2.6.0 of requests using pip?

Expected: Run python -m pip install requests==2.6.0.

**Generated answer:**

To install exactly version 2.6.0 of requests using pip, use the following command:

```bash
python -m pip install requests==2.6.0
```

This command specifies the exact version number required, ensuring that the correct version of the `requests` library is installed in your virtual environment.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Gives the correct exact-version pip installation command.

Borderline: False. Full annotated evidence: True. Output tokens: 66. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

</details>

## test_002 / top_k_2

How do I install exactly version 2.6.0 of requests using pip?

Expected: Run python -m pip install requests==2.6.0.

**Generated answer:**

To install exactly version 2.6.0 of requests using pip, use the following command:

```bash
python -m pip install requests==2.6.0
```

This command specifies the exact version number required.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Gives the correct exact-version pip installation command.

Borderline: False. Full annotated evidence: True. Output tokens: 48. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

</details>

## test_002 / top_k_8

How do I install exactly version 2.6.0 of requests using pip?

Expected: Run python -m pip install requests==2.6.0.

**Generated answer:**

Use the following command to install version 2.6.0 of requests:

```bash
python -m pip install requests==2.6.0
```

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Gives the correct exact-version pip installation command.

Borderline: False. Full annotated evidence: True. Output tokens: 34. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_venv_chunk001] 12. Virtual Environments and Packages

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

[python_modules_chunk005] >>> from fibo import *
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

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

</details>

## test_003 / budget_900

What does pip do if I repeat the installation command for an already installed requested version?

Expected: It notices that the requested version is installed and does nothing.

**Generated answer:**

If you repeat the installation command for an already installed requested version, pip will notice that the requested version is already installed and do nothing.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly states that pip notices the requested version is installed and does nothing.

Borderline: False. Full annotated evidence: True. Output tokens: 28. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

</details>

## test_003 / top_k_2

What does pip do if I repeat the installation command for an already installed requested version?

Expected: It notices that the requested version is installed and does nothing.

**Generated answer:**

If you repeat the installation command for an already installed requested version with pip, it will notice that the specified version is already installed and do nothing.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly states that pip notices the requested version is installed and does nothing.

Borderline: False. Full annotated evidence: True. Output tokens: 30. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

</details>

## test_003 / top_k_8

What does pip do if I repeat the installation command for an already installed requested version?

Expected: It notices that the requested version is installed and does nothing.

**Generated answer:**

If you repeat the installation command for an already installed requested version, pip will notice that the requested version is already installed and do nothing.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly states that pip notices the requested version is installed and does nothing.

Borderline: False. Full annotated evidence: True. Output tokens: 28. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_venv_chunk001] 12. Virtual Environments and Packages

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

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

</details>

## test_004 / budget_900

How can another developer install the packages listed in requirements.txt?

Expected: Run python -m pip install -r requirements.txt.

**Generated answer:**

Another developer can install the packages listed in requirements.txt by running the command `python -m pip install -r requirements.txt`. This command reads the contents of the requirements.txt file, installs each package specified there, and updates the system's package index accordingly.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Correct command, but incorrectly adds that pip updates the system package index.

Borderline: False. Full annotated evidence: True. Output tokens: 52. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_venv_chunk001] 12. Virtual Environments and Packages

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

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

</details>

## test_004 / top_k_2

How can another developer install the packages listed in requirements.txt?

Expected: Run python -m pip install -r requirements.txt.

**Generated answer:**

Another developer can install the packages listed in requirements.txt by running the following command within their virtual environment:

```bash
python -m pip install -r requirements.txt
```

This command reads the `requirements.txt` file, installs each package specified there, and ensures that they are compatible with the current Python version used in the virtual environment.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Correct command, but adds an unsupported guarantee that installation ensures compatibility with the current Python version; material overclaim.

Borderline: True. Full annotated evidence: True. Output tokens: 69. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_venv_chunk001] 12. Virtual Environments and Packages

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

</details>

## test_004 / top_k_8

How can another developer install the packages listed in requirements.txt?

Expected: Run python -m pip install -r requirements.txt.

**Generated answer:**

Another developer can install the packages listed in requirements.txt by running the following command in the terminal:

```bash
(tutorial-env) $ python -m pip install -r requirements.txt
```

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correct install -r command; treats the displayed shell prompt as notation, not part of the command.

Borderline: False. Full annotated evidence: True. Output tokens: 39. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_venv_chunk001] 12. Virtual Environments and Packages

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

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_modules_chunk007] If the module is imported, the code is not run:

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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_errors_chunk014] Some objects define standard clean-up actions to be undertaken when the object
is no longer needed, regardless of whether or not the operation using the object
succeeded or failed. Look at the following example, which tries to open a file
and print its contents to the screen.

for line in open("myfile.txt"):
    print(line, end="")

The problem with this code is that it leaves the file open for an indeterminate
amount of time after this part of the code has finished executing.
This is not an issue in simple scripts, but can be a problem for larger
applications. The with statement allows objects like files to be
used in a way that ensures they are always cleaned up promptly and correctly.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

After the statement is executed, the file f is always closed, even if a
problem was encountered while processing the lines. Objects which, like files,
provide predefined clean-up actions will indicate this in their documentation.

8.9. Raising and Handling Multiple Unrelated Exceptions

There are situations where it is necessary to report several exceptions that
have occurred. This is often the case in concurrency frameworks, when several
tasks may have failed in parallel, but there are also other use cases where
it is desirable to continue execution and collect multiple errors rather than
raise the first exception.

[python_errors_chunk009] >>> try:
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

</details>

## test_005 / budget_900

Does import fibo directly add fib and fib2 to the current namespace?

Expected: No. It adds the module name fibo; access its functions through that module.

**Generated answer:**

No, import fibo does not add fib and fib2 to the current namespace. Only the module name fibo is added to the current namespace.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly says only the module name fibo is introduced; sufficient namespace explanation.

Borderline: False. Full annotated evidence: True. Output tokens: 31. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk002] # Fibonacci numbers module

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

[python_modules_chunk004] Each module has its own private namespace, which is used as the global namespace
by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user’s global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation used to
refer to its functions, modname.itemname .

Modules can import other modules.  It is customary but not required to place all import statements at the beginning of a module (or script, for that
matter).  The imported module names, if placed at the top level of a module
(outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a
module directly into the importing module’s namespace.  For example:

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

[python_modules_chunk003] >>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'

If you intend to use a function often you can assign it to a local name:

>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

6.1. More on Modules

A module can contain executable statements as well as function definitions.
These statements are intended to initialize the module. They are executed only
the first time the module name is encountered in an import statement. [ 1 ] (They are also run if the file is executed as a script.)

[python_modules_chunk022] Note that relative imports are based on the name of the current module’s package.
Since the main module does not have a package, modules intended for use
as the main module of a Python application must always use absolute imports.

Footnotes

In fact function definitions are also ‘statements’ that are ‘executed’; the
execution of a module-level function definition adds the function name to
the module’s global namespace.

</details>

## test_005 / top_k_2

Does import fibo directly add fib and fib2 to the current namespace?

Expected: No. It adds the module name fibo; access its functions through that module.

**Generated answer:**

No, import fibo does not add fib and fib2 to the current namespace; it only adds the module name fibo there.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly says only the module name fibo is introduced; sufficient namespace explanation.

Borderline: False. Full annotated evidence: True. Output tokens: 28. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk002] # Fibonacci numbers module

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

[python_modules_chunk004] Each module has its own private namespace, which is used as the global namespace
by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user’s global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation used to
refer to its functions, modname.itemname .

Modules can import other modules.  It is customary but not required to place all import statements at the beginning of a module (or script, for that
matter).  The imported module names, if placed at the top level of a module
(outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a
module directly into the importing module’s namespace.  For example:

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

</details>

## test_005 / top_k_8

Does import fibo directly add fib and fib2 to the current namespace?

Expected: No. It adds the module name fibo; access its functions through that module.

**Generated answer:**

No, import fibo does not add fib and fib2 to the current namespace.

**Proposed correctness:** 1 | **Grounding:** supported | **Abstention:** None

**Reason:** Correct no, but omits that only the module name is introduced and functions are accessed through it.

Borderline: True. Full annotated evidence: True. Output tokens: 18. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk002] # Fibonacci numbers module

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

[python_modules_chunk004] Each module has its own private namespace, which is used as the global namespace
by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user’s global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation used to
refer to its functions, modname.itemname .

Modules can import other modules.  It is customary but not required to place all import statements at the beginning of a module (or script, for that
matter).  The imported module names, if placed at the top level of a module
(outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a
module directly into the importing module’s namespace.  For example:

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

[python_modules_chunk003] >>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'

If you intend to use a function often you can assign it to a local name:

>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

6.1. More on Modules

A module can contain executable statements as well as function definitions.
These statements are intended to initialize the module. They are executed only
the first time the module name is encountered in an import statement. [ 1 ] (They are also run if the file is executed as a script.)

[python_modules_chunk005] >>> from fibo import *
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

[python_modules_chunk013] _finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']

Without arguments, dir() lists the names you have defined currently:

>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

Note that it lists all types of names: variables, modules, functions, etc.

dir() does not list the names of built-in functions and variables.  If you
want a list of those, they are defined in the standard module builtins :

[python_modules_chunk020] Be aware that submodules might become shadowed by locally defined names. For
example, if you added a reverse function to the sound/effects/__init__.py file, the from sound.effects import * would only import the two submodules echo and surround , but not the reverse submodule, because it is shadowed by the locally defined reverse function:

__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'

If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package sound.effects into the
current namespace; it only ensures that the package sound.effects has
been imported (possibly running any initialization code in __init__.py )
and then imports whatever names are defined in the package.  This includes any
names defined (and submodules explicitly loaded) by __init__.py .  It
also includes any submodules of the package that were explicitly loaded by
previous import statements.  Consider this code:

import sound.effects.echo
import sound.effects.surround
from sound.effects import *

[python_modules_chunk021] In this example, the echo and surround modules are imported in the
current namespace because they are defined in the sound.effects package
when the from...import statement is executed.  (This also works when __all__ is defined.)

Although certain modules are designed to export only names that follow certain
patterns when you use import * , it is still considered bad practice in
production code.

Remember, there is nothing wrong with using from package import specific_submodule !  In fact, this is the recommended notation unless the
importing module needs to use submodules with the same name from different
packages.

6.4.2. Intra-package References

When packages are structured into subpackages (as with the sound package
in the example), you can use absolute imports to refer to submodules of siblings
packages.  For example, if the module sound.filters.vocoder needs to use
the echo module in the sound.effects package, it can use from sound.effects import echo .

You can also write relative imports, with the from module import name form
of import statement.  These imports use leading dots to indicate the current and
parent packages involved in the relative import.  From the surround module for example, you might use:

from . import echo
from .. import formats
from ..filters import equalizer

[python_modules_chunk022] Note that relative imports are based on the name of the current module’s package.
Since the main module does not have a package, modules intended for use
as the main module of a Python application must always use absolute imports.

Footnotes

In fact function definitions are also ‘statements’ that are ‘executed’; the
execution of a module-level function definition adds the function name to
the module’s global namespace.

</details>

## test_006 / budget_900

How can I reload a changed module during an interactive interpreter session?

Expected: Use importlib.reload(modulename), after importing importlib.

**Generated answer:**

You can reload a changed module during an interactive interpreter session by using `importlib.reload()` followed by importing the module again. For example, if you have modified the `fibo` module and want to re-import it after saving changes, you would first reload the module like so:

```python
import importlib
importlib.reload(fibo_module)
```

Then, you can import and use

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Adds an unnecessary re-import and uses an unexplained fibo_module name in the example; truncated.

Borderline: False. Full annotated evidence: True. Output tokens: 80. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk006] >>> from fibo import fib as fibonacci
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

[python_modules_chunk001] 6. Modules

If you quit from the Python interpreter and enter it again, the definitions you
have made (functions and variables) are lost. Therefore, if you want to write a
somewhat longer program, you are better off using a text editor to prepare the
input for the interpreter and running it with that file as input instead.  This
is known as creating a script .  As your program gets longer, you may want to
split it into several files for easier maintenance.  You may also want to use a
handy function that you’ve written in several programs without copying its
definition into each program.

To support this, Python has a way to put definitions in a file and use them in a
script or in an interactive instance of the interpreter. Such a file is called a module ; definitions from a module can be imported into other modules or into
the main module (the collection of variables that you have access to in a
script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements.  The file name
is the module name with the suffix .py appended.  Within a module, the
module’s name (as a string) is available as the value of the global variable __name__ .  For instance, use your favorite text editor to create a file
called fibo.py in the current directory with the following contents:

</details>

## test_006 / top_k_2

How can I reload a changed module during an interactive interpreter session?

Expected: Use importlib.reload(modulename), after importing importlib.

**Generated answer:**

Use importlib.reload(module_name)

**Proposed correctness:** 1 | **Grounding:** supported | **Abstention:** None

**Reason:** Correct reload call, but omits the prerequisite import importlib specified by the reference.

Borderline: True. Full annotated evidence: True. Output tokens: 8. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk006] >>> from fibo import fib as fibonacci
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

</details>

## test_006 / top_k_8

How can I reload a changed module during an interactive interpreter session?

Expected: Use importlib.reload(modulename), after importing importlib.

**Generated answer:**

You can reload a changed module during an interactive interpreter session by using `importlib.reload()` followed by re-importing the module. For example, if you've modified the `fibonacci` function in the `fibo` module, you could reload it like this:

```python
import importlib
importlib.reload(fibo)
```

After reloading the module, any changes you made to the

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Gives importlib.reload(fibo), but incorrectly requires a subsequent re-import and trails off at the token cap.

Borderline: False. Full annotated evidence: True. Output tokens: 80. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk006] >>> from fibo import fib as fibonacci
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

[python_modules_chunk001] 6. Modules

If you quit from the Python interpreter and enter it again, the definitions you
have made (functions and variables) are lost. Therefore, if you want to write a
somewhat longer program, you are better off using a text editor to prepare the
input for the interpreter and running it with that file as input instead.  This
is known as creating a script .  As your program gets longer, you may want to
split it into several files for easier maintenance.  You may also want to use a
handy function that you’ve written in several programs without copying its
definition into each program.

To support this, Python has a way to put definitions in a file and use them in a
script or in an interactive instance of the interpreter. Such a file is called a module ; definitions from a module can be imported into other modules or into
the main module (the collection of variables that you have access to in a
script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements.  The file name
is the module name with the suffix .py appended.  Within a module, the
module’s name (as a string) is available as the value of the global variable __name__ .  For instance, use your favorite text editor to create a file
called fibo.py in the current directory with the following contents:

[python_modules_chunk010] Python comes with a library of standard modules, described in a separate
document, the Python Library Reference (“Library Reference” hereafter).  Some
modules are built into the interpreter; these provide access to operations that
are not part of the core of the language but are nevertheless built in, either
for efficiency or to provide access to operating system primitives such as
system calls.  The set of such modules is a configuration option which also
depends on the underlying platform.  For example, the winreg module is only
provided on Windows systems. One particular module deserves some attention: sys , which is built into every Python interpreter.  The variables sys.ps1 and sys.ps2 define the strings used as primary and secondary
prompts:

>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>

These two variables are only defined if the interpreter is in interactive mode.

The variable sys.path is a list of strings that determines the interpreter’s
search path for modules. It is initialized to a default path taken from the
environment variable PYTHONPATH , or from a built-in default if PYTHONPATH is not set.  You can modify it using standard list
operations:

>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')

6.3. The dir() Function

[python_modules_chunk005] >>> from fibo import *
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

[python_errors_chunk020] >>> def f():
...     raise OSError('operation failed')
...
>>> excs = []
>>> for i in range(3):
...     try:
...         f()
...     except Exception as e:
...         e.add_note(f'Happened in Iteration {i+1}')
...         excs.append(e)
...
>>> raise ExceptionGroup('We have some problems', excs)
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |     raise ExceptionGroup('We have some problems', excs)
  | ExceptionGroup: We have some problems (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration 1
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration

[python_modules_chunk002] # Fibonacci numbers module

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

[python_modules_chunk007] If the module is imported, the code is not run:

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

</details>

## test_007 / budget_900

Where does Python cache compiled modules, and how does it detect stale cached code?

Expected: It stores compiled modules in __pycache__ using version-tagged .pyc names. It checks the source modification date against the compiled version.

**Generated answer:**

Python caches compiled modules in the `__pycache__` directory under names like `module.version.pyc`, where `version` encodes the format of the compiled file. It detects staleness by comparing the modification dates of the source code with the compiled versions.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correct cache directory, version-tagged filename and source modification comparison.

Borderline: False. Full annotated evidence: True. Output tokens: 54. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

</details>

## test_007 / top_k_2

Where does Python cache compiled modules, and how does it detect stale cached code?

Expected: It stores compiled modules in __pycache__ using version-tagged .pyc names. It checks the source modification date against the compiled version.

**Generated answer:**

Python caches compiled modules in the `__pycache__` directory under names like `module.version.pyc`, where `version` encodes the format of the compiled file. It detects staleness by comparing the modification dates of the source code against the compiled versions.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correct cache directory, version-tagged filename and source modification comparison.

Borderline: False. Full annotated evidence: True. Output tokens: 54. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

</details>

## test_007 / top_k_8

Where does Python cache compiled modules, and how does it detect stale cached code?

Expected: It stores compiled modules in __pycache__ using version-tagged .pyc names. It checks the source modification date against the compiled version.

**Generated answer:**

Python caches compiled modules in the `__pycache__` directory under the name `module.version`. It detects stale cached code by checking the modification date of the source against the compiled version.

**Proposed correctness:** 1 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Correct directory and stale-source check, but explicitly gives module.version without the .pyc suffix.

Borderline: False. Full annotated evidence: True. Output tokens: 39. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

[python_modules_chunk020] Be aware that submodules might become shadowed by locally defined names. For
example, if you added a reverse function to the sound/effects/__init__.py file, the from sound.effects import * would only import the two submodules echo and surround , but not the reverse submodule, because it is shadowed by the locally defined reverse function:

__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'

If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package sound.effects into the
current namespace; it only ensures that the package sound.effects has
been imported (possibly running any initialization code in __init__.py )
and then imports whatever names are defined in the package.  This includes any
names defined (and submodules explicitly loaded) by __init__.py .  It
also includes any submodules of the package that were explicitly loaded by
previous import statements.  Consider this code:

import sound.effects.echo
import sound.effects.surround
from sound.effects import *

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_errors_chunk014] Some objects define standard clean-up actions to be undertaken when the object
is no longer needed, regardless of whether or not the operation using the object
succeeded or failed. Look at the following example, which tries to open a file
and print its contents to the screen.

for line in open("myfile.txt"):
    print(line, end="")

The problem with this code is that it leaves the file open for an indeterminate
amount of time after this part of the code has finished executing.
This is not an issue in simple scripts, but can be a problem for larger
applications. The with statement allows objects like files to be
used in a way that ensures they are always cleaned up promptly and correctly.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

After the statement is executed, the file f is always closed, even if a
problem was encountered while processing the lines. Objects which, like files,
provide predefined clean-up actions will indicate this in their documentation.

8.9. Raising and Handling Multiple Unrelated Exceptions

There are situations where it is necessary to report several exceptions that
have occurred. This is often the case in concurrency frameworks, when several
tasks may have failed in parallel, but there are also other use cases where
it is desirable to continue execution and collect multiple errors rather than
raise the first exception.

[python_modules_chunk013] _finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']

Without arguments, dir() lists the names you have defined currently:

>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

Note that it lists all types of names: variables, modules, functions, etc.

dir() does not list the names of built-in functions and variables.  If you
want a list of those, they are defined in the standard module builtins :

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

</details>

## test_008 / budget_900

Does reading a program from a .pyc file make its execution faster than reading it from .py?

Expected: No. Compiled files load faster, but the program itself does not run faster for that reason.

**Generated answer:**

No, reading a program from a .pyc file makes its execution slower compared to reading it from a .py file.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Incorrectly claims slower execution; the reference says loading is faster but execution is not.

Borderline: False. Full annotated evidence: True. Output tokens: 26. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_errors_chunk004] >>> while True:
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

[python_modules_chunk017] sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.

The __init__.py files are required to make Python treat directories
containing the file as packages (unless using a namespace package , a
relatively advanced feature). This prevents directories with a common name,
such as string , from unintentionally hiding valid modules that occur later
on the module search path. In the simplest case, __init__.py can just be
an empty file, but it can also execute initialization code for the package or
set the __all__ variable, described later.

Users of the package can import individual modules from the package, for
example:

import sound.effects.echo

This loads the submodule sound.effects.echo .  It must be referenced with
its full name.

</details>

## test_008 / top_k_2

Does reading a program from a .pyc file make its execution faster than reading it from .py?

Expected: No. Compiled files load faster, but the program itself does not run faster for that reason.

**Generated answer:**

No, reading a program from a .pyc file makes its execution slower compared to reading it from a .py file.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Incorrectly claims slower execution; the reference says loading is faster but execution is not.

Borderline: False. Full annotated evidence: True. Output tokens: 26. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_errors_chunk004] >>> while True:
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

</details>

## test_008 / top_k_8

Does reading a program from a .pyc file make its execution faster than reading it from .py?

Expected: No. Compiled files load faster, but the program itself does not run faster for that reason.

**Generated answer:**

No, reading a program from a .pyc file makes its execution faster than reading it from a .py file.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Says No but then asserts faster execution, contradicting the reference distinction between loading and running.

Borderline: False. Full annotated evidence: True. Output tokens: 25. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_errors_chunk004] >>> while True:
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

[python_modules_chunk017] sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.

The __init__.py files are required to make Python treat directories
containing the file as packages (unless using a namespace package , a
relatively advanced feature). This prevents directories with a common name,
such as string , from unintentionally hiding valid modules that occur later
on the module search path. In the simplest case, __init__.py can just be
an empty file, but it can also execute initialization code for the package or
set the __all__ variable, described later.

Users of the package can import individual modules from the package, for
example:

import sound.effects.echo

This loads the submodule sound.effects.echo .  It must be referenced with
its full name.

[python_modules_chunk001] 6. Modules

If you quit from the Python interpreter and enter it again, the definitions you
have made (functions and variables) are lost. Therefore, if you want to write a
somewhat longer program, you are better off using a text editor to prepare the
input for the interpreter and running it with that file as input instead.  This
is known as creating a script .  As your program gets longer, you may want to
split it into several files for easier maintenance.  You may also want to use a
handy function that you’ve written in several programs without copying its
definition into each program.

To support this, Python has a way to put definitions in a file and use them in a
script or in an interactive instance of the interpreter. Such a file is called a module ; definitions from a module can be imported into other modules or into
the main module (the collection of variables that you have access to in a
script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements.  The file name
is the module name with the suffix .py appended.  Within a module, the
module’s name (as a string) is available as the value of the global variable __name__ .  For instance, use your favorite text editor to create a file
called fibo.py in the current directory with the following contents:

[python_errors_chunk014] Some objects define standard clean-up actions to be undertaken when the object
is no longer needed, regardless of whether or not the operation using the object
succeeded or failed. Look at the following example, which tries to open a file
and print its contents to the screen.

for line in open("myfile.txt"):
    print(line, end="")

The problem with this code is that it leaves the file open for an indeterminate
amount of time after this part of the code has finished executing.
This is not an issue in simple scripts, but can be a problem for larger
applications. The with statement allows objects like files to be
used in a way that ensures they are always cleaned up promptly and correctly.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

After the statement is executed, the file f is always closed, even if a
problem was encountered while processing the lines. Objects which, like files,
provide predefined clean-up actions will indicate this in their documentation.

8.9. Raising and Handling Multiple Unrelated Exceptions

There are situations where it is necessary to report several exceptions that
have occurred. This is often the case in concurrency frameworks, when several
tasks may have failed in parallel, but there are also other use cases where
it is desirable to continue execution and collect multiple errors rather than
raise the first exception.

[python_modules_chunk006] >>> from fibo import fib as fibonacci
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

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_venv_chunk007] pip has many more options.  Consult the Installing Python modules guide for complete documentation for pip .  When you’ve written
a package and want to make it available on the Python Package Index,
consult the Python packaging user guide .

</details>

## test_009 / budget_900

What happens if an exception in a try clause matches none of its except clauses?

Expected: It propagates to outer handlers; if none handles it, execution stops with an error.

**Generated answer:**

An exception in a try clause that does not match any except clause causes the program to stop executing at the point where the except clause would have been executed. This results in an unhandled exception, leading to an error message indicating that there was an uncaught exception.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** States immediate termination at an except position instead of propagation to outer handlers.

Borderline: False. Full annotated evidence: True. Output tokens: 54. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk005] A class in an except clause matches exceptions which are instances of the
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

[python_errors_chunk004] >>> while True:
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

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

</details>

## test_009 / top_k_2

What happens if an exception in a try clause matches none of its except clauses?

Expected: It propagates to outer handlers; if none handles it, execution stops with an error.

**Generated answer:**

An exception in a try clause that does not match any except clause causes the program to stop executing with an error message.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** States unconditional termination after no local match, omitting the possible outer handler; material condition is wrong.

Borderline: False. Full annotated evidence: True. Output tokens: 25. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk005] A class in an except clause matches exceptions which are instances of the
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

[python_errors_chunk004] >>> while True:
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

</details>

## test_009 / top_k_8

What happens if an exception in a try clause matches none of its except clauses?

Expected: It propagates to outer handlers; if none handles it, execution stops with an error.

**Generated answer:**

If an exception in a try clause matches none of its except clauses, the exception is propagated up through the call stack until caught by some higher-level except clause or the program terminates normally.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Mentions propagation but incorrectly describes an unhandled exception as normal termination.

Borderline: False. Full annotated evidence: True. Output tokens: 38. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk005] A class in an except clause matches exceptions which are instances of the
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

[python_errors_chunk004] >>> while True:
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

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_errors_chunk016] By using except* instead of except , we can selectively
handle only the exceptions in the group that match a certain
type. In the following example, which shows a nested exception
group, each except* clause extracts from the group exceptions
of a certain type while letting all other exceptions propagate to
other clauses and eventually to be reraised.

[python_errors_chunk011] Exception classes can be defined which do anything any other class can do, but
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

[python_errors_chunk009] >>> try:
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

[python_errors_chunk012] An exception could occur during execution of an except or else clause. Again, the exception is re-raised after
the finally clause has been executed.

If the finally clause executes a break , continue or return statement, exceptions are not
re-raised.

If the try statement reaches a break , continue or return statement, the finally clause will execute just prior to the break , continue or return statement’s execution.

If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the
value from the try clause’s return statement.

For example:

>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False

A more complicated example:

[python_errors_chunk010] >>> def func():
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

</details>

## test_010 / budget_900

If several except clauses could match an exception, which one runs?

Expected: The first matching except clause runs.

**Generated answer:**

Only the first matching except clause runs.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly identifies the first matching handler.

Borderline: False. Full annotated evidence: True. Output tokens: 9. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk016] By using except* instead of except , we can selectively
handle only the exceptions in the group that match a certain
type. In the following example, which shows a nested exception
group, each except* clause extracts from the group exceptions
of a certain type while letting all other exceptions propagate to
other clauses and eventually to be reraised.

[python_errors_chunk005] A class in an except clause matches exceptions which are instances of the
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

[python_errors_chunk004] >>> while True:
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

[python_errors_chunk012] An exception could occur during execution of an except or else clause. Again, the exception is re-raised after
the finally clause has been executed.

If the finally clause executes a break , continue or return statement, exceptions are not
re-raised.

If the try statement reaches a break , continue or return statement, the finally clause will execute just prior to the break , continue or return statement’s execution.

If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the
value from the try clause’s return statement.

For example:

>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False

A more complicated example:

</details>

## test_010 / top_k_2

If several except clauses could match an exception, which one runs?

Expected: The first matching except clause runs.

**Generated answer:**

If several except clauses could match an exception, the one with the most specific exception type listed runs. This ensures that only the relevant exceptions are handled, preventing propagation to unrelated ones.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Incorrectly selects the most specific type rather than the first matching handler.

Borderline: False. Full annotated evidence: True. Output tokens: 37. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk016] By using except* instead of except , we can selectively
handle only the exceptions in the group that match a certain
type. In the following example, which shows a nested exception
group, each except* clause extracts from the group exceptions
of a certain type while letting all other exceptions propagate to
other clauses and eventually to be reraised.

[python_errors_chunk005] A class in an except clause matches exceptions which are instances of the
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

</details>

## test_010 / top_k_8

If several except clauses could match an exception, which one runs?

Expected: The first matching except clause runs.

**Generated answer:**

The Python documentation states that "At most one handler will be executed." So, among several except clauses that could match an exception, only one will run.

**Proposed correctness:** 1 | **Grounding:** supported | **Abstention:** None

**Reason:** Says at most one handler runs but does not identify the first matching handler.

Borderline: False. Full annotated evidence: True. Output tokens: 32. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk016] By using except* instead of except , we can selectively
handle only the exceptions in the group that match a certain
type. In the following example, which shows a nested exception
group, each except* clause extracts from the group exceptions
of a certain type while letting all other exceptions propagate to
other clauses and eventually to be reraised.

[python_errors_chunk005] A class in an except clause matches exceptions which are instances of the
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

[python_errors_chunk004] >>> while True:
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

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_errors_chunk012] An exception could occur during execution of an except or else clause. Again, the exception is re-raised after
the finally clause has been executed.

If the finally clause executes a break , continue or return statement, exceptions are not
re-raised.

If the try statement reaches a break , continue or return statement, the finally clause will execute just prior to the break , continue or return statement’s execution.

If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the
value from the try clause’s return statement.

For example:

>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False

A more complicated example:

[python_errors_chunk011] Exception classes can be defined which do anything any other class can do, but
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

[python_modules_chunk019] Now what happens when the user writes from sound.effects import * ?  Ideally,
one would hope that this somehow goes out to the filesystem, finds which
submodules are present in the package, and imports them all.  This could take a
long time and importing sub-modules might have unwanted side-effects that should
only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the
package.  The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__ , it is taken to be the
list of module names that should be imported when from package import * is
encountered.  It is up to the package author to keep this list up-to-date when a
new version of the package is released.  Package authors may also decide not to
support it, if they don’t see a use for importing * from their package.  For
example, the file sound/effects/__init__.py could contain the following
code:

__all__ = ["echo", "surround", "reverse"]

This would mean that from sound.effects import * would import the three
named submodules of the sound.effects package.

[python_errors_chunk014] Some objects define standard clean-up actions to be undertaken when the object
is no longer needed, regardless of whether or not the operation using the object
succeeded or failed. Look at the following example, which tries to open a file
and print its contents to the screen.

for line in open("myfile.txt"):
    print(line, end="")

The problem with this code is that it leaves the file open for an indeterminate
amount of time after this part of the code has finished executing.
This is not an issue in simple scripts, but can be a problem for larger
applications. The with statement allows objects like files to be
used in a way that ensures they are always cleaned up promptly and correctly.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

After the statement is executed, the file f is always closed, even if a
problem was encountered while processing the lines. Objects which, like files,
provide predefined clean-up actions will indicate this in their documentation.

8.9. Raising and Handling Multiple Unrelated Exceptions

There are situations where it is necessary to report several exceptions that
have occurred. This is often the case in concurrency frameworks, when several
tasks may have failed in parallel, but there are also other use cases where
it is desirable to continue execution and collect multiple errors rather than
raise the first exception.

</details>

## test_011 / budget_900

Why put successful follow-up work in a try statement's else clause?

Expected: It runs when the try clause raises no exception. It avoids accidentally catching exceptions from follow-up work in the original handlers.

**Generated answer:**

Put successful follow-up work in a try statement's else clause so that it can be executed even if the try block raises an exception. This avoids accidentally catching an exception that wasn't raised by the code being protected by the try ... except statement.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Incorrectly states else runs even if try raises an exception.

Borderline: False. Full annotated evidence: True. Output tokens: 50. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_errors_chunk013] >>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    divide("2", "1")
    ~~~~~~^^^^^^^^^^
  File "<stdin>", line 3, in divide
    result = x / y
             ~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'str'

As you can see, the finally clause is executed in any event.  The TypeError raised by dividing two strings is not handled by the except clause and therefore re-raised after the finally clause has been executed.

In real world applications, the finally clause is useful for
releasing external resources (such as files or network connections), regardless
of whether the use of the resource was successful.

8.8. Predefined Clean-up Actions

[python_errors_chunk012] An exception could occur during execution of an except or else clause. Again, the exception is re-raised after
the finally clause has been executed.

If the finally clause executes a break , continue or return statement, exceptions are not
re-raised.

If the try statement reaches a break , continue or return statement, the finally clause will execute just prior to the break , continue or return statement’s execution.

If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the
value from the try clause’s return statement.

For example:

>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False

A more complicated example:

</details>

## test_011 / top_k_2

Why put successful follow-up work in a try statement's else clause?

Expected: It runs when the try clause raises no exception. It avoids accidentally catching exceptions from follow-up work in the original handlers.

**Generated answer:**

Put successful follow-up work in a try statement's else clause so that it will execute even if an exception occurs within the try block. This prevents accidentally catching an exception that wasn't raised by the code being protected by the try ... except statement.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Incorrectly states else runs even if try raises an exception.

Borderline: False. Full annotated evidence: True. Output tokens: 50. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_errors_chunk013] >>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    divide("2", "1")
    ~~~~~~^^^^^^^^^^
  File "<stdin>", line 3, in divide
    result = x / y
             ~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'str'

As you can see, the finally clause is executed in any event.  The TypeError raised by dividing two strings is not handled by the except clause and therefore re-raised after the finally clause has been executed.

In real world applications, the finally clause is useful for
releasing external resources (such as files or network connections), regardless
of whether the use of the resource was successful.

8.8. Predefined Clean-up Actions

</details>

## test_011 / top_k_8

Why put successful follow-up work in a try statement's else clause?

Expected: It runs when the try clause raises no exception. It avoids accidentally catching exceptions from follow-up work in the original handlers.

**Generated answer:**

Put successful follow-up work in a try statement's else clause so that it is executed if the try clause does not raise an exception. This avoids accidentally catching an exception that wasn't raised by the code being protected by the try-except statement.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly explains the no-exception condition and avoiding accidental catches from follow-up work.

Borderline: False. Full annotated evidence: True. Output tokens: 50. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_errors_chunk013] >>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    divide("2", "1")
    ~~~~~~^^^^^^^^^^
  File "<stdin>", line 3, in divide
    result = x / y
             ~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'str'

As you can see, the finally clause is executed in any event.  The TypeError raised by dividing two strings is not handled by the except clause and therefore re-raised after the finally clause has been executed.

In real world applications, the finally clause is useful for
releasing external resources (such as files or network connections), regardless
of whether the use of the resource was successful.

8.8. Predefined Clean-up Actions

[python_errors_chunk012] An exception could occur during execution of an except or else clause. Again, the exception is re-raised after
the finally clause has been executed.

If the finally clause executes a break , continue or return statement, exceptions are not
re-raised.

If the try statement reaches a break , continue or return statement, the finally clause will execute just prior to the break , continue or return statement’s execution.

If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the
value from the try clause’s return statement.

For example:

>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False

A more complicated example:

[python_errors_chunk011] Exception classes can be defined which do anything any other class can do, but
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

[python_errors_chunk004] >>> while True:
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

[python_errors_chunk014] Some objects define standard clean-up actions to be undertaken when the object
is no longer needed, regardless of whether or not the operation using the object
succeeded or failed. Look at the following example, which tries to open a file
and print its contents to the screen.

for line in open("myfile.txt"):
    print(line, end="")

The problem with this code is that it leaves the file open for an indeterminate
amount of time after this part of the code has finished executing.
This is not an issue in simple scripts, but can be a problem for larger
applications. The with statement allows objects like files to be
used in a way that ensures they are always cleaned up promptly and correctly.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

After the statement is executed, the file f is always closed, even if a
problem was encountered while processing the lines. Objects which, like files,
provide predefined clean-up actions will indicate this in their documentation.

8.9. Raising and Handling Multiple Unrelated Exceptions

There are situations where it is necessary to report several exceptions that
have occurred. This is often the case in concurrency frameworks, when several
tasks may have failed in parallel, but there are also other use cases where
it is desirable to continue execution and collect multiple errors rather than
raise the first exception.

[python_errors_chunk005] A class in an except clause matches exceptions which are instances of the
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

[python_modules_chunk001] 6. Modules

If you quit from the Python interpreter and enter it again, the definitions you
have made (functions and variables) are lost. Therefore, if you want to write a
somewhat longer program, you are better off using a text editor to prepare the
input for the interpreter and running it with that file as input instead.  This
is known as creating a script .  As your program gets longer, you may want to
split it into several files for easier maintenance.  You may also want to use a
handy function that you’ve written in several programs without copying its
definition into each program.

To support this, Python has a way to put definitions in a file and use them in a
script or in an interactive instance of the interpreter. Such a file is called a module ; definitions from a module can be imported into other modules or into
the main module (the collection of variables that you have access to in a
script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements.  The file name
is the module name with the suffix .py appended.  Within a module, the
module’s name (as a string) is available as the value of the global variable __name__ .  For instance, use your favorite text editor to create a file
called fibo.py in the current directory with the following contents:

</details>

## test_012 / budget_900

How can I add explanatory notes to a caught exception, and where are those notes displayed?

Expected: Call add_note with a string. The standard traceback displays the notes after the exception in insertion order.

**Generated answer:**

You can add explanatory notes to a caught exception by calling the `add_note` method on the exception object. These notes are appended to the exception's notes list and included in the traceback output. The standard traceback rendering includes all notes added to the exception after its creation.

**Proposed correctness:** 1 | **Grounding:** supported | **Abstention:** None

**Reason:** Identifies add_note and traceback display, but does not describe insertion order or placement after the exception.

Borderline: False. Full annotated evidence: True. Output tokens: 55. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk018] Note that the exceptions nested in an exception group must be instances,
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

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

[python_errors_chunk019] For example, when collecting exceptions into an exception group, we may want
to add context information for the individual errors. In the following each
exception in the group has a note indicating when this error has occurred.

</details>

## test_012 / top_k_2

How can I add explanatory notes to a caught exception, and where are those notes displayed?

Expected: Call add_note with a string. The standard traceback displays the notes after the exception in insertion order.

**Generated answer:**

You can add explanatory notes to a caught exception by calling the `add_note` method on the exception object. These notes will be included in the exception's notes list, which is appended to the standard traceback rendering.

**Proposed correctness:** 1 | **Grounding:** supported | **Abstention:** None

**Reason:** Identifies add_note and traceback display, but omits the string argument and insertion order after the exception.

Borderline: False. Full annotated evidence: True. Output tokens: 44. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk018] Note that the exceptions nested in an exception group must be instances,
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

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

</details>

## test_012 / top_k_8

How can I add explanatory notes to a caught exception, and where are those notes displayed?

Expected: Call add_note with a string. The standard traceback displays the notes after the exception in insertion order.

**Generated answer:**

You can add explanatory notes to a caught exception by calling the `add_note` method on the exception instance. These notes are appended to the exception's notes list and included in the traceback output.

**Proposed correctness:** 1 | **Grounding:** supported | **Abstention:** None

**Reason:** Identifies add_note and traceback display, but omits the string argument and insertion order after the exception.

Borderline: False. Full annotated evidence: True. Output tokens: 40. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk018] Note that the exceptions nested in an exception group must be instances,
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

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

[python_errors_chunk014] Some objects define standard clean-up actions to be undertaken when the object
is no longer needed, regardless of whether or not the operation using the object
succeeded or failed. Look at the following example, which tries to open a file
and print its contents to the screen.

for line in open("myfile.txt"):
    print(line, end="")

The problem with this code is that it leaves the file open for an indeterminate
amount of time after this part of the code has finished executing.
This is not an issue in simple scripts, but can be a problem for larger
applications. The with statement allows objects like files to be
used in a way that ensures they are always cleaned up promptly and correctly.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

After the statement is executed, the file f is always closed, even if a
problem was encountered while processing the lines. Objects which, like files,
provide predefined clean-up actions will indicate this in their documentation.

8.9. Raising and Handling Multiple Unrelated Exceptions

There are situations where it is necessary to report several exceptions that
have occurred. This is often the case in concurrency frameworks, when several
tasks may have failed in parallel, but there are also other use cases where
it is desirable to continue execution and collect multiple errors rather than
raise the first exception.

[python_errors_chunk001] 8. Errors and Exceptions

Until now error messages haven’t been more than mentioned, but if you have tried
out the examples you have probably seen some.  There are (at least) two
distinguishable kinds of errors: syntax errors and exceptions .

8.1. Syntax Errors

Syntax errors, also known as parsing errors, are perhaps the most common kind of
complaint you get while you are still learning Python:

>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax

The parser repeats the offending line and displays little arrows pointing
at the place where the error was detected.  Note that this is not always the
place that needs to be fixed.  In the example, the error is detected at the
function print() , since a colon ( ':' ) is missing just before it.

The file name ( <stdin> in our example) and line number are printed so you
know where to look in case the input came from a file.

8.2. Exceptions

[python_errors_chunk015] The builtin ExceptionGroup wraps a list of exception instances so
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

[python_modules_chunk002] # Fibonacci numbers module

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

[python_errors_chunk019] For example, when collecting exceptions into an exception group, we may want
to add context information for the individual errors. In the following each
exception in the group has a note indicating when this error has occurred.

</details>

## test_013 / budget_900

How can I create a virtual environment named tutorial-env and then install dependencies from requirements.txt into it?

Expected: Create it with python -m venv tutorial-env and activate it. Then run python -m pip install -r requirements.txt.

**Generated answer:**

To create a virtual environment named tutorial-env and then install dependencies from requirements.txt into it, follow these steps:

1. Decide on a directory where you want to place the virtual environment. For example, you might choose a directory called .venv.

2. Run the following command to create the virtual environment:

   ```
   python -m venv tutorial-env
   ```

3. This command

**Proposed correctness:** 1 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Gives the requested create command but truncates before activation or installation. Also inconsistently mentions .venv.

Borderline: False. Full annotated evidence: True. Output tokens: 80. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

</details>

## test_013 / top_k_2

How can I create a virtual environment named tutorial-env and then install dependencies from requirements.txt into it?

Expected: Create it with python -m venv tutorial-env and activate it. Then run python -m pip install -r requirements.txt.

**Generated answer:**

To create a virtual environment named tutorial-env and then install dependencies from requirements.txt into it, follow these steps:

1. Decide on a directory where you want to place the virtual environment. For example, choose a directory named `.venv`.

2. Run the following command to create the virtual environment:

   ```
   python -m venv .venv
   ```

3. Activate the virtual

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Creates .venv instead of tutorial-env and truncates before activation and installation.

Borderline: False. Full annotated evidence: True. Output tokens: 80. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

</details>

## test_013 / top_k_8

How can I create a virtual environment named tutorial-env and then install dependencies from requirements.txt into it?

Expected: Create it with python -m venv tutorial-env and activate it. Then run python -m pip install -r requirements.txt.

**Generated answer:**

To create a virtual environment named `tutorial-env` and install dependencies from `requirements.txt`, follow these steps:

1. Decide upon a directory where you want to place the virtual environment. In this case, we'll use `.venv`.
2. Run the following command to create the virtual environment:
   ```bash
   python -m venv tutorial-env
   ```
3. Activate the virtual

**Proposed correctness:** 1 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Gives the requested create command but never completes activation or dependency installation. Also inconsistently mentions .venv.

Borderline: False. Full annotated evidence: True. Output tokens: 80. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_venv_chunk001] 12. Virtual Environments and Packages

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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_errors_chunk004] >>> while True:
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

</details>

## test_014 / budget_900

How can I upgrade requests and record the resulting installed package versions for sharing?

Expected: Run python -m pip install --upgrade requests. Export versions with python -m pip freeze > requirements.txt.

**Generated answer:**

To upgrade requests, use `python -m pip install --upgrade requests`. To record the resulting installed package versions for sharing, create a `requirements.txt` file containing the following commands:

```bash
python -m pip install --upgrade requests
cat requirements.txt
```

This script will first upgrade requests and then print out the updated list of installed packages.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Incorrectly puts shell commands into requirements.txt and uses cat instead of exporting versions, despite evidence being present.

Borderline: False. Full annotated evidence: True. Output tokens: 73. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_venv_chunk007] pip has many more options.  Consult the Installing Python modules guide for complete documentation for pip .  When you’ve written
a package and want to make it available on the Python Package Index,
consult the Python packaging user guide .

</details>

## test_014 / top_k_2

How can I upgrade requests and record the resulting installed package versions for sharing?

Expected: Run python -m pip install --upgrade requests. Export versions with python -m pip freeze > requirements.txt.

**Generated answer:**

To upgrade requests, use the following command:

```bash
$ python -m pip install --upgrade requests
```

After upgrading, you can check the installed package versions with:

```bash
$ python -m pip list
```

This will display the updated versions of all packages installed in your virtual environment.

**Proposed correctness:** 1 | **Grounding:** supported | **Abstention:** None

**Reason:** Correct upgrade and listing command, but no export for sharing; chunk006 is missing.

Borderline: False. Full annotated evidence: False. Output tokens: 64. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

</details>

## test_014 / top_k_8

How can I upgrade requests and record the resulting installed package versions for sharing?

Expected: Run python -m pip install --upgrade requests. Export versions with python -m pip freeze > requirements.txt.

**Generated answer:**

Upgrade requests using `python -m pip install --upgrade requests`. To record the installed package versions for sharing, create a `requirements.txt` file by running `python -m pip freeze > requirements.txt`, then commit the `requirements.txt` file to version control.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correct upgrade and pip freeze redirection; version-control suggestion is supported by chunk006.

Borderline: False. Full annotated evidence: True. Output tokens: 54. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_modules_chunk019] Now what happens when the user writes from sound.effects import * ?  Ideally,
one would hope that this somehow goes out to the filesystem, finds which
submodules are present in the package, and imports them all.  This could take a
long time and importing sub-modules might have unwanted side-effects that should
only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the
package.  The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__ , it is taken to be the
list of module names that should be imported when from package import * is
encountered.  It is up to the package author to keep this list up-to-date when a
new version of the package is released.  Package authors may also decide not to
support it, if they don’t see a use for importing * from their package.  For
example, the file sound/effects/__init__.py could contain the following
code:

__all__ = ["echo", "surround", "reverse"]

This would mean that from sound.effects import * would import the three
named submodules of the sound.effects package.

[python_venv_chunk007] pip has many more options.  Consult the Installing Python modules guide for complete documentation for pip .  When you’ve written
a package and want to make it available on the Python Package Index,
consult the Python packaging user guide .

</details>

## test_015 / budget_900

How can I import fibo under the name fib and reload that module after editing it?

Expected: Use import fibo as fib. After importing importlib, call importlib.reload(fib).

**Generated answer:**

To import fibo under the name fib and reload that module after editing it, you should first ensure that the module is reloaded using `importlib.reload()` before reloading it again. Here's how you can do it:

```python
from importlib import reload

# First, reload the module
reload(fibo)

# Then, import fibo again under the new alias
import fibo

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Does not implement import fibo as fib and starts with reload before importing; truncated.

Borderline: False. Full annotated evidence: True. Output tokens: 80. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk006] >>> from fibo import fib as fibonacci
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

[python_modules_chunk005] >>> from fibo import *
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

[python_modules_chunk013] _finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']

Without arguments, dir() lists the names you have defined currently:

>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

Note that it lists all types of names: variables, modules, functions, etc.

dir() does not list the names of built-in functions and variables.  If you
want a list of those, they are defined in the standard module builtins :

</details>

## test_015 / top_k_2

How can I import fibo under the name fib and reload that module after editing it?

Expected: Use import fibo as fib. After importing importlib, call importlib.reload(fib).

**Generated answer:**

To import fibo under the name fib and reload that module after editing it, you should first ensure that the module is reloaded using `importlib.reload()` before reloading it again. Here's how you can do it:

```python
from importlib import reload

# Reload the module
reload(fibo)

# Now you can import fibo again and use it
fib = fibo()


**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Does not implement the alias import and incorrectly calls the module as fibo(); truncated.

Borderline: False. Full annotated evidence: True. Output tokens: 80. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk006] >>> from fibo import fib as fibonacci
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

[python_modules_chunk005] >>> from fibo import *
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

</details>

## test_015 / top_k_8

How can I import fibo under the name fib and reload that module after editing it?

Expected: Use import fibo as fib. After importing importlib, call importlib.reload(fib).

**Generated answer:**

You can import fibo under the name fib and reload that module after editing it by using `importlib.reload(fibo)` after making changes to the file.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Omits import fibo as fib and reloads fibo instead of the requested alias.

Borderline: False. Full annotated evidence: True. Output tokens: 33. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk006] >>> from fibo import fib as fibonacci
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

[python_modules_chunk005] >>> from fibo import *
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

[python_modules_chunk013] _finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']

Without arguments, dir() lists the names you have defined currently:

>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

Note that it lists all types of names: variables, modules, functions, etc.

dir() does not list the names of built-in functions and variables.  If you
want a list of those, they are defined in the standard module builtins :

[python_modules_chunk002] # Fibonacci numbers module

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

[python_modules_chunk003] >>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'

If you intend to use a function often you can assign it to a local name:

>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

6.1. More on Modules

A module can contain executable statements as well as function definitions.
These statements are intended to initialize the module. They are executed only
the first time the module name is encountered in an import statement. [ 1 ] (They are also run if the file is executed as a script.)

[python_modules_chunk004] Each module has its own private namespace, which is used as the global namespace
by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user’s global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation used to
refer to its functions, modname.itemname .

Modules can import other modules.  It is customary but not required to place all import statements at the beginning of a module (or script, for that
matter).  The imported module names, if placed at the top level of a module
(outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a
module directly into the importing module’s namespace.  For example:

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_modules_chunk001] 6. Modules

If you quit from the Python interpreter and enter it again, the definitions you
have made (functions and variables) are lost. Therefore, if you want to write a
somewhat longer program, you are better off using a text editor to prepare the
input for the interpreter and running it with that file as input instead.  This
is known as creating a script .  As your program gets longer, you may want to
split it into several files for easier maintenance.  You may also want to use a
handy function that you’ve written in several programs without copying its
definition into each program.

To support this, Python has a way to put definitions in a file and use them in a
script or in an interactive instance of the interpreter. Such a file is called a module ; definitions from a module can be imported into other modules or into
the main module (the collection of variables that you have access to in a
script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements.  The file name
is the module name with the suffix .py appended.  Within a module, the
module’s name (as a string) is available as the value of the global variable __name__ .  For instance, use your favorite text editor to create a file
called fibo.py in the current directory with the following contents:

</details>

## test_016 / budget_900

What does Python's compiled-module cache help with, and can compileall generate these files for a directory?

Expected: The cache speeds up module loading. compileall can create .pyc files for modules in a directory.

**Generated answer:**

Python's compiled-module cache helps speed up loading modules by caching the compiled versions of each module in the __pycache__ directory under the name module.version.pyc, where the version encodes the format of the compiled file. Compileall can create .pyc files for all modules in a directory.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly distinguishes module loading speed and states compileall can generate directory .pyc files.

Borderline: False. Full annotated evidence: True. Output tokens: 61. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

</details>

## test_016 / top_k_2

What does Python's compiled-module cache help with, and can compileall generate these files for a directory?

Expected: The cache speeds up module loading. compileall can create .pyc files for modules in a directory.

**Generated answer:**

Python's compiled-module cache helps speed up loading modules by caching the compiled versions of each module in the __pycache__ directory under the name module.version.pyc, where the version encodes the format of the compiled file. Compileall can generate these files for all modules in a specified directory.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly distinguishes module loading speed and states compileall can generate directory .pyc files.

Borderline: False. Full annotated evidence: True. Output tokens: 60. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

</details>

## test_016 / top_k_8

What does Python's compiled-module cache help with, and can compileall generate these files for a directory?

Expected: The cache speeds up module loading. compileall can create .pyc files for modules in a directory.

**Generated answer:**

Python's compiled-module cache helps speed up loading modules by caching the compiled versions of each module in the __pycache__ directory under the name module.version.pyc, where the version encodes the format of the compiled file. Compileall can create .pyc files for all modules in a directory.

**Proposed correctness:** 2 | **Grounding:** supported | **Abstention:** None

**Reason:** Correctly distinguishes module loading speed and states compileall can generate directory .pyc files.

Borderline: False. Full annotated evidence: True. Output tokens: 61. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

[python_modules_chunk007] If the module is imported, the code is not run:

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

[python_modules_chunk016] Packages are a way of structuring Python’s module namespace by using “dotted
module names”.  For example, the module name A.B designates a submodule
named B in a package named A .  Just like the use of modules saves the
authors of different modules from having to worry about each other’s global
variable names, the use of dotted module names saves the authors of multi-module
packages like NumPy or Pillow from having to worry about
each other’s module names.

Suppose you want to design a collection of modules (a “package”) for the uniform
handling of sound files and sound data.  There are many different sound file
formats (usually recognized by their extension, for example: .wav , .aiff , .au ), so you may need to create and maintain a growing
collection of modules for the conversion between the various file formats.
There are also many different operations you might want to perform on sound data
(such as mixing, adding echo, applying an equalizer function, creating an
artificial stereo effect), so in addition you will be writing a never-ending
stream of modules to perform these operations.  Here’s a possible structure for
your package (expressed in terms of a hierarchical filesystem):

[python_modules_chunk001] 6. Modules

If you quit from the Python interpreter and enter it again, the definitions you
have made (functions and variables) are lost. Therefore, if you want to write a
somewhat longer program, you are better off using a text editor to prepare the
input for the interpreter and running it with that file as input instead.  This
is known as creating a script .  As your program gets longer, you may want to
split it into several files for easier maintenance.  You may also want to use a
handy function that you’ve written in several programs without copying its
definition into each program.

To support this, Python has a way to put definitions in a file and use them in a
script or in an interactive instance of the interpreter. Such a file is called a module ; definitions from a module can be imported into other modules or into
the main module (the collection of variables that you have access to in a
script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements.  The file name
is the module name with the suffix .py appended.  Within a module, the
module’s name (as a string) is available as the value of the global variable __name__ .  For instance, use your favorite text editor to create a file
called fibo.py in the current directory with the following contents:

[python_modules_chunk004] Each module has its own private namespace, which is used as the global namespace
by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user’s global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation used to
refer to its functions, modname.itemname .

Modules can import other modules.  It is customary but not required to place all import statements at the beginning of a module (or script, for that
matter).  The imported module names, if placed at the top level of a module
(outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a
module directly into the importing module’s namespace.  For example:

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

[python_modules_chunk010] Python comes with a library of standard modules, described in a separate
document, the Python Library Reference (“Library Reference” hereafter).  Some
modules are built into the interpreter; these provide access to operations that
are not part of the core of the language but are nevertheless built in, either
for efficiency or to provide access to operating system primitives such as
system calls.  The set of such modules is a configuration option which also
depends on the underlying platform.  For example, the winreg module is only
provided on Windows systems. One particular module deserves some attention: sys , which is built into every Python interpreter.  The variables sys.ps1 and sys.ps2 define the strings used as primary and secondary
prompts:

>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>

These two variables are only defined if the interpreter is in interactive mode.

The variable sys.path is a list of strings that determines the interpreter’s
search path for modules. It is initialized to a default path taken from the
environment variable PYTHONPATH , or from a built-in default if PYTHONPATH is not set.  You can modify it using standard list
operations:

>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')

6.3. The dir() Function

</details>

## test_017 / budget_900

How do I explicitly link a new exception to its cause, and how do I suppress automatic exception chaining?

Expected: Use raise NewException from original_exception to indicate the cause. Use raise NewException from None to suppress automatic chaining.

**Generated answer:**

To explicitly link a new exception to its cause, you can use the `from` keyword followed by `None`. To suppress automatic exception chaining, you can use the `from None` syntax within a `try-except` block.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Correct suppression syntax, but incorrectly uses from None to attach a cause; material contradiction.

Borderline: False. Full annotated evidence: True. Output tokens: 48. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk010] >>> def func():
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

</details>

## test_017 / top_k_2

How do I explicitly link a new exception to its cause, and how do I suppress automatic exception chaining?

Expected: Use raise NewException from original_exception to indicate the cause. Use raise NewException from None to suppress automatic chaining.

**Generated answer:**

To explicitly link a new exception to its cause, use the `from` clause with `None`. To suppress automatic exception chaining, omit the `from` clause.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Confuses explicit cause with from None and incorrectly says omitting from suppresses chaining.

Borderline: False. Full annotated evidence: True. Output tokens: 34. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk010] >>> def func():
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

</details>

## test_017 / top_k_8

How do I explicitly link a new exception to its cause, and how do I suppress automatic exception chaining?

Expected: Use raise NewException from original_exception to indicate the cause. Use raise NewException from None to suppress automatic chaining.

**Generated answer:**

To explicitly link a new exception to its cause, you can use the `from` keyword followed by `None`. To suppress automatic exception chaining, you can catch the exception using a specific exception handler like `except Exception as exc:` instead of just `except:`.

**Proposed correctness:** 0 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Confuses explicit cause with from None and gives incorrect suppression advice.

Borderline: False. Full annotated evidence: True. Output tokens: 54. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk010] >>> def func():
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_errors_chunk020] >>> def f():
...     raise OSError('operation failed')
...
>>> excs = []
>>> for i in range(3):
...     try:
...         f()
...     except Exception as e:
...         e.add_note(f'Happened in Iteration {i+1}')
...         excs.append(e)
...
>>> raise ExceptionGroup('We have some problems', excs)
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |     raise ExceptionGroup('We have some problems', excs)
  | ExceptionGroup: We have some problems (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration 1
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration

[python_errors_chunk011] Exception classes can be defined which do anything any other class can do, but
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

[python_errors_chunk005] A class in an except clause matches exceptions which are instances of the
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

[python_modules_chunk019] Now what happens when the user writes from sound.effects import * ?  Ideally,
one would hope that this somehow goes out to the filesystem, finds which
submodules are present in the package, and imports them all.  This could take a
long time and importing sub-modules might have unwanted side-effects that should
only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the
package.  The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__ , it is taken to be the
list of module names that should be imported when from package import * is
encountered.  It is up to the package author to keep this list up-to-date when a
new version of the package is released.  Package authors may also decide not to
support it, if they don’t see a use for importing * from their package.  For
example, the file sound/effects/__init__.py could contain the following
code:

__all__ = ["echo", "surround", "reverse"]

This would mean that from sound.effects import * would import the three
named submodules of the sound.effects package.

[python_modules_chunk005] >>> from fibo import *
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

</details>

## test_018 / budget_900

How can several exception instances be raised together and only those of a chosen type handled?

Expected: Wrap exception instances in an ExceptionGroup and raise it. Use except* to handle matching types within the group.

**Generated answer:**

Several exception instances can be raised together by wrapping them in an `ExceptionGroup` object. Only exceptions of a specified type need to be handled; others will be propagated.

**Proposed correctness:** 1 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Correct grouping, but selective handling and propagation claim is not established by the selected chunks; omits except*.

Borderline: True. Full annotated evidence: False. Output tokens: 35. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk015] The builtin ExceptionGroup wraps a list of exception instances so
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

[python_errors_chunk006] >>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception type
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs

The exception’s __str__() output is printed as the last part (‘detail’)
of the message for unhandled exceptions.

BaseException is the common base class of all exceptions. One of its
subclasses, Exception , is the base class of all the non-fatal exceptions.
Exceptions which are not subclasses of Exception are not typically
handled, because they are used to indicate that the program should terminate.
They include SystemExit which is raised by sys.exit() and KeyboardInterrupt which is raised when a user wishes to interrupt
the program.

Exception can be used as a wildcard that catches (almost) everything.
However, it is good practice to be as specific as possible with the types
of exceptions that we intend to handle, and to allow any unexpected
exceptions to propagate on.

[python_errors_chunk018] Note that the exceptions nested in an exception group must be instances,
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

</details>

## test_018 / top_k_2

How can several exception instances be raised together and only those of a chosen type handled?

Expected: Wrap exception instances in an ExceptionGroup and raise it. Use except* to handle matching types within the group.

**Generated answer:**

Several exception instances can be raised together by wrapping them in an `ExceptionGroup` object. This group can then be caught specifically if desired, allowing different handling based on the nature of the exceptions within the group.

**Proposed correctness:** 1 | **Grounding:** supported | **Abstention:** None

**Reason:** Correct ExceptionGroup wrapping and catching, but no mechanism for selecting subexception types; required evidence is missing.

Borderline: True. Full annotated evidence: False. Output tokens: 43. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk015] The builtin ExceptionGroup wraps a list of exception instances so
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

[python_errors_chunk006] >>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception type
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs

The exception’s __str__() output is printed as the last part (‘detail’)
of the message for unhandled exceptions.

BaseException is the common base class of all exceptions. One of its
subclasses, Exception , is the base class of all the non-fatal exceptions.
Exceptions which are not subclasses of Exception are not typically
handled, because they are used to indicate that the program should terminate.
They include SystemExit which is raised by sys.exit() and KeyboardInterrupt which is raised when a user wishes to interrupt
the program.

Exception can be used as a wildcard that catches (almost) everything.
However, it is good practice to be as specific as possible with the types
of exceptions that we intend to handle, and to allow any unexpected
exceptions to propagate on.

</details>

## test_018 / top_k_8

How can several exception instances be raised together and only those of a chosen type handled?

Expected: Wrap exception instances in an ExceptionGroup and raise it. Use except* to handle matching types within the group.

**Generated answer:**

Several exception instances can be raised together by wrapping them in an `ExceptionGroup`. Only exceptions of a specified type within the group can be handled; others are passed to subsequent except blocks.

**Proposed correctness:** 1 | **Grounding:** unsupported_or_contradicted | **Abstention:** None

**Reason:** Correct ExceptionGroup concept, but omits except* and describes ordinary except blocks for selective handling.

Borderline: True. Full annotated evidence: True. Output tokens: 38. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk015] The builtin ExceptionGroup wraps a list of exception instances so
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

[python_errors_chunk006] >>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception type
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs

The exception’s __str__() output is printed as the last part (‘detail’)
of the message for unhandled exceptions.

BaseException is the common base class of all exceptions. One of its
subclasses, Exception , is the base class of all the non-fatal exceptions.
Exceptions which are not subclasses of Exception are not typically
handled, because they are used to indicate that the program should terminate.
They include SystemExit which is raised by sys.exit() and KeyboardInterrupt which is raised when a user wishes to interrupt
the program.

Exception can be used as a wildcard that catches (almost) everything.
However, it is good practice to be as specific as possible with the types
of exceptions that we intend to handle, and to allow any unexpected
exceptions to propagate on.

[python_errors_chunk018] Note that the exceptions nested in an exception group must be instances,
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

[python_errors_chunk016] By using except* instead of except , we can selectively
handle only the exceptions in the group that match a certain
type. In the following example, which shows a nested exception
group, each except* clause extracts from the group exceptions
of a certain type while letting all other exceptions propagate to
other clauses and eventually to be reraised.

[python_errors_chunk007] The most common pattern for handling Exception is to print or log
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

[python_errors_chunk011] Exception classes can be defined which do anything any other class can do, but
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

[python_errors_chunk002] Even if a statement or expression is syntactically correct, it may cause an
error when an attempt is made to execute it. Errors detected during execution
are called exceptions and are not unconditionally fatal: you will soon learn
how to handle them in Python programs.  Most exceptions are not handled by
programs, however, and result in error messages as shown here:

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

[python_errors_chunk005] A class in an except clause matches exceptions which are instances of the
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

</details>

## test_019 / budget_900

What exact maximum disk space can a Python virtual environment occupy?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

I do not have enough information to determine the exact maximum disk space a Python virtual environment can occupy.

**Proposed correctness:** None | **Grounding:** not_applicable | **Abstention:** True

**Reason:** Clearly declines to give a maximum disk value and adds no substantive unsupported advice.

Borderline: False. Full annotated evidence: None. Output tokens: 21. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_venv_chunk001] 12. Virtual Environments and Packages

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

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

</details>

## test_019 / top_k_2

What exact maximum disk space can a Python virtual environment occupy?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

I do not have enough information to determine the exact maximum disk space a Python virtual environment can occupy. This would depend on various factors including the size of the installed packages, the operating system, and other software configurations.

**Proposed correctness:** None | **Grounding:** unsupported_or_contradicted | **Abstention:** True

**Reason:** Declines the value, but adds size/OS/configuration factors not established by the supplied context.

Borderline: False. Full annotated evidence: None. Output tokens: 44. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_venv_chunk001] 12. Virtual Environments and Packages

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

</details>

## test_019 / top_k_8

What exact maximum disk space can a Python virtual environment occupy?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

I do not have enough information to determine the exact maximum disk space a Python virtual environment can occupy.

**Proposed correctness:** None | **Grounding:** not_applicable | **Abstention:** True

**Reason:** Clearly declines to give a maximum disk value and adds no substantive unsupported advice.

Borderline: False. Full annotated evidence: None. Output tokens: 21. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_venv_chunk001] 12. Virtual Environments and Packages

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

[python_venv_chunk002] The module used to create and manage virtual environments is called venv . venv will install the Python version from which
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_errors_chunk003] The last line of the error message indicates what happened. Exceptions come in
different types, and the type is printed as part of the message: the types in
the example are ZeroDivisionError , NameError and TypeError .
The string printed as the exception type is the name of the built-in exception
that occurred.  This is true for all built-in exceptions, but need not be true
for user-defined exceptions (although it is a useful convention). Standard
exception names are built-in identifiers (not reserved keywords).

The rest of the line provides detail based on the type of exception and what
caused it.

The preceding part of the error message shows the context where the exception
occurred, in the form of a stack traceback. In general it contains a stack
traceback listing source lines; however, it will not display lines read from
standard input.

Built-in Exceptions lists the built-in exceptions and their meanings.

8.3. Handling Exceptions

It is possible to write programs that handle selected exceptions. Look at the
following example, which asks the user for input until a valid integer has been
entered, but allows the user to interrupt the program (using Control - C or
whatever the operating system supports); note that a user-generated interruption
is signalled by raising the KeyboardInterrupt exception.

[python_modules_chunk010] Python comes with a library of standard modules, described in a separate
document, the Python Library Reference (“Library Reference” hereafter).  Some
modules are built into the interpreter; these provide access to operations that
are not part of the core of the language but are nevertheless built in, either
for efficiency or to provide access to operating system primitives such as
system calls.  The set of such modules is a configuration option which also
depends on the underlying platform.  For example, the winreg module is only
provided on Windows systems. One particular module deserves some attention: sys , which is built into every Python interpreter.  The variables sys.ps1 and sys.ps2 define the strings used as primary and secondary
prompts:

>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>

These two variables are only defined if the interpreter is in interactive mode.

The variable sys.path is a list of strings that determines the interpreter’s
search path for modules. It is initialized to a default path taken from the
environment variable PYTHONPATH , or from a built-in default if PYTHONPATH is not set.  You can modify it using standard list
operations:

>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')

6.3. The dir() Function

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_modules_chunk004] Each module has its own private namespace, which is used as the global namespace
by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user’s global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation used to
refer to its functions, modname.itemname .

Modules can import other modules.  It is customary but not required to place all import statements at the beginning of a module (or script, for that
matter).  The imported module names, if placed at the top level of a module
(outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a
module directly into the importing module’s namespace.  For example:

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

</details>

## test_020 / budget_900

What pip version is currently installed on my laptop?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

I do not have enough information to determine the exact pip version installed on your laptop based solely on the provided text. The text does not mention any specific pip version being installed. To find out the current pip version, you would need to check the system's PATH or use tools like `pip` itself to query its own version.

**Proposed correctness:** None | **Grounding:** unsupported_or_contradicted | **Abstention:** True

**Reason:** Declines the requested version, but falsely says no specific pip version is mentioned and adds unsupported PATH advice.

Borderline: False. Full annotated evidence: None. Output tokens: 67. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_venv_chunk007] pip has many more options.  Consult the Installing Python modules guide for complete documentation for pip .  When you’ve written
a package and want to make it available on the Python Package Index,
consult the Python packaging user guide .

</details>

## test_020 / top_k_2

What pip version is currently installed on my laptop?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

I do not have enough information to determine the exact pip version installed on your laptop based solely on the provided text. The text does not mention any specific pip version being installed. To find out the current pip version, you would need to check the system's PATH or use tools like `pip freeze` which lists installed packages along with their versions.

**Proposed correctness:** None | **Grounding:** unsupported_or_contradicted | **Abstention:** True

**Reason:** Declines the requested version, but falsely says the text has no specific pip version (it contains an example) and adds unsupported PATH/freeze advice.

Borderline: False. Full annotated evidence: None. Output tokens: 70. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

</details>

## test_020 / top_k_8

What pip version is currently installed on my laptop?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

I do not have enough information to determine the current pip version installed on your laptop.

**Proposed correctness:** None | **Grounding:** not_applicable | **Abstention:** True

**Reason:** Clearly states the laptop pip version cannot be determined.

Borderline: False. Full annotated evidence: None. Output tokens: 18. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_modules_chunk013] _finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']

Without arguments, dir() lists the names you have defined currently:

>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

Note that it lists all types of names: variables, modules, functions, etc.

dir() does not list the names of built-in functions and variables.  If you
want a list of those, they are defined in the standard module builtins :

[python_venv_chunk001] 12. Virtual Environments and Packages

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

[python_venv_chunk007] pip has many more options.  Consult the Installing Python modules guide for complete documentation for pip .  When you’ve written
a package and want to make it available on the Python Package Index,
consult the Python packaging user guide .

[python_errors_chunk003] The last line of the error message indicates what happened. Exceptions come in
different types, and the type is printed as part of the message: the types in
the example are ZeroDivisionError , NameError and TypeError .
The string printed as the exception type is the name of the built-in exception
that occurred.  This is true for all built-in exceptions, but need not be true
for user-defined exceptions (although it is a useful convention). Standard
exception names are built-in identifiers (not reserved keywords).

The rest of the line provides detail based on the type of exception and what
caused it.

The preceding part of the error message shows the context where the exception
occurred, in the form of a stack traceback. In general it contains a stack
traceback listing source lines; however, it will not display lines read from
standard input.

Built-in Exceptions lists the built-in exceptions and their meanings.

8.3. Handling Exceptions

It is possible to write programs that handle selected exceptions. Look at the
following example, which asks the user for input until a valid integer has been
entered, but allows the user to interrupt the program (using Control - C or
whatever the operating system supports); note that a user-generated interruption
is signalled by raising the KeyboardInterrupt exception.

</details>

## test_021 / budget_900

Which private package-index URL does our company require?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

I do not know.

**Proposed correctness:** None | **Grounding:** not_applicable | **Abstention:** True

**Reason:** Clearly declines to identify the unknown company package-index URL.

Borderline: False. Full annotated evidence: None. Output tokens: 6. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_venv_chunk007] pip has many more options.  Consult the Installing Python modules guide for complete documentation for pip .  When you’ve written
a package and want to make it available on the Python Package Index,
consult the Python packaging user guide .

[python_modules_chunk019] Now what happens when the user writes from sound.effects import * ?  Ideally,
one would hope that this somehow goes out to the filesystem, finds which
submodules are present in the package, and imports them all.  This could take a
long time and importing sub-modules might have unwanted side-effects that should
only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the
package.  The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__ , it is taken to be the
list of module names that should be imported when from package import * is
encountered.  It is up to the package author to keep this list up-to-date when a
new version of the package is released.  Package authors may also decide not to
support it, if they don’t see a use for importing * from their package.  For
example, the file sound/effects/__init__.py could contain the following
code:

__all__ = ["echo", "surround", "reverse"]

This would mean that from sound.effects import * would import the three
named submodules of the sound.effects package.

[python_modules_chunk004] Each module has its own private namespace, which is used as the global namespace
by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user’s global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation used to
refer to its functions, modname.itemname .

Modules can import other modules.  It is customary but not required to place all import statements at the beginning of a module (or script, for that
matter).  The imported module names, if placed at the top level of a module
(outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a
module directly into the importing module’s namespace.  For example:

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

</details>

## test_021 / top_k_2

Which private package-index URL does our company require?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

I do not have enough information to determine the specific private package index URL required by the company. The provided text does not mention any requirements related to a private package index. Therefore, I cannot provide an answer based solely on this context.

**Proposed correctness:** None | **Grounding:** not_applicable | **Abstention:** True

**Reason:** Clearly declines to identify the unknown company package-index URL.

Borderline: False. Full annotated evidence: None. Output tokens: 48. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_venv_chunk007] pip has many more options.  Consult the Installing Python modules guide for complete documentation for pip .  When you’ve written
a package and want to make it available on the Python Package Index,
consult the Python packaging user guide .

</details>

## test_021 / top_k_8

Which private package-index URL does our company require?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

I do not have enough information to determine which private package-index URL your company requires.

**Proposed correctness:** None | **Grounding:** not_applicable | **Abstention:** True

**Reason:** Clearly declines to identify the unknown company package-index URL.

Borderline: False. Full annotated evidence: None. Output tokens: 18. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk003] Activating the virtual environment will change your shell’s prompt to show what
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

[python_venv_chunk007] pip has many more options.  Consult the Installing Python modules guide for complete documentation for pip .  When you’ve written
a package and want to make it available on the Python Package Index,
consult the Python packaging user guide .

[python_modules_chunk019] Now what happens when the user writes from sound.effects import * ?  Ideally,
one would hope that this somehow goes out to the filesystem, finds which
submodules are present in the package, and imports them all.  This could take a
long time and importing sub-modules might have unwanted side-effects that should
only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the
package.  The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__ , it is taken to be the
list of module names that should be imported when from package import * is
encountered.  It is up to the package author to keep this list up-to-date when a
new version of the package is released.  Package authors may also decide not to
support it, if they don’t see a use for importing * from their package.  For
example, the file sound/effects/__init__.py could contain the following
code:

__all__ = ["echo", "surround", "reverse"]

This would mean that from sound.effects import * would import the three
named submodules of the sound.effects package.

[python_modules_chunk004] Each module has its own private namespace, which is used as the global namespace
by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user’s global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation used to
refer to its functions, modname.itemname .

Modules can import other modules.  It is customary but not required to place all import statements at the beginning of a module (or script, for that
matter).  The imported module names, if placed at the top level of a module
(outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a
module directly into the importing module’s namespace.  For example:

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

[python_modules_chunk022] Note that relative imports are based on the name of the current module’s package.
Since the main module does not have a package, modules intended for use
as the main module of a Python application must always use absolute imports.

Footnotes

In fact function definitions are also ‘statements’ that are ‘executed’; the
execution of a module-level function definition adds the function name to
the module’s global namespace.

[python_errors_chunk001] 8. Errors and Exceptions

Until now error messages haven’t been more than mentioned, but if you have tried
out the examples you have probably seen some.  There are (at least) two
distinguishable kinds of errors: syntax errors and exceptions .

8.1. Syntax Errors

Syntax errors, also known as parsing errors, are perhaps the most common kind of
complaint you get while you are still learning Python:

>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax

The parser repeats the offending line and displays little arrows pointing
at the place where the error was detected.  Note that this is not always the
place that needs to be fixed.  In the example, the error is detected at the
function print() , since a colon ( ':' ) is missing just before it.

The file name ( <stdin> in our example) and line number are printed so you
know where to look in case the input came from a file.

8.2. Exceptions

[python_modules_chunk020] Be aware that submodules might become shadowed by locally defined names. For
example, if you added a reverse function to the sound/effects/__init__.py file, the from sound.effects import * would only import the two submodules echo and surround , but not the reverse submodule, because it is shadowed by the locally defined reverse function:

__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'

If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package sound.effects into the
current namespace; it only ensures that the package sound.effects has
been imported (possibly running any initialization code in __init__.py )
and then imports whatever names are defined in the package.  This includes any
names defined (and submodules explicitly loaded) by __init__.py .  It
also includes any submodules of the package that were explicitly loaded by
previous import statements.  Consider this code:

import sound.effects.echo
import sound.effects.surround
from sound.effects import *

[python_venv_chunk001] 12. Virtual Environments and Packages

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

</details>

## test_022 / budget_900

What numerical speedup is guaranteed when loading a cached .pyc module?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

Automatic

**Proposed correctness:** None | **Grounding:** unsupported_or_contradicted | **Abstention:** False

**Reason:** Automatic is irrelevant to the requested numeric speedup and is not an abstention.

Borderline: False. Full annotated evidence: None. Output tokens: 2. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_modules_chunk019] Now what happens when the user writes from sound.effects import * ?  Ideally,
one would hope that this somehow goes out to the filesystem, finds which
submodules are present in the package, and imports them all.  This could take a
long time and importing sub-modules might have unwanted side-effects that should
only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the
package.  The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__ , it is taken to be the
list of module names that should be imported when from package import * is
encountered.  It is up to the package author to keep this list up-to-date when a
new version of the package is released.  Package authors may also decide not to
support it, if they don’t see a use for importing * from their package.  For
example, the file sound/effects/__init__.py could contain the following
code:

__all__ = ["echo", "surround", "reverse"]

This would mean that from sound.effects import * would import the three
named submodules of the sound.effects package.

</details>

## test_022 / top_k_2

What numerical speedup is guaranteed when loading a cached .pyc module?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

Not applicable

**Proposed correctness:** None | **Grounding:** unsupported_or_contradicted | **Abstention:** False

**Reason:** Not applicable does not clearly explain that the supplied documentation lacks a numeric speedup.

Borderline: True. Full annotated evidence: None. Output tokens: 3. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

</details>

## test_022 / top_k_8

What numerical speedup is guaranteed when loading a cached .pyc module?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

No numerical speedup is guaranteed when loading a cached .pyc module.

**Proposed correctness:** None | **Grounding:** unsupported_or_contradicted | **Abstention:** True

**Reason:** Does not fabricate a number and is interpreted as denying a documented guarantee, but wording is broader than the reference: absence of documentation is not proof no guarantee exists.

Borderline: True. Full annotated evidence: None. Output tokens: 16. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_modules_chunk019] Now what happens when the user writes from sound.effects import * ?  Ideally,
one would hope that this somehow goes out to the filesystem, finds which
submodules are present in the package, and imports them all.  This could take a
long time and importing sub-modules might have unwanted side-effects that should
only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the
package.  The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__ , it is taken to be the
list of module names that should be imported when from package import * is
encountered.  It is up to the package author to keep this list up-to-date when a
new version of the package is released.  Package authors may also decide not to
support it, if they don’t see a use for importing * from their package.  For
example, the file sound/effects/__init__.py could contain the following
code:

__all__ = ["echo", "surround", "reverse"]

This would mean that from sound.effects import * would import the three
named submodules of the sound.effects package.

[python_modules_chunk004] Each module has its own private namespace, which is used as the global namespace
by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user’s global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation used to
refer to its functions, modname.itemname .

Modules can import other modules.  It is customary but not required to place all import statements at the beginning of a module (or script, for that
matter).  The imported module names, if placed at the top level of a module
(outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a
module directly into the importing module’s namespace.  For example:

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

[python_errors_chunk003] The last line of the error message indicates what happened. Exceptions come in
different types, and the type is printed as part of the message: the types in
the example are ZeroDivisionError , NameError and TypeError .
The string printed as the exception type is the name of the built-in exception
that occurred.  This is true for all built-in exceptions, but need not be true
for user-defined exceptions (although it is a useful convention). Standard
exception names are built-in identifiers (not reserved keywords).

The rest of the line provides detail based on the type of exception and what
caused it.

The preceding part of the error message shows the context where the exception
occurred, in the form of a stack traceback. In general it contains a stack
traceback listing source lines; however, it will not display lines read from
standard input.

Built-in Exceptions lists the built-in exceptions and their meanings.

8.3. Handling Exceptions

It is possible to write programs that handle selected exceptions. Look at the
following example, which asks the user for input until a valid integer has been
entered, but allows the user to interrupt the program (using Control - C or
whatever the operating system supports); note that a user-generated interruption
is signalled by raising the KeyboardInterrupt exception.

[python_modules_chunk007] If the module is imported, the code is not run:

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

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_modules_chunk018] sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

An alternative way of importing the submodule is:

from sound.effects import echo

This also loads the submodule echo , and makes it available without its
package prefix, so it can be used as follows:

echo.echofilter(input, output, delay=0.7, atten=4)

Yet another variation is to import the desired function or variable directly:

from sound.effects.echo import echofilter

Again, this loads the submodule echo , but this makes its function echofilter() directly available:

echofilter(input, output, delay=0.7, atten=4)

Note that when using from package import item , the item can be either a
submodule (or subpackage) of the package, or some  other name defined in the
package, like a function, class or variable.  The import statement first
tests whether the item is defined in the package; if not, it assumes it is a
module and attempts to load it.  If it fails to find it, an ImportError exception is raised.

Contrarily, when using syntax like import item.subitem.subsubitem , each item
except for the last must be a package; the last item can be a module or a
package but can’t be a class or function or variable defined in the previous
item.

6.4.1. Importing * From a Package

</details>

## test_023 / budget_900

What maximum number of exception notes does this documentation specify?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

This documentation specifies that there is no explicit limit on the number of exception notes that can be added to an exception object. However, adding too many notes can clutter the tracebacks and make them harder to read. It's generally recommended to keep the number of notes minimal and relevant to avoid unnecessary complexity.

**Proposed correctness:** None | **Grounding:** unsupported_or_contradicted | **Abstention:** True

**Reason:** Interpreted as saying no explicit maximum is specified; adds unsupported tracebacks/style advice. Do not read it as proof of an unlimited implementation.

Borderline: True. Full annotated evidence: None. Output tokens: 61. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk004] >>> while True:
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

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_errors_chunk018] Note that the exceptions nested in an exception group must be instances,
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

</details>

## test_023 / top_k_2

What maximum number of exception notes does this documentation specify?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

The documentation specifies up to two exception notes per except clause.

**Proposed correctness:** None | **Grounding:** unsupported_or_contradicted | **Abstention:** False

**Reason:** Invents a maximum of two notes per except clause.

Borderline: False. Full annotated evidence: None. Output tokens: 13. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk004] >>> while True:
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

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

</details>

## test_023 / top_k_8

What maximum number of exception notes does this documentation specify?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

The documentation specifies that a class in an except clause matches exceptions which are instances of the class itself or one of its derived classes, but not the other way around. For example, the following code will print B, C, D in that order:

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B,

**Proposed correctness:** None | **Grounding:** supported | **Abstention:** False

**Reason:** Irrelevant exception-handler explanation; the complete claims are drawn from context but it does not acknowledge the missing maximum. Truncated.

Borderline: False. Full annotated evidence: None. Output tokens: 80. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_errors_chunk004] >>> while True:
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

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_errors_chunk018] Note that the exceptions nested in an exception group must be instances,
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

[python_errors_chunk005] A class in an except clause matches exceptions which are instances of the
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

[python_errors_chunk003] The last line of the error message indicates what happened. Exceptions come in
different types, and the type is printed as part of the message: the types in
the example are ZeroDivisionError , NameError and TypeError .
The string printed as the exception type is the name of the built-in exception
that occurred.  This is true for all built-in exceptions, but need not be true
for user-defined exceptions (although it is a useful convention). Standard
exception names are built-in identifiers (not reserved keywords).

The rest of the line provides detail based on the type of exception and what
caused it.

The preceding part of the error message shows the context where the exception
occurred, in the form of a stack traceback. In general it contains a stack
traceback listing source lines; however, it will not display lines read from
standard input.

Built-in Exceptions lists the built-in exceptions and their meanings.

8.3. Handling Exceptions

It is possible to write programs that handle selected exceptions. Look at the
following example, which asks the user for input until a valid integer has been
entered, but allows the user to interrupt the program (using Control - C or
whatever the operating system supports); note that a user-generated interruption
is signalled by raising the KeyboardInterrupt exception.

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_modules_chunk004] Each module has its own private namespace, which is used as the global namespace
by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user’s global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation used to
refer to its functions, modname.itemname .

Modules can import other modules.  It is customary but not required to place all import statements at the beginning of a module (or script, for that
matter).  The imported module names, if placed at the top level of a module
(outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a
module directly into the importing module’s namespace.  For example:

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

[python_venv_chunk007] pip has many more options.  Consult the Installing Python modules guide for complete documentation for pip .  When you’ve written
a package and want to make it available on the Python Package Index,
consult the Python packaging user guide .

</details>

## test_024 / budget_900

What is the current latest requests release on PyPI?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

The current latest version of requests on PyPI is 2.7.0.

**Proposed correctness:** None | **Grounding:** unsupported_or_contradicted | **Abstention:** False

**Reason:** Presents the historical example version 2.7.0 as the current latest release, which the supplied snapshot cannot establish.

Borderline: False. Full annotated evidence: None. Output tokens: 18. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

</details>

## test_024 / top_k_2

What is the current latest requests release on PyPI?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

The current latest version of requests on PyPI is 2.7.0.

**Proposed correctness:** None | **Grounding:** unsupported_or_contradicted | **Abstention:** False

**Reason:** Presents the historical example version 2.7.0 as the current latest release, which the supplied snapshot cannot establish.

Borderline: False. Full annotated evidence: None. Output tokens: 18. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

</details>

## test_024 / top_k_8

What is the current latest requests release on PyPI?

Expected: State that the answer cannot be determined from the supplied documentation.

**Generated answer:**

The current latest version of the "requests" package on PyPI is 2.7.0.

**Proposed correctness:** None | **Grounding:** unsupported_or_contradicted | **Abstention:** False

**Reason:** Presents the historical example version 2.7.0 as the current latest release, which the supplied snapshot cannot establish.

Borderline: False. Full annotated evidence: None. Output tokens: 22. Source citation: False.

<details>
<summary>Supplied context</summary>

[python_venv_chunk004] pip has a number of subcommands: “install”, “uninstall”,
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

[python_venv_chunk005] (tutorial-env) $ python -m pip install --upgrade requests
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

[python_venv_chunk006] python -m pip freeze will produce a similar list of the installed packages,
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

[python_errors_chunk003] The last line of the error message indicates what happened. Exceptions come in
different types, and the type is printed as part of the message: the types in
the example are ZeroDivisionError , NameError and TypeError .
The string printed as the exception type is the name of the built-in exception
that occurred.  This is true for all built-in exceptions, but need not be true
for user-defined exceptions (although it is a useful convention). Standard
exception names are built-in identifiers (not reserved keywords).

The rest of the line provides detail based on the type of exception and what
caused it.

The preceding part of the error message shows the context where the exception
occurred, in the form of a stack traceback. In general it contains a stack
traceback listing source lines; however, it will not display lines read from
standard input.

Built-in Exceptions lists the built-in exceptions and their meanings.

8.3. Handling Exceptions

It is possible to write programs that handle selected exceptions. Look at the
following example, which asks the user for input until a valid integer has been
entered, but allows the user to interrupt the program (using Control - C or
whatever the operating system supports); note that a user-generated interruption
is signalled by raising the KeyboardInterrupt exception.

[python_modules_chunk009] Python does not check the cache in two circumstances.  First, it always
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

[python_modules_chunk008] After initialization, Python programs can modify sys.path .  The
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

[python_modules_chunk007] If the module is imported, the code is not run:

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

[python_modules_chunk004] Each module has its own private namespace, which is used as the global namespace
by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user’s global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation used to
refer to its functions, modname.itemname .

Modules can import other modules.  It is customary but not required to place all import statements at the beginning of a module (or script, for that
matter).  The imported module names, if placed at the top level of a module
(outside any functions or classes), are added to the module’s global namespace.

There is a variant of the import statement that imports names from a
module directly into the importing module’s namespace.  For example:

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local namespace (so in the example, fibo is not defined).

There is even a variant to import all names that a module defines:

</details>

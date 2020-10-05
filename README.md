# gitmodules_example_b
This is the second example for the
<a href=https://github.com/KuYaki/gitmodules>gitmodules</a> project.
However it is just a part of a complex construction with root at 
<a href=https://github.com/KuYaki/gitmodules_example_a>gitmodules_example_a</a>.

## Dependencies
This project is assumed to be used with the <a href=https://github.com/KuYaki/gitmodules>gitmodules</a> dependency

```
pip install gitmodules
```

And the <a href=https://github.com/KuYaki/gitmodules_example_c>gitmodules_example_c</a> should be updated as well

```
git submodule update --recursive --init
```

## Description
<a href=https://github.com/KuYaki/gitmodules_example_c>gitmodules_example_c</a> can be executed as a main script 
but if you will try to import it in any other project as a git submodule
you will be forced to append its path to the <b>sys.path</b>:

```python
# in b.py from gitmodules_example_b
import sys
sys.path.append("gitmodules_example_c")
from gitmodules_example_c import c
```

Or you can simply use <a href=https://github.com/KuYaki/gitmodules>gitmodules</a> instead:

```python
# in b.py from gitmodules_example_b
import gitmodules
from gitmodules_example_c import c
```

This method allows you to import git submodule as an ordinary module or as a standard library.
So that if you will decide to upload your git submodules to PyPi you will not be forced to change your scripts. 

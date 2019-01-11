# Contributing

> Welcome! Contributors are welcome, under the following guidelines.  You do not have to be a member of our organization to contribute!

This project is intended as a library for [mechasqueak3](https://github.com/FuelRats/pipsqueak3), open source, and released under [BSD-3](LICENSE).

While some members have direct write access, it is intended that feature updates undergo a peer review process.  Please submit a PR for any feature request, against the DEVELOP branch.

One does not simply *commit* to master.

## Pull Request Requirements
* Pull requests without meaningful testing will NOT be accepted.
* Pull requests that are out of scope or modify unnecessary files will NOT be accepted.
* Pull requests should have concise messages and commits.

Use docstrings and comments to document how your feature functions, and why.
Docstrings should be formatted to the flavor of [Google](https://google.github.io/styleguide/pyguide.html?showone=Comments#Comments).

Example docstring:
```python
def example_function(param1: int, param2: str) -> bool:
"""
This is an example doc string.  It may span multiple lines, however
it may not break the 100 characters per line PEP8 standard.  It is a
good standard to include expected types, explain what your function
attempts to accomplish, and what result is returned, if any.

Args:
    param1 (int): First Parameter.
    param2 (str): Second Parameter.

Returns:
    bool: True if successful, False otherwise.
"""
return False
```

### Reporting Issues
Please report issues on Github.

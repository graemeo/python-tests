[![Build Status](https://travis-ci.org/graemeo/python-tests.svg?branch=master)](https://travis-ci.org/graemeo/python-tests)
# Description

Simple Python project to explore and learn Python's testing capability.

# Pre-requisite(s)

* virtualenv
* Python 2.7

# Installation

## Setup Python virtual environment

```
virtualenv <PROJECT>
source <PROJECT>/bin/activate
```

## Install Python modules

```
pip install -r <PATH>/requirements
```


# Usage(s)

## Tests execution

```
python -m unittest discover tests -v "*_test.py""
```

## Coverage report generation

```
coverage run --source=. --branch -m unittest discover tests -v "*_test.py"
coverage report -m
```

# Custodian(s)

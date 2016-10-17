========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-leeway/badge/?style=flat
    :target: https://readthedocs.org/projects/python-leeway
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/sdrees/python-leeway.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/sdrees/python-leeway

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/sdrees/python-leeway?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/sdrees/python-leeway

.. |requires| image:: https://requires.io/github/sdrees/python-leeway/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/sdrees/python-leeway/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/sdrees/python-leeway/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/github/sdrees/python-leeway

.. |codecov| image:: https://codecov.io/github/sdrees/python-leeway/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/sdrees/python-leeway

.. |landscape| image:: https://landscape.io/github/sdrees/python-leeway/master/landscape.svg?style=flat
    :target: https://landscape.io/github/sdrees/python-leeway/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg?style=flat
    :target: https://www.codacy.com/app/sdrees/python-leeway
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/sdrees/python-leeway/badges/gpa.svg
   :target: https://codeclimate.com/github/sdrees/python-leeway
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/leeway.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/leeway

.. |downloads| image:: https://img.shields.io/pypi/dm/leeway.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/leeway

.. |wheel| image:: https://img.shields.io/pypi/wheel/leeway.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/leeway

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/leeway.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/leeway

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/leeway.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/leeway

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/sdrees/python-leeway/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/sdrees/python-leeway/


.. end-badges

Bread and butter box pushing bread slices under butter knives. Hints from previous runs are taken.

* Free software: BSD license

Installation
============

::

    pip install leeway

Documentation
=============

https://python-leeway.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

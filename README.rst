========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires| |coveralls|
        | |scrutinizer| |codeclimate| |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-leeway/badge/?style=flat
    :target: https://readthedocs.org/projects/python-leeway/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/sthagen/python-leeway.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/sthagen/python-leeway

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/sthagen/python-leeway?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/sthagen/python-leeway

.. |requires| image:: https://requires.io/github/sthagen/python-leeway/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/sthagen/python-leeway/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/sthagen/python-leeway/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/github/sthagen/python-leeway

.. |codecov| image:: https://codecov.io/gh/sthagen/python-leeway/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/gh/sthagen/python-leeway

.. |codeclimate| image:: https://codeclimate.com/github/sthagen/python-leeway/badges/gpa.svg
   :target: https://codeclimate.com/github/sthagen/python-leeway
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/leeway.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/leeway

.. |downloads| image:: https://img.shields.io/pypi/dm/leeway.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.org/project/leeway

.. |wheel| image:: https://img.shields.io/pypi/wheel/leeway.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.org/project/leeway

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/leeway.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.org/project/leeway

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/leeway.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.org/project/leeway

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/sthagen/python-leeway/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/sthagen/python-leeway/


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

Note: The name of the default branch is *default* :wink:

#!/usr/bin/env python
import os
import sys

if sys.version_info < (3, 6):
    print('Error: dbt does not support this version of Python.')
    print('Please upgrade to Python 3.6 or higher.')
    sys.exit(1)


from setuptools import setup
try:
    from setuptools import find_namespace_packages
except ImportError:
    # the user has a downlevel version of setuptools.
    print('Error: dbt requires setuptools v40.1.0 or higher.')
    print('Please upgrade setuptools with "pip install --upgrade setuptools" '
          'and try again')
    sys.exit(1)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


package_name = "dbt-core"
package_version = "0.20.0rc1"
description = """dbt (data build tool) is a command line tool that helps \
analysts and engineers transform data in their warehouse more effectively"""


setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="Fishtown Analytics",
    author_email="info@fishtownanalytics.com",
    url="https://github.com/fishtown-analytics/dbt",
    packages=find_namespace_packages(include=['dbt', 'dbt.*']),
    package_data={
        'dbt': [
            'include/index.html',
            'include/global_project/dbt_project.yml',
            'include/global_project/docs/*.md',
            'include/global_project/macros/*.sql',
            'include/global_project/macros/**/*.sql',
            'include/global_project/macros/**/**/*.sql',
            'py.typed',
        ]
    },
    test_suite='test',
    entry_points={
        'console_scripts': [
            'dbt = dbt.main:main',
        ],
    },
    scripts=[
        'scripts/dbt',
    ],
    install_requires=[
        'Jinja2==2.11.3',
        'PyYAML>=3.11',
        'agate>=1.6,<1.6.2',
        'colorama>=0.3.9,<0.4.5',
        'dataclasses>=0.6,<0.9;python_version<"3.7"',
        'hologram==0.0.14',
        'isodate>=0.6,<0.7',
        'json-rpc>=1.12,<2',
        'logbook>=1.5,<1.6',
        'mashumaro==2.5',
        'minimal-snowplow-tracker==0.0.2',
        'networkx>=2.3,<3',
        'packaging~=20.9',
        'sqlparse>=0.2.3,<0.4',
        'tree-sitter==0.19.0',
        'tree-sitter-jinja2==0.1.0a1',
        'typing-extensions>=3.7.4,<3.8',
        'werkzeug>=0.15,<2.0',
        # the following are all to match snowflake-connector-python
        'requests<3.0.0',
        'idna>=2.5,<3',
        'cffi>=1.9,<2.0.0',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: Apache Software License',

        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires=">=3.6.3",
)

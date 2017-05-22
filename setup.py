"""
setup for data-structures
"""
from setuptools import setup

DEPENDENCIES = ['pytest', 'pytest-cov', 'ipython']
MODULES = ['linked_list']
EXTRA_PACKAGES = {
    'test': ['tox']
}
CONSOLE_SCRIPTS = {
    'console_scripts': [
        'linked_list = linked_list:main'
    ]
}
setup(
    name="data-structures",
    description="""A module that contains code
    samples for a number of classic data structures implemented in Python.""",
    version='0.1',
    author='Elyanil Castro',
    author_email='yanil3500@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    # insert the names of pymodule into array
    py_modules=MODULES,
    install_requires=DEPENDENCIES,
    extras_require=EXTRA_PACKAGES,
    # console scripts allow for custom commands
    entry_points=CONSOLE_SCRIPTS


)

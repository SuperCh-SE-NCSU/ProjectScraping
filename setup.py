try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def discover_and_run_tests():
    import os
    import sys
    import unittest

    # get setup.py directory
    setup_file = sys.modules['__main__'].__file__
    setup_dir = os.path.abspath(os.path.dirname(setup_file))

    # use the default shared TestLoader instance
    test_loader = unittest.defaultTestLoader

    # use the basic test runner that outputs to sys.stderr
    test_runner = unittest.TextTestRunner()

    # automatically discover all tests
    # NOTE: only works for python 2.7 and later
    test_suite = test_loader.discover(setup_dir)

    # run the test suite
    test_runner.run(test_suite)

try:
    from setuptools.command.test import test

    class DiscoverTest(test):

        def finalize_options(self):
            test.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            discover_and_run_tests()

except ImportError:
    from distutils.core import Command

    class DiscoverTest(Command):
        user_options = []

        def initialize_options(self):
                pass

        def finalize_options(self):
            pass

        def run(self):
            discover_and_run_tests()

setup(
    name='coveralls',
    version='1.0a2',
    packages=['coveralls'],
    url='http://github.com/coagulant/coveralls-python',
    license='MIT',
    entry_points={
        'console_scripts': [
            'coveralls = coveralls.cli:main',
        ],
    },
    install_requires=['coverage>=3.6', 'requests>=1.0.0'],
    cmdclass={'test': DiscoverTest},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)

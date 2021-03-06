from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


# also update in nsq/version.py
version = '0.6.5'


setup(
    name='pynsq',
    version=version,
    description='official Python client library for NSQ',
    keywords='python nsq',
    author='Matt Reiferson',
    author_email='snakes@gmail.com',
    url='http://github.com/bitly/pynsq',
    download_url='https://s3.amazonaws.com/bitly-downloads/nsq/pynsq-%s.tar.gz' % version,
    packages=['nsq'],
    requires=['tornado', 'six'],
    include_package_data=True,
    zip_safe=False,
    tests_require=['pytest', 'mock', 'tornado', 'six'],
    cmdclass={'test': PyTest},
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ]
)

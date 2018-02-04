# -*- coding:utf-8 -*-
#!/usr/bin/env python
# encoding: utf-8
import sys

try:
    from setuptools import Command, setup
except ImportError:
    from distutils.core import Command, setup
try:
    import unittest2 as unittest
except ImportError:
    import unittest

# import psptools
# import tests

required = ''
with open('requirements.txt') as f:
    required = f.read().splitlines()

class RunTests(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if(sys.stdout.encoding == 'utf-8'):
            print('╭─────────────────────────────────────╮')
            print('│                                     │')
            print('│              Test Start             │')
            print('│                                     │')
            print('╰─────────────────────────────────────╯')
        else:
            print('Test Start')
        import tests
        import time
        print('1')
        ptests = unittest.TestSuite(tests.suite())
        print('2')
        runner = unittest.TextTestRunner(verbosity=2)
        print('3')
        results = runner.run(ptests)
        print('4')
        time.sleep(1)
        print('5')
        sys.exit(0 if results.wasSuccessful() else 1)


classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Operating System :: OS Independent',
    'Environment :: X11 Applications',
    'Environment :: Win32 (MS Windows)',
    'Environment :: MacOS X',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python',
    # 'Programming Language :: Python :: 2',
    # 'Programming Language :: Python :: 2.6',
    # 'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.6',
    'Topic :: Text Processing',
    'Topic :: Utilities',
    'Topic :: Software Development :: Code Generators']


def description():
    lines = open('README.rst', 'rb').read().splitlines(False)
    return '\n' + str(b'\n'.join(lines)) + '\n'


setup(name='psptools',
      version=0.1,
      description='Python sports programming tools...',
      long_description=description(),
      author='Epikem',
      author_email='dltldls95@naver.com',
      url='https://github.com/Epikem/psptools.git',
      packages=['psptools'],
      license='MIT',
      classifiers=classifiers,
      install_requires=required,
      tests_require=required,
    #   install_requires=
    #   [
    #       'astunparse',
    #       'mock'
    #   ],
      cmdclass={
          'test': RunTests,
      })


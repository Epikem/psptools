import os.path
import shutil
import sys
import logging
# import psptools
logging.basicConfig(format='%(levelname)s:%(funcName)s:%(message)s',
                    level=logging.INFO)
try:
    import unittest2 as unittest
except ImportError:
    import unittest



def make_folder(path=None):
    if path is None:
        path = 'testfolder'
    os.mkdir(path)

def remove_recursively(path=None):
    if path is None:
        path = 'testfolder'
    if not os.path.exists(path):
        return
    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path)


def only_for(version):
    """Should be used as a decorator for a unittest.TestCase test method"""
    return unittest.skipIf(
        sys.version < version,
        'This test requires at least {0} version of Python.'.format(version))


def only_for_versions_lower(version):
    """Should be used as a decorator for a unittest.TestCase test method"""
    return unittest.skipIf(
        sys.version > version,
        'This test requires version of Python lower than {0}'.format(version))


def skipNotPOSIX():
    return unittest.skipIf(os.name != 'posix',
                           'This test works only on POSIX')
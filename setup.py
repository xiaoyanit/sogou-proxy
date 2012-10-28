from distutils.core import setup
import py2exe

setup(
    console=['bootstrap.py'],
    zipfile=None,
    options={
        "py2exe": {
            "optimize": 2,
            "compressed": True,
            "bundle_files": 1,
            "ascii": True,
            "includes": [
                "__future__",
                "contextlib",
                "ctypes",
                "ctypes.wintypes",
                "functools",
                "htmlentitydefs",
                "logging",
                "os",
                "select",
                "signal",
                "socket",
                "struct",
                "time",
                "urllib",
                "ConfigParser",
                ],
            "excludes": [
                "_ssl",
                "bdb",
                "calendar",
                "difflib",
                "doctest",
                "gettext",
                "hashlib",
                "httplib",
                "inspect",
                "locale",
                "optparse",
                "pdb",
                "pickle",
                "rfc822",
                "ssl",
                "subprocess",
                "tempfile",
                "tokenize",
                "unittest",
            ]
        }
    }
)
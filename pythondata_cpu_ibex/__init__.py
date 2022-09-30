import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2561"
version_tuple = (0, 0, 2561)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2561")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2419"
data_version_tuple = (0, 0, 2419)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2419")
except ImportError:
    pass
data_git_hash = "1313104bade1302ee651610b8536209255654cc4"
data_git_describe = "v0.0-2419-g1313104b"
data_git_msg = """\
commit 1313104bade1302ee651610b8536209255654cc4
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Sep 28 11:59:48 2022 +0100

    [ci] Fix pmp_smoke_test
    
    It was renamed pmp_smoke_test from pmp_exception_test in the software
    build but not the actual test run

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

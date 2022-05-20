import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2428"
version_tuple = (0, 0, 2428)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2428")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2300"
data_version_tuple = (0, 0, 2300)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2300")
except ImportError:
    pass
data_git_hash = "fe157648a6e51fe06a6f67f2050ef1236a75c13c"
data_git_describe = "v0.0-2300-gfe157648"
data_git_msg = """\
commit fe157648a6e51fe06a6f67f2050ef1236a75c13c
Author: nedguthrie <101828291+nedguthrie@users.noreply.github.com>
Date:   Fri May 20 13:12:59 2022 -0400

    Fix formatting if IcacheScramble Description

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

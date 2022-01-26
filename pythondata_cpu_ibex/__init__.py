import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2267"
version_tuple = (0, 0, 2267)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2267")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2145"
data_version_tuple = (0, 0, 2145)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2145")
except ImportError:
    pass
data_git_hash = "69dfa6f8daf294c766a042c640a5830169e5b914"
data_git_describe = "v0.0-2145-g69dfa6f8"
data_git_msg = """\
commit 69dfa6f8daf294c766a042c640a5830169e5b914
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Jan 26 15:09:07 2022 +0000

    [ci] Add missing python3-dev dependency
    
    Private CI is broken without this. The public CI runs on azure agents
    which already have this installed.

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

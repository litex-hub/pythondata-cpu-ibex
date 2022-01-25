import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2266"
version_tuple = (0, 0, 2266)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2266")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2144"
data_version_tuple = (0, 0, 2144)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2144")
except ImportError:
    pass
data_git_hash = "c0f67946f21838de36088b6a25573051b925207e"
data_git_describe = "v0.0-2144-gc0f67946"
data_git_msg = """\
commit c0f67946f21838de36088b6a25573051b925207e
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Mon Jan 24 18:46:46 2022 +0000

    [rtl,doc] Add double fault detection.
    
    Fixes #1117

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

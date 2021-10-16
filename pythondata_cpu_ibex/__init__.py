import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2204"
version_tuple = (0, 0, 2204)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2204")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2092"
data_version_tuple = (0, 0, 2092)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2092")
except ImportError:
    pass
data_git_hash = "a345da3badf65788e02634ca3386b79c1c44d72c"
data_git_describe = "v0.0-2092-ga345da3b"
data_git_msg = """\
commit a345da3badf65788e02634ca3386b79c1c44d72c
Author: Henner Zeller <h.zeller@acm.org>
Date:   Fri Oct 15 13:42:47 2021 -0700

    Change use of blocking assignment to non-blocking inside always_ff
    
    Fixes #1457
    
    Signed-off-by: Henner Zeller <h.zeller@acm.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

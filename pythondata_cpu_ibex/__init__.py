import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2465"
version_tuple = (0, 0, 2465)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2465")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2323"
data_version_tuple = (0, 0, 2323)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2323")
except ImportError:
    pass
data_git_hash = "7ba6667f3237c9a6fd48c21bfff4b2f4fb5ff491"
data_git_describe = "v0.0-2323-g7ba6667f"
data_git_msg = """\
commit 7ba6667f3237c9a6fd48c21bfff4b2f4fb5ff491
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Mon Jul 11 11:24:35 2022 +0100

    [dv] Check privilege after DRET
    
    Timing fix for dret_test and modelling controller behaviour for FLUSH transition.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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

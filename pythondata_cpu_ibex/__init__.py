import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2472"
version_tuple = (0, 0, 2472)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2472")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2330"
data_version_tuple = (0, 0, 2330)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2330")
except ImportError:
    pass
data_git_hash = "dfca76f3865d9fc8ab7f093ff563f91add6648ca"
data_git_describe = "v0.0-2330-gdfca76f3"
data_git_msg = """\
commit dfca76f3865d9fc8ab7f093ff563f91add6648ca
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Tue Jul 12 23:44:19 2022 +0100

    [dv,fcov] Implement Misaligned Mem Error coverage
    
    Adds some signal to the load store unit to catch when we have the
    fetch error signals from both first and second part of the misaligned
    load/store access cases.
    
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

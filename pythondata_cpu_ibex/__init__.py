import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2676"
version_tuple = (0, 0, 2676)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2676")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2534"
data_version_tuple = (0, 0, 2534)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2534")
except ImportError:
    pass
data_git_hash = "7592bb9478653a04a59c1ab14c009b14be9f72e9"
data_git_describe = "v0.0-2534-g7592bb94"
data_git_msg = """\
commit 7592bb9478653a04a59c1ab14c009b14be9f72e9
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Nov 2 16:35:18 2022 +0000

    [dv] Disable bad integrity on uninit accesses for mem error tests

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

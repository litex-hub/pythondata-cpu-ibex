import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2579"
version_tuple = (0, 0, 2579)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2579")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2437"
data_version_tuple = (0, 0, 2437)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2437")
except ImportError:
    pass
data_git_hash = "7c28d3caf3860408d6ef016e9e18e862e70d971a"
data_git_describe = "v0.0-2437-g7c28d3ca"
data_git_msg = """\
commit 7c28d3caf3860408d6ef016e9e18e862e70d971a
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Mon Oct 10 10:39:45 2022 +0100

    [ci] Update IBEX_COSIM_VERSION to latest
    
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

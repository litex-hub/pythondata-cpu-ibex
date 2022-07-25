import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2479"
version_tuple = (0, 0, 2479)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2479")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2337"
data_version_tuple = (0, 0, 2337)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2337")
except ImportError:
    pass
data_git_hash = "1e613cc7f439415ae4f4c86f4452f11a829d7e5e"
data_git_describe = "v0.0-2337-g1e613cc7"
data_git_msg = """\
commit 1e613cc7f439415ae4f4c86f4452f11a829d7e5e
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Thu Jul 14 21:32:46 2022 +0100

    [cosim,dv] Add support to set mcount registers
    
    Extends RVFI connections further to include 30 mhpmcounterX registers.
    Sets them up before every cosim step to let Spike know their real values.
    
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

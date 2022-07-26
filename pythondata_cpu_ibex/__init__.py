import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2486"
version_tuple = (0, 0, 2486)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2486")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2344"
data_version_tuple = (0, 0, 2344)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2344")
except ImportError:
    pass
data_git_hash = "6dc0683773635bfde3949c6fa7d9c3e7282ab916"
data_git_describe = "v0.0-2344-g6dc06837"
data_git_msg = """\
commit 6dc0683773635bfde3949c6fa7d9c3e7282ab916
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Jul 26 13:28:44 2022 +0100

    [dv] Fix IbexDataRPayloadX assertion
    
    Some aspects of the memory response are only relevant to reads. This
    introduces outstanding request tracking so we know which outstanding
    requests are reads and applies X checks appropriately.
    
    Fixes #1645

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

import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2263"
version_tuple = (0, 0, 2263)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2263")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2141"
data_version_tuple = (0, 0, 2141)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2141")
except ImportError:
    pass
data_git_hash = "187944c417f04c144b9730445052aec0fc93620a"
data_git_describe = "v0.0-2141-g187944c4"
data_git_msg = """\
commit 187944c417f04c144b9730445052aec0fc93620a
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Thu Oct 7 18:04:56 2021 +0100

    [icache] Add RAM Primitives for scrambling
    
    This commit includes switching to a scrambling RAM primitive for
    ICache data and tag RAMs. Also introduces minor changes to ICache
    to handle scrambling key valid signal.
    
    It also includes a minor bug fix regarding not initializing
    `fill_way_q` signal without ResetAll parameter. When the parameter
    is not set and we have our first hit right after ICache enables,
    the signal hangs.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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

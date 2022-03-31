import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2328"
version_tuple = (0, 0, 2328)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2328")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2202"
data_version_tuple = (0, 0, 2202)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2202")
except ImportError:
    pass
data_git_hash = "2fc4cde7d269e69c77f784468959779cef2f3a55"
data_git_describe = "v0.0-2202-g2fc4cde7"
data_git_msg = """\
commit 2fc4cde7d269e69c77f784468959779cef2f3a55
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Thu Mar 31 15:32:32 2022 +0100

    [dv,xlm] Pass simulator flag to cov.py in Makefile
    
    Enables us to work with only xlm licences when doing the coverage.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

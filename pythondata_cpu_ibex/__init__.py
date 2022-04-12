import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2345"
version_tuple = (0, 0, 2345)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2345")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2219"
data_version_tuple = (0, 0, 2219)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2219")
except ImportError:
    pass
data_git_hash = "6caf82c2b402c4b0895a514ca30bc15f4705e17f"
data_git_describe = "v0.0-2219-g6caf82c2"
data_git_msg = """\
commit 6caf82c2b402c4b0895a514ca30bc15f4705e17f
Author: Michael Schaffner <msf@google.com>
Date:   Mon Apr 11 18:59:38 2022 -0700

    [lint] Minor fixes
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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

import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2279"
version_tuple = (0, 0, 2279)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2279")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2153"
data_version_tuple = (0, 0, 2153)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2153")
except ImportError:
    pass
data_git_hash = "336173b4d953560e9d0c9e6cb9ffefbc02d336b4"
data_git_describe = "v0.0-2153-g336173b4"
data_git_msg = """\
commit 336173b4d953560e9d0c9e6cb9ffefbc02d336b4
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Feb 15 17:50:34 2022 +0000

    Re-enable bitmanip tests

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

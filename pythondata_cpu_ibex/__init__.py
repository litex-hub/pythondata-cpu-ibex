import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2270"
version_tuple = (0, 0, 2270)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2270")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2146"
data_version_tuple = (0, 0, 2146)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2146")
except ImportError:
    pass
data_git_hash = "46b7e07098f5900b45a37bc45fb8e7b779776b9d"
data_git_describe = "v0.0-2146-g46b7e070"
data_git_msg = """\
commit 46b7e07098f5900b45a37bc45fb8e7b779776b9d
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Jan 27 09:21:51 2022 +0000

    [doc] Fix RV32B enum description

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

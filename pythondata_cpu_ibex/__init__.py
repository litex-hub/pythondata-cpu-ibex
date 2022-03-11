import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2301"
version_tuple = (0, 0, 2301)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2301")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2175"
data_version_tuple = (0, 0, 2175)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2175")
except ImportError:
    pass
data_git_hash = "094451a9489d631895101a5de19a26cd4cf4fd7d"
data_git_describe = "v0.0-2175-g094451a9"
data_git_msg = """\
commit 094451a9489d631895101a5de19a26cd4cf4fd7d
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Mar 10 17:59:51 2022 +0000

    [doc] Add examples info to README

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

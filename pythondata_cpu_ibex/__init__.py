import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2203"
version_tuple = (0, 0, 2203)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2203")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2091"
data_version_tuple = (0, 0, 2091)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2091")
except ImportError:
    pass
data_git_hash = "416ecb10dfdb80ce88b8b41ab7c39a6bcefbba50"
data_git_describe = "v0.0-2091-g416ecb10"
data_git_msg = """\
commit 416ecb10dfdb80ce88b8b41ab7c39a6bcefbba50
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Sep 17 15:49:06 2021 +0100

    [dv] Add co-simulation environment support to UVM testbench

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

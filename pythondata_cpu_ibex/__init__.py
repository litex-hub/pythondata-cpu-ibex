import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2103"
version_tuple = (0, 0, 2103)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2103")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2008"
data_version_tuple = (0, 0, 2008)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2008")
except ImportError:
    pass
data_git_hash = "25cd6600c64e6eec4c3f5ee20237b53e4d5a3a52"
data_git_describe = "v0.0-2008-g25cd6600"
data_git_msg = """\
commit 25cd6600c64e6eec4c3f5ee20237b53e4d5a3a52
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Apr 7 16:07:49 2021 +0100

    [dv] Don't kill regression on sim error
    
    When the simulator terminates with an error code that is reported as a
    test failure and the regression continues. A new check for a plain
    'Error' message is required to catch simulator reported errors that
    don't become a UVM_FATAL or UVM_ERROR message (e.g. hitting an illegal
    coverage bin). Previously any such simulation error would kill the whole
    regression.

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

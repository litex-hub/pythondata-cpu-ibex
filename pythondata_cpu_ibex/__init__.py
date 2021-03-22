import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2092"
version_tuple = (0, 0, 2092)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2092")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1997"
data_version_tuple = (0, 0, 1997)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1997")
except ImportError:
    pass
data_git_hash = "69ae65c71352028cd175fe3ce99f2404f46b14c5"
data_git_describe = "v0.0-1997-g69ae65c7"
data_git_msg = """\
commit 69ae65c71352028cd175fe3ce99f2404f46b14c5
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Mon Mar 22 16:33:08 2021 +0000

    [dv] Remove semicolon
    
    It's Python.

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

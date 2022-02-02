import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2272"
version_tuple = (0, 0, 2272)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2272")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2148"
data_version_tuple = (0, 0, 2148)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2148")
except ImportError:
    pass
data_git_hash = "4482af17898046d7249d63fd18b92614b7598552"
data_git_describe = "v0.0-2148-g4482af17"
data_git_msg = """\
commit 4482af17898046d7249d63fd18b92614b7598552
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Feb 2 09:50:31 2022 +0000

    [doc] Fix inline literal syntax in icache.rst

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

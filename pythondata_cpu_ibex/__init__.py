import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2621"
version_tuple = (0, 0, 2621)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2621")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2479"
data_version_tuple = (0, 0, 2479)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2479")
except ImportError:
    pass
data_git_hash = "ed927be38770b3478f34d4eace6edc1d74decaa8"
data_git_describe = "v0.0-2479-ged927be3"
data_git_msg = """\
commit ed927be38770b3478f34d4eace6edc1d74decaa8
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Oct 27 15:56:25 2022 +0100

    [cov] Remove ignored_csrs coverpoints
    
    These related to unimplemented CSRs. These are already captured by one
    of the illegal instruction categories.

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

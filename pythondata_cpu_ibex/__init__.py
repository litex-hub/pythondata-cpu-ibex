import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2106"
version_tuple = (0, 0, 2106)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2106")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2011"
data_version_tuple = (0, 0, 2011)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2011")
except ImportError:
    pass
data_git_hash = "ed5f12c99e2dc822dd74961b82c973eacdb5deb5"
data_git_describe = "v0.0-2011-ged5f12c9"
data_git_msg = """\
commit ed5f12c99e2dc822dd74961b82c973eacdb5deb5
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Apr 8 17:29:03 2021 +0100

    [rtl] Fix RF read enables for illegal instruction/fetch error
    
    The read enables should only be asserted where an actual RF read will
    occur. Where there is an illegal instruction or a fetch error the raw
    decoder signals might still be asserted but should be squashed before
    they become the true enable signals.

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

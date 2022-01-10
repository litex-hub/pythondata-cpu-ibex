import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2252"
version_tuple = (0, 0, 2252)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2252")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2134"
data_version_tuple = (0, 0, 2134)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2134")
except ImportError:
    pass
data_git_hash = "8c01488624b42066fcb268dcecf20b008146dbbd"
data_git_describe = "v0.0-2134-g8c014886"
data_git_msg = """\
commit 8c01488624b42066fcb268dcecf20b008146dbbd
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Jan 7 14:15:41 2022 +0100

    [rtl] Document lockstep reset generation mechanism
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

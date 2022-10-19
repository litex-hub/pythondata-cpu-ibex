import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2599"
version_tuple = (0, 0, 2599)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2599")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2457"
data_version_tuple = (0, 0, 2457)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2457")
except ImportError:
    pass
data_git_hash = "ce536ae47677e952de02b7421e1b78efb5761ab2"
data_git_describe = "v0.0-2457-gce536ae4"
data_git_msg = """\
commit ce536ae47677e952de02b7421e1b78efb5761ab2
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Fri Oct 14 12:03:26 2022 +0000

    [rtl] Assert that dummy instructions only write R0
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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

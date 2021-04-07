import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2102"
version_tuple = (0, 0, 2102)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2102")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2007"
data_version_tuple = (0, 0, 2007)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2007")
except ImportError:
    pass
data_git_hash = "a88f5eb91218f0c30ca5dc0dac30bbd3d0f2810e"
data_git_describe = "v0.0-2007-ga88f5eb9"
data_git_msg = """\
commit a88f5eb91218f0c30ca5dc0dac30bbd3d0f2810e
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Thu Mar 25 17:11:50 2021 +0000

    [rtl] Add dual core lockstep option
    
    Note that the alert output is tied off for now until an option is added
    to reset all registers (otherwise there will be X propagation).
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

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

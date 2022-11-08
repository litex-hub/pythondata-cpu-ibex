import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2681"
version_tuple = (0, 0, 2681)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2681")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2539"
data_version_tuple = (0, 0, 2539)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2539")
except ImportError:
    pass
data_git_hash = "2c15b96a353aeb42dbcaeadec4a92a8f4b54fe63"
data_git_describe = "v0.0-2539-g2c15b96a"
data_git_msg = """\
commit 2c15b96a353aeb42dbcaeadec4a92a8f4b54fe63
Author: Saad Khalid <saad.khalid@lowrisc.org>
Date:   Thu Nov 3 14:28:59 2022 +0000

    [dv] added functional coverpoints
    
    Coverpoints for priv modes with interrupts and mstatus.MIE, and with exceptions.
    Also, fixed a checker for scenarios when interrupt is taken from lower priv modes.
    
    Signed-off-by: Saad Khalid <saad.khalid@lowrisc.org>

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

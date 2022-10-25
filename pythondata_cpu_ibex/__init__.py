import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2610"
version_tuple = (0, 0, 2610)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2610")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2468"
data_version_tuple = (0, 0, 2468)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2468")
except ImportError:
    pass
data_git_hash = "659dc458f2a8d32cbb04ca4b43f793f51faf1ee8"
data_git_describe = "v0.0-2468-g659dc458"
data_git_msg = """\
commit 659dc458f2a8d32cbb04ca4b43f793f51faf1ee8
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Tue Oct 25 14:46:50 2022 +0100

    Fix bug in passing cosim_agent handle to the data_intf_seq
    
    The handle was passed before the cosim was constructed, so when it came to use
    the handle it caused a null pointer exception.

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

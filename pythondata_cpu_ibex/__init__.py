import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2593"
version_tuple = (0, 0, 2593)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2593")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2451"
data_version_tuple = (0, 0, 2451)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2451")
except ImportError:
    pass
data_git_hash = "083fe2a54f087235a09f4c90bc1560d798b9685e"
data_git_describe = "v0.0-2451-g083fe2a5"
data_git_msg = """\
commit 083fe2a54f087235a09f4c90bc1560d798b9685e
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Sat Oct 15 20:36:49 2022 +0100

    [dv] Use fetch enable sequence by default
    
    This sequence randomly toggles the fetch enable.

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

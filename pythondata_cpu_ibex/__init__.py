import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2111"
version_tuple = (0, 0, 2111)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2111")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2016"
data_version_tuple = (0, 0, 2016)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2016")
except ImportError:
    pass
data_git_hash = "0e7117fbec434fcfdf2bcce4ed379d34cdbe68b4"
data_git_describe = "v0.0-2016-g0e7117fb"
data_git_msg = """\
commit 0e7117fbec434fcfdf2bcce4ed379d34cdbe68b4
Author: Michael Schaffner <msf@google.com>
Date:   Thu Apr 15 18:23:38 2021 -0700

    [lockstep] Introduce optimization barrier around lockstep Ibex
    
    Certain synthesis tools like DC are very smart at optimizing away redundant logic.
    Hence, we have to insert an optimization barrier at the IOs of the lockstep Ibex.
    This is achieved by manually buffering each bit using prim_buf.
    Our Xilinx and DC synthesis flows make sure that these buffers cannot be optimized
    away using keep attributes (Vivado) and size_only constraints (DC).
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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

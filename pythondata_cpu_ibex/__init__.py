import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2226"
version_tuple = (0, 0, 2226)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2226")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2114"
data_version_tuple = (0, 0, 2114)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2114")
except ImportError:
    pass
data_git_hash = "40dab87448db052b40758075289382fda7b41fc1"
data_git_describe = "v0.0-2114-g40dab874"
data_git_msg = """\
commit 40dab87448db052b40758075289382fda7b41fc1
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Nov 26 16:40:33 2021 +0100

    [rtl, bitmanip] Clarify situation around zext.[bh] pseudo-instructions
    
    This is related to lowRISC/Ibex#1228.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

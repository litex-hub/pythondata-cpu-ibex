import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2262"
version_tuple = (0, 0, 2262)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2262")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2140"
data_version_tuple = (0, 0, 2140)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2140")
except ImportError:
    pass
data_git_hash = "e53b033962d39a09da574216a8c1813afccdd212"
data_git_describe = "v0.0-2140-ge53b0339"
data_git_msg = """\
commit e53b033962d39a09da574216a8c1813afccdd212
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Jan 13 18:17:30 2022 +0000

    [examples/fpga] Fix memory interface
    
    Logic driving instr_gnt/data_gnt violated Ibex memory protocol. It just
    happened to work until a recent change.
    
    Fixes #1500

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

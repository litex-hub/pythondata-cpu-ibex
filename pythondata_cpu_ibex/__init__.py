import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2469"
version_tuple = (0, 0, 2469)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2469")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2327"
data_version_tuple = (0, 0, 2327)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2327")
except ImportError:
    pass
data_git_hash = "42d92c7c9bb96a63cdaec78cd40f1367d2eadbd3"
data_git_describe = "v0.0-2327-g42d92c7c"
data_git_msg = """\
commit 42d92c7c9bb96a63cdaec78cd40f1367d2eadbd3
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Thu Jun 30 14:13:52 2022 +0100

    Create riscv_assorted_traps_interrupts_debug_test
    
    Signed-off-by: Harry Callahan <hcallahan@lowrisc.org>

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

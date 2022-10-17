import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2597"
version_tuple = (0, 0, 2597)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2597")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2455"
data_version_tuple = (0, 0, 2455)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2455")
except ImportError:
    pass
data_git_hash = "33f1d0a702bac8f1fbd18bda0c447a0329d1d6d3"
data_git_describe = "v0.0-2455-g33f1d0a7"
data_git_msg = """\
commit 33f1d0a702bac8f1fbd18bda0c447a0329d1d6d3
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Fri Oct 14 16:16:52 2022 +0100

    Update google_riscv-dv to google/riscv-dv@e0eae9e
    
    Update code from upstream repository https://github.com/google/riscv-
    dv to revision e0eae9e0ca69770c519c82c48421005f65521eac
    
    * [sv] Explicit type casting for VCS compability (Canberk Topal)
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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

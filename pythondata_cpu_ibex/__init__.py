import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2582"
version_tuple = (0, 0, 2582)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2582")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2440"
data_version_tuple = (0, 0, 2440)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2440")
except ImportError:
    pass
data_git_hash = "25d81afef664351f6fd14fd4ed7a19bba2224b55"
data_git_describe = "v0.0-2440-g25d81afe"
data_git_msg = """\
commit 25d81afef664351f6fd14fd4ed7a19bba2224b55
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Tue Oct 11 16:50:16 2022 +0100

    Update google_riscv-dv to google/riscv-dv@c6acc18
    
    Update code from upstream repository https://github.com/google/riscv-
    dv to revision c6acc1897429f5245cc89b2ecee2e3eefdefd18d
    
    * Add plusarg to enable ECALL insn in main randomized body (Harry
      Callahan)
    
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

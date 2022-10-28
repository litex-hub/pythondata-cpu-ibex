import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2624"
version_tuple = (0, 0, 2624)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2624")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2482"
data_version_tuple = (0, 0, 2482)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2482")
except ImportError:
    pass
data_git_hash = "0c0626ebbf6ded92fe84dbb8cdb558383c99adf2"
data_git_describe = "v0.0-2482-g0c0626eb"
data_git_msg = """\
commit 0c0626ebbf6ded92fe84dbb8cdb558383c99adf2
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Fri Oct 28 14:19:39 2022 +0100

    Update google_riscv-dv to google/riscv-dv@be9c75f
    
    Update code from upstream repository https://github.com/google/riscv-
    dv to revision be9c75fe6911504c0e6e9b89dc2a7766e367c500
    
    * Reserve one extra word when pushing GPRs to kernel stack (Harry
      Callahan)
    * Store user-stack-pointer on kernel stack when pushing/popping GPRs
      (Harry Callahan)
    
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

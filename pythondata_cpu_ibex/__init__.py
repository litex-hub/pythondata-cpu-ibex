import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2654"
version_tuple = (0, 0, 2654)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2654")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2512"
data_version_tuple = (0, 0, 2512)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2512")
except ImportError:
    pass
data_git_hash = "120607f4f2d96c6f7cdade85144463ffc3864d84"
data_git_describe = "v0.0-2512-g120607f4"
data_git_msg = """\
commit 120607f4f2d96c6f7cdade85144463ffc3864d84
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Wed Nov 2 17:11:47 2022 +0000

    [xlm] Enable access to signals without dumping waves
    
    The `-access rw` option allows Xcelium to access signals in the design
    (e.g., with `uvm_hdl_read` or `uvm_hdl_force`) without having to dump
    waves (which substantially increases the run time).  See [1] for the
    background discussion.
    
    [1]: https://github.com/lowRISC/ibex/pull/1879#issuecomment-1300216022
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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

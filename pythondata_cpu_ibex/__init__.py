import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2090"
version_tuple = (0, 0, 2090)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2090")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1995"
data_version_tuple = (0, 0, 1995)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1995")
except ImportError:
    pass
data_git_hash = "c1e287e13b6877589944a4e91e2bae11ea2bd508"
data_git_describe = "v0.0-1995-gc1e287e1"
data_git_msg = """\
commit c1e287e13b6877589944a4e91e2bae11ea2bd508
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Mar 18 14:35:03 2021 +0000

    [dv] Fix riscv_nested_interrupt_test
    
    This broke due to changes in IRQ sequences. It relies on the inner
    interrupt being an NMI. This alters the test to use the specific NMI
    sequence.

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

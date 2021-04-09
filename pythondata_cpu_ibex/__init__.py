import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2104"
version_tuple = (0, 0, 2104)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2104")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2009"
data_version_tuple = (0, 0, 2009)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2009")
except ImportError:
    pass
data_git_hash = "550487611050155c30ee02db7cb26521a0c34666"
data_git_describe = "v0.0-2009-g55048761"
data_git_msg = """\
commit 550487611050155c30ee02db7cb26521a0c34666
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Mar 26 14:28:21 2021 +0000

    [dv] Add known failure detection to riscv_debug_ebreakmu_test

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

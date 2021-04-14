import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2110"
version_tuple = (0, 0, 2110)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2110")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2015"
data_version_tuple = (0, 0, 2015)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2015")
except ImportError:
    pass
data_git_hash = "1b59c67b5064d03ec62a2877de4e94d2802a2225"
data_git_describe = "v0.0-2015-g1b59c67b"
data_git_msg = """\
commit 1b59c67b5064d03ec62a2877de4e94d2802a2225
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Apr 13 14:34:05 2021 +0100

    [dv] Remove MISA from csr_description.yaml
    
    The value of `misa` will change depending on whether M or B are enabled.
    The presence and read values of other CSRs may also depend upon the Ibex
    configuration. A fix is required to allow riscv_csr_test to deal with
    different CSR descriptions for different Ibex configurations. For now
    just comment out `misa` from the descriptions file to enable
    riscv_csr_test to run on a wider range of configurations.

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

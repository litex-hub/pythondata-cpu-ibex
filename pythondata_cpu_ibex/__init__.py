import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2607"
version_tuple = (0, 0, 2607)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2607")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2465"
data_version_tuple = (0, 0, 2465)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2465")
except ImportError:
    pass
data_git_hash = "f385d4d6b1d1a2455baf0bec7cc77d3073c37cff"
data_git_describe = "v0.0-2465-gf385d4d6"
data_git_msg = """\
commit f385d4d6b1d1a2455baf0bec7cc77d3073c37cff
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Sep 9 18:55:07 2022 +0100

    [dv] Add cpuctrlsts writes to riscv_rand_instr_test
    
    This will have the effect of randomly enabling/disabling
    
     - The ICache
     - Dummy instruction insertion
     - Data independent timing

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

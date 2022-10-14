import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2586"
version_tuple = (0, 0, 2586)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2586")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2444"
data_version_tuple = (0, 0, 2444)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2444")
except ImportError:
    pass
data_git_hash = "d7ce0827790bc2b551f55670103c516257a4ca8c"
data_git_describe = "v0.0-2444-gd7ce0827"
data_git_msg = """\
commit d7ce0827790bc2b551f55670103c516257a4ca8c
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Oct 14 08:29:07 2022 +0100

    [dv] Remove riscv_perf_counter_test
    
    This test doesn't actually check the performance counters, it just runs
    a random instruction test and dumps the performance counters at the end
    for some final checking. That checking does not exist. The test is
    currently broken as well so just remove it as it adds nothing to the
    regression.

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

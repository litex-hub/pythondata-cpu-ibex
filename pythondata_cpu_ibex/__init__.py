import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2258"
version_tuple = (0, 0, 2258)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2258")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2137"
data_version_tuple = (0, 0, 2137)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2137")
except ImportError:
    pass
data_git_hash = "448191dda28321c22bcca0e889d8f755924d5b7c"
data_git_describe = "v0.0-2137-g448191dd"
data_git_msg = """\
commit 448191dda28321c22bcca0e889d8f755924d5b7c
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Jan 11 10:06:21 2022 +0100

    [rtl] Use prim_flop/clock_mux2 primitives for lockstep reset generation
    
    These primitives can serve as anchor points for constraining backend
    tools.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post121"
tool_version_tuple = (0, 0, 121)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post121")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

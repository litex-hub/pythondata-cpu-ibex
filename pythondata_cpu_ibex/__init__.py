import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2326"
version_tuple = (0, 0, 2326)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2326")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2200"
data_version_tuple = (0, 0, 2200)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2200")
except ImportError:
    pass
data_git_hash = "68b56ef0f5c0ba8058e8cb512fe724263ed874f2"
data_git_describe = "v0.0-2200-g68b56ef0"
data_git_msg = """\
commit 68b56ef0f5c0ba8058e8cb512fe724263ed874f2
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Thu Mar 31 13:43:23 2022 +0100

    Include the main C++ file only with Verilator
    
    This is necessary for having VCS support with simple system example.
    Because in the ibex_simple_system_main.cc we are including some
    Verilator exclusive header files.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

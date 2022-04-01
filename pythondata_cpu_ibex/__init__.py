import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2331"
version_tuple = (0, 0, 2331)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2331")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2205"
data_version_tuple = (0, 0, 2205)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2205")
except ImportError:
    pass
data_git_hash = "4a2427cd32de1c1ab39b23c4c62270ddb5209a41"
data_git_describe = "v0.0-2205-g4a2427cd"
data_git_msg = """\
commit 4a2427cd32de1c1ab39b23c4c62270ddb5209a41
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Fri Apr 1 14:20:16 2022 +0100

    Fix cov_report directory in sim.py
    
    Enables us to save coverage groups text file which helps easily see the overall
    coverage in a regression.

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

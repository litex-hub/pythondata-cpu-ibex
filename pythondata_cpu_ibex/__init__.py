import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2452"
version_tuple = (0, 0, 2452)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2452")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2312"
data_version_tuple = (0, 0, 2312)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2312")
except ImportError:
    pass
data_git_hash = "57d810e7fe93d196d12044ace7b7eec5494c60c5"
data_git_describe = "v0.0-2312-g57d810e7"
data_git_msg = """\
commit 57d810e7fe93d196d12044ace7b7eec5494c60c5
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Mon May 23 12:05:12 2022 +0100

    [fcov] Implementing interrupts section of covplan
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

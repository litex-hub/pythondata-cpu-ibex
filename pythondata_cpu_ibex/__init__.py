import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2276"
version_tuple = (0, 0, 2276)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2276")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2150"
data_version_tuple = (0, 0, 2150)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2150")
except ImportError:
    pass
data_git_hash = "5691ef1a45d035105dd4179023ac3befde2e74b3"
data_git_describe = "v0.0-2150-g5691ef1a"
data_git_msg = """\
commit 5691ef1a45d035105dd4179023ac3befde2e74b3
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Feb 15 13:22:10 2022 +0000

    [ci] Bump RISC-V toolchain version to get bitmanip support
    
    This version should have support for bitmanip 1.00+0.93, the version
    that we target in the RTL.

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

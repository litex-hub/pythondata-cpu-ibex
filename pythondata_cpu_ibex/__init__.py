import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2661"
version_tuple = (0, 0, 2661)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2661")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2519"
data_version_tuple = (0, 0, 2519)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2519")
except ImportError:
    pass
data_git_hash = "66b3ed1ac1df79cc6d285e586135fd1e68ab198f"
data_git_describe = "v0.0-2519-g66b3ed1a"
data_git_msg = """\
commit 66b3ed1ac1df79cc6d285e586135fd1e68ab198f
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Fri Oct 28 20:24:31 2022 +0000

    [dv] Add test glitching register file read data
    
    This commit addresses the integrity checking part of #1756 by verifying
    that a glitch on the data read from the register file raises a major
    alert by the core (if the data read from the register file is used by
    the core).
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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

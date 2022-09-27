import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2558"
version_tuple = (0, 0, 2558)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2558")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2416"
data_version_tuple = (0, 0, 2416)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2416")
except ImportError:
    pass
data_git_hash = "7b1be3354d650bc5b23dff6f439459c353288e4f"
data_git_describe = "v0.0-2416-g7b1be335"
data_git_msg = """\
commit 7b1be3354d650bc5b23dff6f439459c353288e4f
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Sep 21 15:25:02 2022 +0100

    [rtl] Don't cache instructions in debug mode
    
    RISC-V debug modules may utilise dynamically changing code. Don't cache
    any instructions in debug mode to correctly support this.
    
    Fixes #1472

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

import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2205"
version_tuple = (0, 0, 2205)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2205")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2093"
data_version_tuple = (0, 0, 2093)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2093")
except ImportError:
    pass
data_git_hash = "cfeef7e864926cf4d30e271a3e2aa5d95e0c141f"
data_git_describe = "v0.0-2093-gcfeef7e8"
data_git_msg = """\
commit cfeef7e864926cf4d30e271a3e2aa5d95e0c141f
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Wed Aug 25 09:19:43 2021 +0100

    [doc] Update DIT documentation for unaligned ld/st
    
    Relates to #1414
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

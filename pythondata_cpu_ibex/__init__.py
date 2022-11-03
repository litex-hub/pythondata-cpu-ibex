import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2653"
version_tuple = (0, 0, 2653)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2653")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2511"
data_version_tuple = (0, 0, 2511)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2511")
except ImportError:
    pass
data_git_hash = "e5a6c9f38cdc5fabcb51b91bc24e1081a93198a0"
data_git_describe = "v0.0-2511-ge5a6c9f3"
data_git_msg = """\
commit e5a6c9f38cdc5fabcb51b91bc24e1081a93198a0
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Thu Nov 3 08:42:16 2022 +0000

    [doc] Add RF write enable glitch detection
    
    This resolves #1893.
    
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

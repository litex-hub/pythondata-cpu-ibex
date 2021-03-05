import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2076"
version_tuple = (0, 0, 2076)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2076")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1981"
data_version_tuple = (0, 0, 1981)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1981")
except ImportError:
    pass
data_git_hash = "6d9e1aca8ad7cf09d4effcde97e471d6c213ead1"
data_git_describe = "v0.0-1981-g6d9e1aca"
data_git_msg = """\
commit 6d9e1aca8ad7cf09d4effcde97e471d6c213ead1
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Thu Mar 4 11:42:59 2021 +0000

    [rtl] Minor lint fix in ibex_core.sv
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

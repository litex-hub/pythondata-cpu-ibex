import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2297"
version_tuple = (0, 0, 2297)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2297")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2171"
data_version_tuple = (0, 0, 2171)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2171")
except ImportError:
    pass
data_git_hash = "3438b77921941ccbf50cba46b3009a6a37203d4b"
data_git_describe = "v0.0-2171-g3438b779"
data_git_msg = """\
commit 3438b77921941ccbf50cba46b3009a6a37203d4b
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Mar 8 12:07:30 2022 +0000

    [rtl] Add minor alert for icache ECC error

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

import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2285"
version_tuple = (0, 0, 2285)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2285")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2159"
data_version_tuple = (0, 0, 2159)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2159")
except ImportError:
    pass
data_git_hash = "302bb6516166b81de80858c5b045680483797328"
data_git_describe = "v0.0-2159-g302bb651"
data_git_msg = """\
commit 302bb6516166b81de80858c5b045680483797328
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Feb 17 14:58:39 2022 +0000

    [doc] Update bitmanip list in integration.rst

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

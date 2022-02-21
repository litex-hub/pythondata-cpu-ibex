import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2287"
version_tuple = (0, 0, 2287)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2287")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2161"
data_version_tuple = (0, 0, 2161)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2161")
except ImportError:
    pass
data_git_hash = "b18eceba81c1427778aa6047e8a5b0c9225f8277"
data_git_describe = "v0.0-2161-gb18eceba"
data_git_msg = """\
commit b18eceba81c1427778aa6047e8a5b0c9225f8277
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Feb 17 18:39:07 2022 +0000

    [rtl] Switch to multi-bit fetch enable
    
    The multi-bit enable aids security hardening. For non secure Ibex all
    but the bottom bit is ignored so it is effectively a single bit enable.

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

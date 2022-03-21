import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2311"
version_tuple = (0, 0, 2311)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2311")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2185"
data_version_tuple = (0, 0, 2185)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2185")
except ImportError:
    pass
data_git_hash = "f44ae900401224c88ed671a5aad738379e3dd11a"
data_git_describe = "v0.0-2185-gf44ae900"
data_git_msg = """\
commit f44ae900401224c88ed671a5aad738379e3dd11a
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Mar 18 13:03:18 2022 +0000

    [doc] Update coverage plan

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

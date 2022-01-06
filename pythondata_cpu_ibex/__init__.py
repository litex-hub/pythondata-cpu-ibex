import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2250"
version_tuple = (0, 0, 2250)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2250")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2133"
data_version_tuple = (0, 0, 2133)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2133")
except ImportError:
    pass
data_git_hash = "a5c55f132e7fa13c37bcaf26934117f928d52822"
data_git_describe = "v0.0-2133-ga5c55f13"
data_git_msg = """\
commit a5c55f132e7fa13c37bcaf26934117f928d52822
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue May 18 17:28:33 2021 +0100

    [dv] Add initial coverage plan

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

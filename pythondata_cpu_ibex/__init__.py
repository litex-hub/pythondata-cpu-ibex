import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2214"
version_tuple = (0, 0, 2214)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2214")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2102"
data_version_tuple = (0, 0, 2102)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2102")
except ImportError:
    pass
data_git_hash = "e70add7228dc9b82c724078475e44e467808175d"
data_git_describe = "v0.0-2102-ge70add72"
data_git_msg = """\
commit e70add7228dc9b82c724078475e44e467808175d
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Oct 21 16:37:43 2021 +0100

    [ci] Add co-simulation testing of CoreMark

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

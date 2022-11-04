import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2655"
version_tuple = (0, 0, 2655)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2655")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2513"
data_version_tuple = (0, 0, 2513)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2513")
except ImportError:
    pass
data_git_hash = "455dbe30f1791ac08ba2a2e9e36f96e0ee294678"
data_git_describe = "v0.0-2513-g455dbe30"
data_git_msg = """\
commit 455dbe30f1791ac08ba2a2e9e36f96e0ee294678
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Nov 2 10:29:28 2022 +0000

    [dv] Add missing isolation forks

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

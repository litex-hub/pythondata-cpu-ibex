import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2563"
version_tuple = (0, 0, 2563)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2563")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2421"
data_version_tuple = (0, 0, 2421)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2421")
except ImportError:
    pass
data_git_hash = "43dc5e85726908cedbc4f3b6798b6ebd8dd1b720"
data_git_describe = "v0.0-2421-g43dc5e85"
data_git_msg = """\
commit 43dc5e85726908cedbc4f3b6798b6ebd8dd1b720
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Mon Oct 3 15:25:49 2022 +0100

    [formal] Added missing prim secded package

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

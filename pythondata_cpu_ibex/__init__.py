import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2216"
version_tuple = (0, 0, 2216)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2216")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2104"
data_version_tuple = (0, 0, 2104)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2104")
except ImportError:
    pass
data_git_hash = "ab4041c43977539323514b35bea1a10546d69b57"
data_git_describe = "v0.0-2104-gab4041c4"
data_git_msg = """\
commit ab4041c43977539323514b35bea1a10546d69b57
Author: Sam Shahrestani <sam.shahrestani@morsemicro.com>
Date:   Sat Nov 13 08:36:42 2021 +1100

    Move NT branch addr calculation to ID stage

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

import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2066"
version_tuple = (0, 0, 2066)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2066")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1975"
data_version_tuple = (0, 0, 1975)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1975")
except ImportError:
    pass
data_git_hash = "faa1e98a6e1cfa8bea95a86d1ba8db5f7818ac0d"
data_git_describe = "v0.0-1975-gfaa1e98a"
data_git_msg = """\
commit faa1e98a6e1cfa8bea95a86d1ba8db5f7818ac0d
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Feb 26 10:04:58 2021 +0000

    [dv] Fix bug in sim.py and type in testlist

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

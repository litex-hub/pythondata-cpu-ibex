import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2584"
version_tuple = (0, 0, 2584)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2584")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2442"
data_version_tuple = (0, 0, 2442)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2442")
except ImportError:
    pass
data_git_hash = "48733e23ec19e68bd334f27fd9b06f667a012ca3"
data_git_describe = "v0.0-2442-g48733e23"
data_git_msg = """\
commit 48733e23ec19e68bd334f27fd9b06f667a012ca3
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Sep 30 17:45:38 2022 +0100

    [rtl] Ignore MIE bit in U mode

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

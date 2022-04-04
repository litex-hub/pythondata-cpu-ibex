import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2334"
version_tuple = (0, 0, 2334)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2334")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2208"
data_version_tuple = (0, 0, 2208)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2208")
except ImportError:
    pass
data_git_hash = "a3b50fb69420f3534a6cd81ba196d4252100a542"
data_git_describe = "v0.0-2208-ga3b50fb6"
data_git_msg = """\
commit a3b50fb69420f3534a6cd81ba196d4252100a542
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Apr 1 17:38:48 2022 +0100

    [doc, fcov] Remove coverpoint names from unimplemented coverage

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

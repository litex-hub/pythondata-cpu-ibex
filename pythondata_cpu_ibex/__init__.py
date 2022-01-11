import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2254"
version_tuple = (0, 0, 2254)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2254")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2136"
data_version_tuple = (0, 0, 2136)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2136")
except ImportError:
    pass
data_git_hash = "756610800bfeee6c211c9b428539d694ea7e39b3"
data_git_describe = "v0.0-2136-g75661080"
data_git_msg = """\
commit 756610800bfeee6c211c9b428539d694ea7e39b3
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Mon Jan 10 17:30:13 2022 +0000

    [doc] Fix config and expand max-width of docs

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

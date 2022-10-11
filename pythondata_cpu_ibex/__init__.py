import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2577"
version_tuple = (0, 0, 2577)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2577")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2435"
data_version_tuple = (0, 0, 2435)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2435")
except ImportError:
    pass
data_git_hash = "08115056f9da99f5df14d72d0909e1637bdd25b5"
data_git_describe = "v0.0-2435-g08115056"
data_git_msg = """\
commit 08115056f9da99f5df14d72d0909e1637bdd25b5
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Mon Oct 10 12:20:19 2022 +0100

    [doc] Add NAPOT address mode to coverage plan

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

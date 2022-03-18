import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2310"
version_tuple = (0, 0, 2310)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2310")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2184"
data_version_tuple = (0, 0, 2184)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2184")
except ImportError:
    pass
data_git_hash = "07a49045fb303cf44f902485acc07f8172ff615a"
data_git_describe = "v0.0-2184-g07a49045"
data_git_msg = """\
commit 07a49045fb303cf44f902485acc07f8172ff615a
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Mon Mar 14 18:09:21 2022 +0000

    [ibex, dv] Removed extra hierarchy of ic_top inside icache TB
    
    This commit removes extra hierarchy of ic_top inside icache TB and moves
    the scrambling request generation logic and instantiation of data and
    tag RAMs to tb.

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

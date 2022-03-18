import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2307"
version_tuple = (0, 0, 2307)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2307")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2181"
data_version_tuple = (0, 0, 2181)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2181")
except ImportError:
    pass
data_git_hash = "6bb67e20f8a7c670e4baf5fe8f130a5ef360f411"
data_git_describe = "v0.0-2181-g6bb67e20"
data_git_msg = """\
commit 6bb67e20f8a7c670e4baf5fe8f130a5ef360f411
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Mon Mar 14 16:55:58 2022 +0000

    [icache, dv] Added scrambling agent to verify scrambling in RAMs
    
    This commit adds a new scrambling agent to drive scrambling key and
    valid to the data and tag memory interfaces.
    
    Update lowrisc_ip to lowRISC/opentitan@7c4f8b3fd
    
    Update code from upstream repository
    https://github.com/lowRISC/opentitan to revision
    7c4f8b3fde4bb625ac3330ff52d3f66507190fe5
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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

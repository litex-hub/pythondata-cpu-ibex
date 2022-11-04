import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2664"
version_tuple = (0, 0, 2664)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2664")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2522"
data_version_tuple = (0, 0, 2522)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2522")
except ImportError:
    pass
data_git_hash = "7b0921e14cca9bcba02e9492b22f9a185dbfdc7a"
data_git_describe = "v0.0-2522-g7b0921e1"
data_git_msg = """\
commit 7b0921e14cca9bcba02e9492b22f9a185dbfdc7a
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Fri Oct 28 10:09:02 2022 +0000

    [dv] Add test glitching icache data or tag
    
    This commit addresses the integrity part of #1759 by verifying that a
    glitch on the data or tag response from the instruction cache raises a
    minor alert by the core (if the data/tag returned from the cache is used
    by the core).
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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

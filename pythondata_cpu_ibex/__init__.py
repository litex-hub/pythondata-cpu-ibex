import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2294"
version_tuple = (0, 0, 2294)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2294")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2168"
data_version_tuple = (0, 0, 2168)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2168")
except ImportError:
    pass
data_git_hash = "af0c0278670225b70d3f9afcb9a6e6ed2e5d8bd9"
data_git_describe = "v0.0-2168-gaf0c0278"
data_git_msg = """\
commit af0c0278670225b70d3f9afcb9a6e6ed2e5d8bd9
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Thu Feb 24 15:03:11 2022 +0000

    [ibex, dv] Makes delays between req, gnt and rvalid configurable
    
    This commit adds functionalty to the memory response agent to make delays more
    configurable.
    There are two delays
    - Delay between req and gnt
    - Delay between gnt and rvalid
    
    For each of these delays we have three modes:
    * Fully random delay
    * Fixed delay
    * Biased delay. Randomised delays but allow biasing towards 0 delay, to give a mix of runs with back
    to back transfers with no delay and some with delays.
    
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

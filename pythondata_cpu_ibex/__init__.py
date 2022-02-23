import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2289"
version_tuple = (0, 0, 2289)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2289")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2163"
data_version_tuple = (0, 0, 2163)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2163")
except ImportError:
    pass
data_git_hash = "58bc6f27ab28ce52e4ae35fd455efb15e1adc645"
data_git_describe = "v0.0-2163-g58bc6f27"
data_git_msg = """\
commit 58bc6f27ab28ce52e4ae35fd455efb15e1adc645
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Feb 22 16:55:29 2022 +0000

    [doc] Add details about icache latency to DIT docs
    
    When the icache is enabled and data independent timing is required
    variable fetch latency due to cache hit or miss may introduce
    undesirable timing behaviour. This adds explicit mention of this to the
    documentation.

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

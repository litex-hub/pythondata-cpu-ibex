import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2348"
version_tuple = (0, 0, 2348)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2348")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2222"
data_version_tuple = (0, 0, 2222)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2222")
except ImportError:
    pass
data_git_hash = "9b52fc132adfabf533e01dea86d045354498f49b"
data_git_describe = "v0.0-2222-g9b52fc13"
data_git_msg = """\
commit 9b52fc132adfabf533e01dea86d045354498f49b
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Thu Apr 7 12:22:33 2022 +0100

    Handle stdstreams from submakefile commands cleanly
    
    Some commands utilise a logfile argument, while others capture the stdstreams
    into a file. Discard the stdout/stderr when a logfile argument is used.
    This keeps the logs readable.

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

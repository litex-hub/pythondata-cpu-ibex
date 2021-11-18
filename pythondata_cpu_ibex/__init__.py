import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2217"
version_tuple = (0, 0, 2217)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2217")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2105"
data_version_tuple = (0, 0, 2105)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2105")
except ImportError:
    pass
data_git_hash = "1bbe27effeda63f34c4f5c06cc88da58f9c5a404"
data_git_describe = "v0.0-2105-g1bbe27ef"
data_git_msg = """\
commit 1bbe27effeda63f34c4f5c06cc88da58f9c5a404
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Thu Nov 18 15:16:08 2021 +0000

    [dv/icache] Add missing window reset call
    
    The cache hit-rate tracking logic needs to be reset on every
    invalidation.
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

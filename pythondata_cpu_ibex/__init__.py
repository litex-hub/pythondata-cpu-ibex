import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2277"
version_tuple = (0, 0, 2277)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2277")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2151"
data_version_tuple = (0, 0, 2151)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2151")
except ImportError:
    pass
data_git_hash = "6f6cafaa4d09d0c227966645b00ce0d34fd03175"
data_git_describe = "v0.0-2151-g6f6cafaa"
data_git_msg = """\
commit 6f6cafaa4d09d0c227966645b00ce0d34fd03175
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Feb 15 15:50:46 2022 +0000

    [ci] Bump Spike version to get cosim implementation
    
    This will only have an effect on our private CI, which picks up this
    spike build from the toolnas. The build is the ibex_cosim branch,
    which contains the stuff we need for the recent cosim support. It's
    also new enough to support the v1.0+0.93 bitmanip flavour that we
    support in the RTL.

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

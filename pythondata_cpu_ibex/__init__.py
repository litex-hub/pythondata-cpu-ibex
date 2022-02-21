import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2286"
version_tuple = (0, 0, 2286)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2286")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2160"
data_version_tuple = (0, 0, 2160)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2160")
except ImportError:
    pass
data_git_hash = "3475b9106c21c99d0289034bc1e0736c6833ef59"
data_git_describe = "v0.0-2160-g3475b910"
data_git_msg = """\
commit 3475b9106c21c99d0289034bc1e0736c6833ef59
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Feb 18 12:48:50 2022 +0000

    Refer to a specific tag for the ibex-cosim version of Spike
    
    We're going to want to make a couple more releases of Spike, cleaving
    a bit closer to the upstream repository. Let's be explicit about which
    version people should get.

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

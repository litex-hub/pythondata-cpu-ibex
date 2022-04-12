import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2342"
version_tuple = (0, 0, 2342)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2342")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2216"
data_version_tuple = (0, 0, 2216)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2216")
except ImportError:
    pass
data_git_hash = "1f6bcb9ab5029225b606bf42ff3b61b2fddeed2b"
data_git_describe = "v0.0-2216-g1f6bcb9a"
data_git_msg = """\
commit 1f6bcb9ab5029225b606bf42ff3b61b2fddeed2b
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 24 16:16:56 2022 +0000

    [dv] Remove support for building against ibex-cosim-v0.1

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

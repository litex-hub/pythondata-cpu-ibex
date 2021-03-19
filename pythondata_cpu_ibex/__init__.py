import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2086"
version_tuple = (0, 0, 2086)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2086")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1991"
data_version_tuple = (0, 0, 1991)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1991")
except ImportError:
    pass
data_git_hash = "4b43afa53315d00784d5c3b714583276127eddcc"
data_git_describe = "v0.0-1991-g4b43afa5"
data_git_msg = """\
commit 4b43afa53315d00784d5c3b714583276127eddcc
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Mar 18 16:18:56 2021 +0000

    [doc] Fix table rendering for `mseccfg`

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2290"
version_tuple = (0, 0, 2290)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2290")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2164"
data_version_tuple = (0, 0, 2164)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2164")
except ImportError:
    pass
data_git_hash = "0f69d4972c5184e8c8de41c4002fb914ef3ce10f"
data_git_describe = "v0.0-2164-g0f69d497"
data_git_msg = """\
commit 0f69d4972c5184e8c8de41c4002fb914ef3ce10f
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Feb 24 12:59:21 2022 +0000

    [dv] Add X assertions for top-level IO
    
    Ensure all top-level inputs and outputs are known when they are
    expected to be known.

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

import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2249"
version_tuple = (0, 0, 2249)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2249")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2132"
data_version_tuple = (0, 0, 2132)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2132")
except ImportError:
    pass
data_git_hash = "410ffd349da1d4c13f77b208bb3b93adb154fac0"
data_git_describe = "v0.0-2132-g410ffd34"
data_git_msg = """\
commit 410ffd349da1d4c13f77b208bb3b93adb154fac0
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Dec 10 22:16:07 2021 +0100

    [bitmanip, doc] Update info on bitmanip support and area numbers
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

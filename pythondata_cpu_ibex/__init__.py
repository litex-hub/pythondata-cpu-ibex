import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2337"
version_tuple = (0, 0, 2337)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2337")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2211"
data_version_tuple = (0, 0, 2211)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2211")
except ImportError:
    pass
data_git_hash = "a3e5eebffa9eb1aed3d04f229299aa7da8e7195e"
data_git_describe = "v0.0-2211-ga3e5eebf"
data_git_msg = """\
commit a3e5eebffa9eb1aed3d04f229299aa7da8e7195e
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Mon Apr 4 10:22:46 2022 +0100

    [dv,fcov] Timeout fix + removing .ccf from yaml
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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

import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2280"
version_tuple = (0, 0, 2280)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2280")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2154"
data_version_tuple = (0, 0, 2154)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2154")
except ImportError:
    pass
data_git_hash = "a46ff074890a3bed70cc3a13b1c072e91ff488e6"
data_git_describe = "v0.0-2154-ga46ff074"
data_git_msg = """\
commit a46ff074890a3bed70cc3a13b1c072e91ff488e6
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Feb 15 16:58:20 2022 +0100

    [rtl] Fix AscentLint errors
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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

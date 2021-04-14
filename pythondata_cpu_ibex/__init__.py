import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2107"
version_tuple = (0, 0, 2107)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2107")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2012"
data_version_tuple = (0, 0, 2012)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2012")
except ImportError:
    pass
data_git_hash = "69e715b2878c1ee7fdca2c3d1ed3396e6bdadb64"
data_git_describe = "v0.0-2012-g69e715b2"
data_git_msg = """\
commit 69e715b2878c1ee7fdca2c3d1ed3396e6bdadb64
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Mon Apr 12 11:57:18 2021 +0100

    [dv] Improvements to functional coverage
    
    This adds more instruction categories and corrects various issues in the
    categorization code. Further cross coverage has been added including
    illegal bins to remove bins that cannot occur.
    
    The concept of using SVAs with cross coverage has been dropped. The
    systemverilog scheduling model makes the concept unworkable.

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

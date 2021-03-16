import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2082"
version_tuple = (0, 0, 2082)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2082")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1987"
data_version_tuple = (0, 0, 1987)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1987")
except ImportError:
    pass
data_git_hash = "62b1a30c7d0d8fa60a0476d896fec7551cb4c96f"
data_git_describe = "v0.0-1987-g62b1a30c"
data_git_msg = """\
commit 62b1a30c7d0d8fa60a0476d896fec7551cb4c96f
Author: Yusef Karim <48184686+yusefkarim@users.noreply.github.com>
Date:   Mon Mar 15 16:25:50 2021 -0400

    Fix spacing for bullet points to appear
    
    Bullet points now appear properly for the last paragraph under the Data Independent Timing section.

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

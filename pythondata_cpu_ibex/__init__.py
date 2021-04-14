import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2109"
version_tuple = (0, 0, 2109)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2109")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2014"
data_version_tuple = (0, 0, 2014)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2014")
except ImportError:
    pass
data_git_hash = "48a886a25fc788ea4529872047811f79bca4877f"
data_git_describe = "v0.0-2014-g48a886a2"
data_git_msg = """\
commit 48a886a25fc788ea4529872047811f79bca4877f
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Tue Feb 9 15:35:59 2021 +0000

    Update README to match design
    
    Since this part of the README was written the design moved on. Let's
    update it. This update follows the text we have at
    https://ibex-core.readthedocs.io/en/latest/index.html.

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

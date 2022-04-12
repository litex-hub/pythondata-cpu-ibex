import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2344"
version_tuple = (0, 0, 2344)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2344")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2218"
data_version_tuple = (0, 0, 2218)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2218")
except ImportError:
    pass
data_git_hash = "2ae62c145ca2d798d29faaf16f7b171c776430dd"
data_git_describe = "v0.0-2218-g2ae62c14"
data_git_msg = """\
commit 2ae62c145ca2d798d29faaf16f7b171c776430dd
Author: mbaykenar <aykenar.burak@gmail.com>
Date:   Tue Apr 12 16:37:08 2022 +0300

    assign irq_nm_int_cause to all zeros

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

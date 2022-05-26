import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2447"
version_tuple = (0, 0, 2447)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2447")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2311"
data_version_tuple = (0, 0, 2311)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2311")
except ImportError:
    pass
data_git_hash = "97a949df0283fbae223372f592287f275ae869f7"
data_git_describe = "v0.0-2311-g97a949df"
data_git_msg = """\
commit 97a949df0283fbae223372f592287f275ae869f7
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Tue May 17 16:46:58 2022 +0100

    [doc] Update coverage plan to point crosses/cp's
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post136"
tool_version_tuple = (0, 0, 136)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post136")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

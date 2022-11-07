import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2665"
version_tuple = (0, 0, 2665)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2665")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2523"
data_version_tuple = (0, 0, 2523)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2523")
except ImportError:
    pass
data_git_hash = "bd8bee8a729cdc6e26d81061ef3c1f2eba49513f"
data_git_describe = "v0.0-2523-gbd8bee8a"
data_git_msg = """\
commit bd8bee8a729cdc6e26d81061ef3c1f2eba49513f
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Fri Nov 4 17:40:25 2022 +0000

    [dv] Don't set sync_exc_seen in Debug Mode
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

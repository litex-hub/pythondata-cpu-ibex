import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2642"
version_tuple = (0, 0, 2642)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2642")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2500"
data_version_tuple = (0, 0, 2500)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2500")
except ImportError:
    pass
data_git_hash = "c145ac398539d40ddec533d192dc39dc0cdcd4bd"
data_git_describe = "v0.0-2500-gc145ac39"
data_git_msg = """\
commit c145ac398539d40ddec533d192dc39dc0cdcd4bd
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Fri Oct 28 23:51:32 2022 +0100

    [dv] Add a matching NA4 in pmp_full_random_test
    
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

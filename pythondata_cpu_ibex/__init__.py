import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2625"
version_tuple = (0, 0, 2625)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2625")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2483"
data_version_tuple = (0, 0, 2483)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2483")
except ImportError:
    pass
data_git_hash = "eca86aef03539bc297ab4879c58a33632d8c48e3"
data_git_describe = "v0.0-2483-geca86aef"
data_git_msg = """\
commit eca86aef03539bc297ab4879c58a33632d8c48e3
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Sat Oct 29 10:58:39 2022 +0100

    [rtl] Fix id_exception_o signal
    
    Previously it was asserted when an instruction in ID would cause an
    exception but an earlier instruction in WB also causes an exception
    which takes priority.
    
    This didn't cause a functional bug as the `id_exception_o` signal was
    used in a single place ORed with `wb_exception_o`. However it was
    confusing behaviour and could cause killed instructions to appear on the
    RVFI causing false cosim mismatches.

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

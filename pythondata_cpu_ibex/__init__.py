import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2556"
version_tuple = (0, 0, 2556)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2556")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2414"
data_version_tuple = (0, 0, 2414)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2414")
except ImportError:
    pass
data_git_hash = "d35ff67df650633795ead001ea5f285c44b73078"
data_git_describe = "v0.0-2414-gd35ff67d"
data_git_msg = """\
commit d35ff67df650633795ead001ea5f285c44b73078
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Sep 22 22:19:33 2022 +0100

    [dv] Fix timeout issues
    
    core_ibex_directed_test has a 'disable fork' that was killing processes
    that were running sequences. Another part of the testbench waits for
    those sequences to finish. When this 'disable fork' happens too early
    the sequences are killed before they finish so the testbench never
    terminated and times out. Instead ensure the sequences have finished
    before doing the 'disable fork'.

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

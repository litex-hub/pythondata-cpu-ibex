import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2478"
version_tuple = (0, 0, 2478)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2478")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2336"
data_version_tuple = (0, 0, 2336)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2336")
except ImportError:
    pass
data_git_hash = "a6c182e7be504c20ccd38b5fe5f3a345574aa390"
data_git_describe = "v0.0-2336-ga6c182e7"
data_git_msg = """\
commit a6c182e7be504c20ccd38b5fe5f3a345574aa390
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Fri Jul 22 14:39:14 2022 +0100

    [dv,test] Fix race condition to catch ecall
    
    We already have a clocking block inside dut_if. This commit uses it
    to avoid a race condition that happens when `instr_valid_i` goes high
    while `ecall_insn_i` goes low.
    
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

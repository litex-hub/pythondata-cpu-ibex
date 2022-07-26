import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2485"
version_tuple = (0, 0, 2485)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2485")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2343"
data_version_tuple = (0, 0, 2343)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2343")
except ImportError:
    pass
data_git_hash = "7bae3b7ba34d9611bc263d84bd358ec5021f82d3"
data_git_describe = "v0.0-2343-g7bae3b7b"
data_git_msg = """\
commit 7bae3b7ba34d9611bc263d84bd358ec5021f82d3
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Mon Jul 25 09:41:33 2022 +0100

    [dv,fcov] Fix `cp_mem_raw_hz` implementation
    
    This commit fixes how we catch an instruction at WB stage. Before this fix
    we were effectively checking opcode of decoded instruction instead.
    
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

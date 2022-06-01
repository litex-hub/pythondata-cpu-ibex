import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2456"
version_tuple = (0, 0, 2456)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2456")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2314"
data_version_tuple = (0, 0, 2314)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2314")
except ImportError:
    pass
data_git_hash = "ea4e9383dbc6614e811ebe0b55cdb14779aee7ca"
data_git_describe = "v0.0-2314-gea4e9383"
data_git_msg = """\
commit ea4e9383dbc6614e811ebe0b55cdb14779aee7ca
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Tue May 31 16:32:18 2022 +0100

    [syn] Use sv2v for prim_generic_buf
    
    Convert `prim_generic_buf` to Verilog as well.
    Also, replace 'prim_buf' with 'prim_generic_buf' whenever we see a
    `prim_buf` in a generated Verilog file.
    
    Fixes #1557
    
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

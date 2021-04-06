import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2099"
version_tuple = (0, 0, 2099)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2099")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2004"
data_version_tuple = (0, 0, 2004)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2004")
except ImportError:
    pass
data_git_hash = "a799a92e5eef5fbaa7b2a3054c88e5e48260f04f"
data_git_describe = "v0.0-2004-ga799a92e"
data_git_msg = """\
commit a799a92e5eef5fbaa7b2a3054c88e5e48260f04f
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Apr 6 15:12:47 2021 +0200

    [rtl] Add SVA to ensure valid_i in compressed decoder is known
    
    This signal is used to gate several assertions related to
    unknown/invalid selector signals. We want to be sure to catch any X
    values entering the compressed decoder and ultimately ID.
    
    This is related to lowRISC/Ibex#540.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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

import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2095"
version_tuple = (0, 0, 2095)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2095")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2000"
data_version_tuple = (0, 0, 2000)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2000")
except ImportError:
    pass
data_git_hash = "c7f44557d2e14810889b9bcf853495b4a9a4f124"
data_git_describe = "v0.0-2000-gc7f44557"
data_git_msg = """\
commit c7f44557d2e14810889b9bcf853495b4a9a4f124
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Apr 5 12:35:06 2021 +0100

    Fix initialisation in ibex_icache_env_cfg.sv

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

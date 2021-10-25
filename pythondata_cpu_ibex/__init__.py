import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2206"
version_tuple = (0, 0, 2206)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2206")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2094"
data_version_tuple = (0, 0, 2094)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2094")
except ImportError:
    pass
data_git_hash = "d1aff2f1a418662d4498494ffd54f57de64e07fb"
data_git_describe = "v0.0-2094-gd1aff2f1"
data_git_msg = """\
commit d1aff2f1a418662d4498494ffd54f57de64e07fb
Author: Miguel Escobar <mescoba1@github.com>
Date:   Wed Feb 24 11:28:18 2021 -0800

    [dv] get ibex dv co-sim to run w questa
    
    This resolves lowRISC/Ibex#1280.

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

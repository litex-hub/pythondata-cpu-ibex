import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2080"
version_tuple = (0, 0, 2080)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2080")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1985"
data_version_tuple = (0, 0, 1985)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1985")
except ImportError:
    pass
data_git_hash = "42827fc9cd0b2043d5d179cae46b0238a55d3652"
data_git_describe = "v0.0-1985-g42827fc9"
data_git_msg = """\
commit 42827fc9cd0b2043d5d179cae46b0238a55d3652
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Wed Mar 10 14:07:28 2021 +0000

    [rtl/icache] Switch ECC granularity to 32bits
    
    Changes the ECC granularity in the data RAMs from 64bit to 32bit. This
    is to align with an upcoming change in bus ECC. Relates to
    lowRISC/opentitan#5450
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

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

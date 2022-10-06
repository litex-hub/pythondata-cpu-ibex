import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2571"
version_tuple = (0, 0, 2571)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2571")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2429"
data_version_tuple = (0, 0, 2429)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2429")
except ImportError:
    pass
data_git_hash = "7ab2571bea0daca3f14155d82f0124fb0b118799"
data_git_describe = "v0.0-2429-g7ab2571b"
data_git_msg = """\
commit 7ab2571bea0daca3f14155d82f0124fb0b118799
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Wed Oct 5 18:28:35 2022 +0100

    [if,pmp] Check second bit instead of third for instruction alignment
    
    Signed-off-by: Marno van der Maas <mvdmaas+git@lowrisc.org>

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

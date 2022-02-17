import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2282"
version_tuple = (0, 0, 2282)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2282")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2156"
data_version_tuple = (0, 0, 2156)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2156")
except ImportError:
    pass
data_git_hash = "9943f9a42c36062f86f84cc1082e6995b8d328e4"
data_git_describe = "v0.0-2156-g9943f9a4"
data_git_msg = """\
commit 9943f9a42c36062f86f84cc1082e6995b8d328e4
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Feb 17 13:50:08 2022 +0000

    [rtl, doc] Seperate major alert into internal and bus
    
    This is to allow more consistent signalling in systems that integrate
    Ibex (e.g. OpenTitan) so bus integrity errors external to Ibex and one's
    detected within Ibex can be fed into the same alert whilst seperating
    out Ibex's various internal alert causes.

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

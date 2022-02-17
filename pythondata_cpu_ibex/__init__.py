import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2281"
version_tuple = (0, 0, 2281)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2281")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2155"
data_version_tuple = (0, 0, 2155)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2155")
except ImportError:
    pass
data_git_hash = "e84e7de53f326809a6bc11e1ba7cdb440d60719a"
data_git_describe = "v0.0-2155-ge84e7de5"
data_git_msg = """\
commit e84e7de53f326809a6bc11e1ba7cdb440d60719a
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Feb 16 12:57:47 2022 +0000

    Fix narrowing conversion warning in cosim_dpi.cc

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

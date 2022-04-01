import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2332"
version_tuple = (0, 0, 2332)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2332")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2206"
data_version_tuple = (0, 0, 2206)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2206")
except ImportError:
    pass
data_git_hash = "ead2174c1a319a21fd35d81bad4af81187b509fb"
data_git_describe = "v0.0-2206-gead2174c"
data_git_msg = """\
commit ead2174c1a319a21fd35d81bad4af81187b509fb
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Mar 23 16:49:47 2022 +0000

    Introduce internal interrupt concept
    
    An internal interrupt triggers an NMI. A single one is implemented, one
    on integrity errors being seen in load data. This replaces a synchronous
    exception on an integrity error which caused timing issues.

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

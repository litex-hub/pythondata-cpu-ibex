import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2265"
version_tuple = (0, 0, 2265)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2265")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2143"
data_version_tuple = (0, 0, 2143)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2143")
except ImportError:
    pass
data_git_hash = "97fa5cf28024b882ffa1acbe81f6b6c865715840"
data_git_describe = "v0.0-2143-g97fa5cf2"
data_git_msg = """\
commit 97fa5cf28024b882ffa1acbe81f6b6c865715840
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Jan 21 17:10:10 2022 +0000

    [rtl,doc] Add customisable PMP reset values
    
    Fixes #1423

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2315"
version_tuple = (0, 0, 2315)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2315")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2189"
data_version_tuple = (0, 0, 2189)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2189")
except ImportError:
    pass
data_git_hash = "36d77ab0c5ba7d268bd7b7638c0dd68e1f2c0124"
data_git_describe = "v0.0-2189-g36d77ab0"
data_git_msg = """\
commit 36d77ab0c5ba7d268bd7b7638c0dd68e1f2c0124
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Mar 18 19:27:57 2022 +0000

    [ci] Fix coremark cosim job
    
    Actually fail the job if there's an error

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

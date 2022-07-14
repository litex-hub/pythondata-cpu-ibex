import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2466"
version_tuple = (0, 0, 2466)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2466")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2324"
data_version_tuple = (0, 0, 2324)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2324")
except ImportError:
    pass
data_git_hash = "3459d7f8dfd1a4d49a0a70659b22c77fdd7bc5c9"
data_git_describe = "v0.0-2324-g3459d7f8"
data_git_msg = """\
commit 3459d7f8dfd1a4d49a0a70659b22c77fdd7bc5c9
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Mon Jul 11 14:46:23 2022 +0100

    [lint] Remove whitespace from non-vendored source files
    
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

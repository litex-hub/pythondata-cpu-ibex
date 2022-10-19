import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2598"
version_tuple = (0, 0, 2598)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2598")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2456"
data_version_tuple = (0, 0, 2456)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2456")
except ImportError:
    pass
data_git_hash = "73e46b4fc702e5ab31cbd8e4446ec9e6ce756abc"
data_git_describe = "v0.0-2456-g73e46b4f"
data_git_msg = """\
commit 73e46b4fc702e5ab31cbd8e4446ec9e6ce756abc
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Tue Oct 18 18:00:48 2022 +0100

    [fcov,pmp] Illegal PMP write coverpoints check dside request error not low

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

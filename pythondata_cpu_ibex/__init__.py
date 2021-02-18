import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2060"
version_tuple = (0, 0, 2060)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2060")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1969"
data_version_tuple = (0, 0, 1969)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1969")
except ImportError:
    pass
data_git_hash = "65287f7d7b5a9b0733f37c01b292b1de08656e5c"
data_git_describe = "v0.0-1969-g65287f7d"
data_git_msg = """\
commit 65287f7d7b5a9b0733f37c01b292b1de08656e5c
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Thu Feb 18 11:31:46 2021 +0000

    Fix deprecated sphinx html_context usage in conf.py
    
    We were using the old html_context which has been deprecated
    for a while. This PR switches to html_css_files instead.
    See sphinx-doc/sphinx#8885 for more information.

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

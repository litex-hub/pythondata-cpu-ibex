import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2198"
version_tuple = (0, 0, 2198)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2198")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2086"
data_version_tuple = (0, 0, 2086)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2086")
except ImportError:
    pass
data_git_hash = "0aa02b0f3fd3a49a12e5ce9dcc9bcfeef1e61c9d"
data_git_describe = "v0.0-2086-g0aa02b0f"
data_git_msg = """\
commit 0aa02b0f3fd3a49a12e5ce9dcc9bcfeef1e61c9d
Author: Zachary Snow <zach@zachjs.com>
Date:   Wed Oct 6 11:43:09 2021 -0600

    [syn] Use read_verilog -defer in yosys_run_synth.tcl
    
    Newer versions of sv2v carry through elaboration system tasks like
    $fatal. ibex_top_tracing uses $fatal, but isn't actually used in the
    syn_yosys flow. By using -defer, unused modules like ibex_top_tracing
    are not elaborated in Yosys.

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

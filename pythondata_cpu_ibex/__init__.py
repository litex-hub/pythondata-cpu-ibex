import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2321"
version_tuple = (0, 0, 2321)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2321")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2195"
data_version_tuple = (0, 0, 2195)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2195")
except ImportError:
    pass
data_git_hash = "98931c7dff32c3177c8b3ad45e558d4f04320ef2"
data_git_describe = "v0.0-2195-g98931c7d"
data_git_msg = """\
commit 98931c7dff32c3177c8b3ad45e558d4f04320ef2
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Mon Mar 28 14:52:44 2022 +0100

    Remove logfile param in Ibex RTL Sim for Xcelium
    
    Fixes a bug where both Xcelium and Python open the same sim.log file and race to
    write the simulation results into it. This change makes Python the sole writer of this
    file using the captured stdout/stderr from the subprocess.run call in
    run_rtl.py.
    
    This bug was also previously present for VCS but was fixed in 90ff7ca6c.

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

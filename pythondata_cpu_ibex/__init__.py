import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2937"
version_tuple = (0, 0, 2937)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2937")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2787"
data_version_tuple = (0, 0, 2787)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2787")
except ImportError:
    pass
data_git_hash = "5da1679f360b00ae330aab33cc8d79d73dfabb98"
data_git_describe = "v0.0-2787-g5da1679f360b"
data_git_msg = """\
commit 5da1679f360b00ae330aab33cc8d79d73dfabb98
Author: Robert Schilling <rschilling@rivosinc.com>
Date:   Thu Jan 9 20:34:42 2025 +0100

    [ibex_tracer] Use static variables in always/final blocks
    
    Signed-off-by: Robert Schilling <rschilling@rivosinc.com>

"""

# Tool version info
tool_version_str = "0.0.post150"
tool_version_tuple = (0, 0, 150)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post150")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

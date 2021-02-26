import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2063"
version_tuple = (0, 0, 2063)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2063")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1972"
data_version_tuple = (0, 0, 1972)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1972")
except ImportError:
    pass
data_git_hash = "c3bd4fa7ef5143045f8dc15d56b342a62f83cb86"
data_git_describe = "v0.0-1972-gc3bd4fa7"
data_git_msg = """\
commit c3bd4fa7ef5143045f8dc15d56b342a62f83cb86
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Jan 26 16:37:20 2021 +0000

    [rtl] Remove paths between dmem and imem signals
    
    Prior to this change Ibex had multiple feedthrough paths from the data
    memory interface to the instruction memory interface. This existed
    because Ibex would hold off doing a instruction fetch for a jump or
    branch if there was a outstanding memory request. It would wait for the
    response to be available so either the jump or branch would occur or an
    exception was taken.
    
    With this change the branch or jump will speculatively begin the
    instruction fetch whilst there is an outstanding memory request. Should
    an exception result from the memory request the fetch will be discarded
    and the exception taken as normal.
    
    An alternative fix would not factor the data error response
    (data_err_i) directly into the controller logic for branches and jumps.
    With this option new stall cycles would be introduced anywhere a branch
    or jump immediately follows a memory instruction which would have an
    adverse impact on performance.

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

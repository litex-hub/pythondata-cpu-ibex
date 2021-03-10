import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2077"
version_tuple = (0, 0, 2077)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2077")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1982"
data_version_tuple = (0, 0, 1982)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1982")
except ImportError:
    pass
data_git_hash = "70c3702421feccc0774a9a948aebe94cfa289623"
data_git_describe = "v0.0-1982-g70c37024"
data_git_msg = """\
commit 70c3702421feccc0774a9a948aebe94cfa289623
Author: Udi Jonnalagadda <udij@google.com>
Date:   Fri Mar 5 15:09:39 2021 -0800

    [dv/ibex] filter out tests on a per-config basis
    
    This PR adds functionality to filter out tests during regressions for a
    particular config.
    
    e.g. if a full regression is kicked off using the `small` config, we
    don't want to attempt to run any PMP and bitmanip tests as the RTL
    parameter-set will not support it.
    
    To do this, a new YAML field called `rtl_params` is added to relevant
    test entries, to indicate what parameters (if any) are required to be
    able to run the particular test, along with the required value of said
    parameters.
    
    `sim.py` will then parse this field (if it exists), and using
    information from `ibex_configs.yaml` pertaining to the current config,
    will remove tests from being run on-the-fly.
    
    This also gives us the convenient side effect of not having to re-run
    instruction generation if there is a parameter/config mismatch, we can
    just rerun the RTL compilation and simulation stages safely.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn

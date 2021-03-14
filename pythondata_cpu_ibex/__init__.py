import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2081"
version_tuple = (0, 0, 2081)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2081")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1986"
data_version_tuple = (0, 0, 1986)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1986")
except ImportError:
    pass
data_git_hash = "6576247a1ee68baf4d1abd43e04a5bfdde169ecb"
data_git_describe = "v0.0-1986-g6576247a"
data_git_msg = """\
commit 6576247a1ee68baf4d1abd43e04a5bfdde169ecb
Author: Udi Jonnalagadda <udij@google.com>
Date:   Fri Mar 12 17:55:39 2021 -0800

    [ci/ibex] temporarily remove pmp_full_random_test
    
    this test is arbitrarily failing in regressions on a Spike timeout,
    temporarily remove this to avoid blocking.
    
    @udinator to fix this in the near future.
    
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

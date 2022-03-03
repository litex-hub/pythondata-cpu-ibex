import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2292"
version_tuple = (0, 0, 2292)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2292")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2166"
data_version_tuple = (0, 0, 2166)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2166")
except ImportError:
    pass
data_git_hash = "c15f3b88883781808eaa96bda205a9bdaff5eb98"
data_git_describe = "v0.0-2166-gc15f3b88"
data_git_msg = """\
commit c15f3b88883781808eaa96bda205a9bdaff5eb98
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Mar 2 23:46:26 2022 +0000

    [icache] Define some fake DPI functions to simplify linking
    
    This is triggered by the fact that if the ICache parameter is false
    then we don't instantiate the ibex_icache module. For verilator
    simulations, the module is then discarded entirely, which means that
    its two DPI functions are not defined. That's unfortunate because
    we're also compiling the code in scrambled_ecc32_mem_area.cc, which
    expects the functions to be defined.
    
    The obvious solution (don't include scrambled_ecc32_mem_area.cc if you
    don't have an icache) isn't easy to do, because FuseSoc doesn't
    currently allow us to use parameters to configure its dependency
    tree (see fusesoc issue 438 for a discussion).
    
    The super-clever solution that I came up with before(!) was to declare
    these symbols as weak in the C++ code. That way, we can do a runtime
    check to make sure that no-one is silly enough to call them without an
    icache, but everything will still build properly either way.
    
    Unfortunately, that doesn't work well with xcelium simulations.
    Xcelium turns out to compile all the C++ code into one .so library and
    generate functions for exported DPI functions in another. These two
    solibs then get loaded at runtime with dlopen(). But this doesn't work
    with weak symbols: in fact, it seems you end up with the C++ version
    every time. Boo!
    
    So let's be stupider about it and define (bogus) versions of the DPI
    functions in this case. Fortunately, both of them are designed to
    return zero on failure so we can just return zero and needn't worry
    too much.
    
    The idea is that when this lands, we can revert the OpenTitan change
    that switched the C++ code to using weak symbols and Xcelium
    simulations will start working.

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

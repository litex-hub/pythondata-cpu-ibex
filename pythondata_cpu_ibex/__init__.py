import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2071"
version_tuple = (0, 0, 2071)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2071")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1980"
data_version_tuple = (0, 0, 1980)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1980")
except ImportError:
    pass
data_git_hash = "53634991906dbf0efde1018b6a6fb46801d75277"
data_git_describe = "v0.0-1980-g53634991"
data_git_msg = """\
commit 53634991906dbf0efde1018b6a6fb46801d75277
Author: Vladimir Rozic <vrozic@lowrisc.org>
Date:   Wed Mar 3 14:10:39 2021 +0000

    [rtl] Add MCOUNTEREN CSR
    
    This commit adds the MCOUNTEREN CSR as required by the RISC-V spec.
    The register is defined as WARL. At the moment, Ibex doesn't enable U-mode
    access to the performance montiors. Consequently, writes to the register are
    ignored and it reads as zero which is okay according to the spec.
    
    This resolves lowRISC/Ibex#1278 .

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

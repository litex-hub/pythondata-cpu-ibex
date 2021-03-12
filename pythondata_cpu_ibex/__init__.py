import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2079"
version_tuple = (0, 0, 2079)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2079")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1984"
data_version_tuple = (0, 0, 1984)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1984")
except ImportError:
    pass
data_git_hash = "2c75c2b2ec90bebb756386e1360810474323c1ad"
data_git_describe = "v0.0-1984-g2c75c2b2"
data_git_msg = """\
commit 2c75c2b2ec90bebb756386e1360810474323c1ad
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Fri Mar 12 13:19:17 2021 +0000

    Update lowrisc_ip to lowRISC/opentitan@1ae03937f
    
    Update code from upstream repository
    https://github.com/lowRISC/opentitan to revision
    1ae03937f0bb4b146bb6e736bccb4821bfda556b
    
    * [prim/fifo_async] Add assertions on pointers (Tom Roberts)
    * [prim/fifo_async] Add support for Depth <= 2 (Tom Roberts)
    * [prim/fifo_async] Code tidy-up (Tom Roberts)
    * [top / ast] Continued ast integration (Timothy Chen)
    * [dvsim] Use bash when running make underneath (Srikrishna Iyer)
    * [prim] Increase maximum width for prim_util_memload to 312 (Greg
      Chadwick)
    * [sram_ctrl] Fix potential back-to-back partial write bug (Michael
      Schaffner)
    * [dvsim] Fix for lowRISC/opentitan#5527 (Srikrishna Iyer)
    * [lint] Waive Verilator UNUSED warnings for packages (Rupert
      Swarbrick)
    * [uvmdvgen] Update DV doc path and terminology (Srikrishna Iyer)
    * [clkmgr] Fix dft issues (Timothy Chen)
    * [util] add `dec` types to prim_secded_pkg (Udi Jonnalagadda)
    * [util] minor updates to secded_gen (Udi Jonnalagadda)
    * [lint] Fix a bunch of lint warnings related to long lines (>100
      chars) (Michael Schaffner)
    * [dv] Update common intr_test seq (Weicai Yang)
    * [util] Slight refactor of secded_gen.py (Timothy Chen)
    * [tlul] Add memory transmission integrity checks (Timothy Chen)
    * [dvsim] Move clean_odirs to `util.py` (Srikrishna Iyer)
    * [dvsim] Split Deploy into Deploy and Launcher (Srikrishna Iyer)
    * [dvsim] Add utils.TS_FORMAT* vars (Srikrishna Iyer)
    * [dv/lock_reg] Update IPs to adopt the lock_reg changes (Cindy Chen)
    * [dv/enable_regs] Support enable registers have more than one field
      (Cindy Chen)
    * [dv/base_reg] use m_field instead of accessing field (Cindy Chen)
    * [dv/sram] add SRAM scrambling model for DV (Udi Jonnalagadda)
    * [dv/tools] Updated Coverage flow for xcelium (Rasmus Madsen)
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

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

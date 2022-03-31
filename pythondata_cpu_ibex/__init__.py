import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2327"
version_tuple = (0, 0, 2327)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2327")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2201"
data_version_tuple = (0, 0, 2201)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2201")
except ImportError:
    pass
data_git_hash = "4c1a4ed1df4c9b16f9b380c8c507a823cb6a98c0"
data_git_describe = "v0.0-2201-g4c1a4ed1"
data_git_msg = """\
commit 4c1a4ed1df4c9b16f9b380c8c507a823cb6a98c0
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Thu Mar 31 14:08:12 2022 +0100

    Update lowrisc_ip to lowRISC/opentitan@0747afbdd
    
    Update code from upstream repository
    https://github.com/lowRISC/opentitan to revision
    0747afbddec0ad176980429fe3100b32edb71d4a
    
    * [dv] Enable C/C++ code sourcing with VCS in .core (Canberk Topal)
    * [dv/dv_base_reg] Remove duplicated `get_map_by_name` method (Cindy
      Chen)
    * [prim] Pulse Sync assertion to check input/output (Eunchan Kim)
    * [sparse_fsm_flop] Create flop macro to increase DV coverage (Michael
      Schaffner)
    * [dvsim] Make build-randomization opt-in (Srikrishna Iyer)
    * [xcelium] Fix compile error (Srikrishna Iyer)
    * [dv/cov] fpv_csr_assert only collect assertion coverage (Cindy Chen)
    * [dv/jtag] Fix chip_level jtag csr rw failure (Cindy Chen)
    * [rtl] Convert some non-ANSI parameters to localparams (Rupert
      Swarbrick)
    * [prim] Waive unused parameters for Verilator in prim_generic_otp
      (Rupert Swarbrick)
    * [prim] Make a variable widening explicit in prim_present.sv (Rupert
      Swarbrick)
    * [prim] Waive some ALWCOMBORDER Verilator warnings in prim_arbiter_*
      (Rupert Swarbrick)
    * [prim] Fix Verilator lint warnings in prim_gf_mult.sv (Rupert
      Swarbrick)
    * [prim] Make some widening comparisons explicit in prim_clock_*.sv
      (Rupert Swarbrick)
    * [prim] Waive unused EnableAlertTriggerSVA for verilator lint (Rupert
      Swarbrick)
    * [bazel,dvsim] Add build rules for dvsim.py (Timothy Trippel)
    * [prim] Fix a bunch of Verilator lint errors in prim_packer.sv
      (Rupert Swarbrick)
    * [prim_sparse_fsm_flop/lint] Move waiver to correct file (Michael
      Schaffner)
    * [rv_dm dv] Test drive compile-time seed (Srikrishna Iyer)
    * [dvsim] Introduce Verilog compile-time seeds (Srikrishna Iyer)
    * [dvsim] Treat `tests: ["N/A"]` as an ignored testpoint (Srikrishna
      Iyer)
    * [hw/dv] Removed colon from Questa build and run fail patterns.
      (David Pudner)
    * [hw/dv] Code review changes for running questa simulations. (David
      Pudner)
    * [hw/dv] Added apache license header to questa_initial_setup.sh.
      (David Pudner)
    * [doc/ug] Updated opentitan documentation to include information
      about Questa use. (David Pudner)
    * [hw/dv] Added Questa dvsim files (David Pudner)
    * [dv/unr] Blackbox common security modules from UNR flow (Cindy Chen)
    * [dv] Minor fix to error message in mem_model.sv (Rupert Swarbrick)
    * [keymgr] Update keymgr to use prim_edn_req (Timothy Chen)
    * [doc] Fix rendering of special characters in testplan table (Rupert
      Swarbrick)
    * [dv] enable tlul_assert for csr part2 (Rasmus Madsen)
    * [dv] Enable tlul_assert for CSR tests (Weicai Yang)
    * [dv] Add valid/ready req/ack coverage for push_pull agent (Weicai
      Yang)
    * [dv,verilator] Make multiple sim_ctrl extensions play nicely (Rupert
      Swarbrick)
    * [chip dv] Add AST initialization routine (Srikrishna Iyer)
    * [top] auto generate (Timothy Chen)
    * [reggen] Make field 'qe' behavior consistent (Timothy Chen)
    * [prim] IFDEF_CODE waiver in sparsefsm flop (Eunchan Kim)
    * [dv] Update checklist for all blocks (Weicai Yang)
    * [dv/entropy_src] Temp remove stress_all_with_rand_reset test (Cindy
      Chen)
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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

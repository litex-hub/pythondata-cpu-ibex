import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2218"
version_tuple = (0, 0, 2218)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2218")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2106"
data_version_tuple = (0, 0, 2106)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2106")
except ImportError:
    pass
data_git_hash = "53b1732b191b8e2aca159b40221feb8ba09d7ecd"
data_git_describe = "v0.0-2106-g53b1732b"
data_git_msg = """\
commit 53b1732b191b8e2aca159b40221feb8ba09d7ecd
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Mon Nov 29 11:52:25 2021 +0000

    Update lowrisc_ip to lowRISC/opentitan@3a672eb36
    
    This commit also adds memory manipulation package in ibex repository.
    
    Update code from upstream repository
    https://github.com/lowRISC/opentitan to revision
    3a672eb36aee5942d0912a15d15055b1d21c33d6
    
    * [mubi] Fix path in auto-gen header (Rupert Swarbrick)
    * [dv] Allow using memutil_dpi_scrambled even without prim_ram_1p_scr
      (Rupert Swarbrick)
    * [prim] Fix prim_ram_1p_scr Dependencies (Canberk Topal)
    * [dv/clk_rst_if] Split clk_rst_if jitter to 2 different values (Eitan
      Shapira)
    * [dv] Add external hjson path support in ralgen (Srikrishna Iyer)
    * [dv] Add sub RAL block creation knobs (Srikrishna Iyer)
    * [pwrmgr] Make rom_ctrl check signals multi-bit (Timothy Chen)
    * [dv/alert_handler] Randomize mubi input (Cindy Chen)
    * [flash_ctrl] Fix bank erase / info partition issue (Timothy Chen)
    * [ci] Fix CI failure (Weicai Yang)
    * [Cleanup] Remove lc_tx_e type and replace it with lc_tx_t (Weicai
      Yang)
    * [aes] Add gtech synthesis setup (Michael Schaffner)
    * [mubi] Enhance mubi_sync with stability check (Timothy Chen)
    * [prim] Fix prim_packer_fifo when ClearOnRead is false (Rupert
      Swarbrick)
    * [cleanup] Remove mubi4_e and replace it with mubi4_t (Weicai Yang)
    * [dv] Fix shape calculations for replicated ECC (Rupert Swarbrick)
    * [dv/alert] Support LPG in alert_sender/receiver pair (Cindy Chen)
    * [dv] Add a ReadWithIntegrity method to Ecc32MemArea (Rupert
      Swarbrick)
    * [dv] Simplify Ecc32MemArea read/write functions (Rupert Swarbrick)
    * [prim] Add option to not clear the packer FIFO upon read (Pirmin
      Vogel)
    * [dv] Change intg_err test from V3 to V2S (Weicai Yang)
    * [util] Delete generate_prim_mubi.py (Rupert Swarbrick)
    * [dv] Slightly generalise run_stress_all_with_rand_reset_vseq (Rupert
      Swarbrick)
    * [fpv] Fix some assumptions in prim_count (Cindy Chen)
    * [prim] quick path to prim_count assertion (Timothy Chen)
    * [dv] Support Multiple EDN Interfaces in OpenTitan (Canberk Topal)
    * [prim] Add xoshiro256pp primitive. (Vladimir Rozic)
    * [dv/prim_alert] Fix async fatal alert regression error (Cindy Chen)
    * [prim] Add missing include to prim_xilinx_pad_wrapper (Rupert
      Swarbrick)
    * [prim] Add missing include to prim_mubi_dec* (Rupert Swarbrick)
    * [dv/prim_alert_receiver] Fix assertion that consumes large mem
      (Cindy Chen)
    * [prim] Remove extra semicolon (Weicai Yang)
    * [chip,dv] Refactor CSR exclusion method (Srikrishna Iyer)
    * [top, all] update connects for mubi (Timothy Chen)
    * [flash_ctrl] Add plain text integrity in flash (Timothy Chen)
    * [prim] Add time-out functionality to prim_clock_meas (Timothy Chen)
    * [prim] Fix DC sythesis error (Weicai Yang)
    * [fpv] Fix regression failures (Cindy Chen)
    * [dv/ralgen] Update `dv_base_names` input from a string to a list
      (Cindy Chen)
    * [dv/ralgen] Update the `dv-base-prefix` optional input (Cindy Chen)
    * [doc] Add D2S and V2S checklist items to all checklists (Michael
      Schaffner)
    * [dv] Test security countermeasures (Weicai Yang)
    * [dv] Fix ASSERT_INIT race condition (Weicai Yang)
    * [syn/aes/otbn] Minor fixes to fix block level synthesis (Michael
      Schaffner)
    * [all] updated assert rtl ifdef (Timothy Chen)
    * [dv] Update TL intg testplan (Weicai Yang)
    * [prim] Add prim_fifo_async_sram_adapter to FPV list (Eunchan Kim)
    * [spi_device] Upload Cmd/Addr FIFO status revision (Eunchan Kim)
    * [dvsim] Modify resolve_branch to handle branch names with forward
      slash. (Todd Broch)
    * [prim_clock_inv] Add option to disable FPGA BUFG (Michael Schaffner)
    * [ralgen] Be more explicit which tool is called (Philipp Wagner)
    * [prim] Tweak prim_sync_reqack_data assertion so it can be disabled
      (Rupert Swarbrick)
    * [verible] Rename rule file (Philipp Wagner)
    * [dv/base_monitor] Cleaned up base monitor (Rasmus Madsen)
    * [fpv] prim_counter_fpv (Cindy Chen)
    * [dv/shadow_reg] Cross shadow reg error sequence with csr rw (Cindy
      Chen)
    * [dv] Fix scb multi-ral (Weicai Yang)
    * [dvsim] Enabling glob-style patterns for -i switch (Srikrishna Iyer)
    * [dv] Split sec_cm_testplan into multiple testplans (Weicai Yang)
    * [dv/dsim] Remove dsim's system_lib from library path (Guillermo
      Maturana)
    * [prim_packer] Resolve width mismatch (Philipp Wagner)
    * [prim] Fix lint error in prim_util_memload (Philipp Wagner)
    * [prim] Minor fix to make conn checks easy (Srikrishna Iyer)
    * [fpv] prim_secded FPV testbench updates bind file naming (Cindy
      Chen)
    * [dv_macros.svh] minor cleanup (Srikrishna Iyer)
    * [dv,xcelium] minor cleanup (Srikrishna Iyer)
    * [dv/shadowed_reset] Add a shadowed_rst_n interface (Cindy Chen)
    * [fpv] Update FPV file naming (Cindy Chen)
    * [top] Convert to mubi usage in some areas (Timothy Chen)
    * [entropy_src] mubi updates (Timothy Chen)
    * [prim] Add test for mubi invalid (Timothy Chen)
    * [prim_double_lfsr] Add duplicated LFSR primitive (Michael Schaffner)
    * [dv] Fix shadow reg backdoor path and enable csr_reset sequence
      (Weicai Yang)
    * [prim] Fix unused net (Timothy Chen)
    * [dv, clk_rst_if] Improve jitter and add scaling (Srikrishna Iyer)
    * [prim] Anchor buffers around register flip flops (Timothy Chen)
    * [alert_handler/top] Lint fixes and lc_tx_t to mubi4_t conversions
      (Michael Schaffner)
    * [prim_mubi] Replace true/false_value() functions with parameter
      (Michael Schaffner)
    * [dv/dsim] Get dsim to work at full chip (Guillermo Maturana)
    * [prim] Fixes for prim_count (Timothy Chen)
    * [top] Add various anchor points to modules (Timothy Chen)
    * [dv/pwrmgr] Add wakeup test sequence (Guillermo Maturana)
    * [reggen] Add mubi support into hjson (Timothy Chen)
    * [dv/shadow_reg] Fix aes shadow reg failure (Cindy Chen)
    * [dv/cdc] CDC simulation model (Udi Jonnalagadda)
    * [prim_lfsr/lint] Add temporary waiver for LOOP_VAR_OP lint error
      (Michael Schaffner)
    * [prim_clock_buf] Add lint waiver for unused parameter (Michael
      Schaffner)
    * [dvsim] Correctly set self_dir for included Hjson files (Philipp
      Wagner)
    * [util] Add tooling support for V2S milestone (Srikrishna Iyer)
    * [prim_mubi] Add decoder module similar to prim_lc_dec (Michael
      Schaffner)
    * [prim_mubi] Add mubi sender and sync primitives (Michael Schaffner)
    * [prim_mubi_pkg] Switch to True/False terminology (Michael Schaffner)
    * [prim] Minor work-around for xcelium (Timothy Chen)
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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

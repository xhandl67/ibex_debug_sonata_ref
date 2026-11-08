
import os
import shutil

src_dir = os.path.abspath("src")

directories = [
    # Hier deine bisherige directories-Liste unverändert einfügen
    "lowrisc_dv_crypto_prince_ref_0.1",
    "lowrisc_dv_dv_fcov_macros_0",
    "lowrisc_dv_dv_macros_0",
    "lowrisc_dv_scramble_model_0",
    "lowrisc_dv_secded_enc_0",
    "lowrisc_dv_verilator_memutil_dpi_0",
    "lowrisc_dv_verilator_memutil_dpi_scrambled_0",
    "lowrisc_ibex_demo_system_0",
    "lowrisc_ibex_demo_system_core_0",
    "lowrisc_ibex_fpga_xilinx_shared_0",
    "lowrisc_ibex_ibex_core_0.1",
    "lowrisc_ibex_ibex_icache_0.1",
    "lowrisc_ibex_ibex_pkg_0.1",
    "lowrisc_ibex_ibex_top_0.1",
    "lowrisc_ibex_rv_timer_0",
    "lowrisc_prim_abstract_and2_0",
    "lowrisc_prim_abstract_buf_0",
    "lowrisc_prim_abstract_clock_gating_0",
    "lowrisc_prim_abstract_clock_inv_0",
    "lowrisc_prim_abstract_clock_mux2_0",
    "lowrisc_prim_abstract_flop_0",
    "lowrisc_prim_abstract_prim_pkg_0.1",
    "lowrisc_prim_abstract_ram_1p_0",
    "lowrisc_prim_abstract_ram_2p_0",
    "lowrisc_prim_assert_0.1",
    "lowrisc_prim_badbit_ram_1p_0",
    "lowrisc_prim_cdc_rand_delay_0",
    "lowrisc_prim_cipher_0",
    "lowrisc_prim_cipher_pkg_0.1",
    "lowrisc_prim_count_0",
    "lowrisc_prim_fifo_0",
    "lowrisc_prim_flop_2sync_0",
    "lowrisc_prim_generic_and2_0",
    "lowrisc_prim_generic_buf_0",
    "lowrisc_prim_generic_clock_gating_0",
    "lowrisc_prim_generic_clock_inv_0",
    "lowrisc_prim_generic_clock_mux2_0",
    "lowrisc_prim_generic_flop_0",
    "lowrisc_prim_generic_ram_1p_0",
    "lowrisc_prim_generic_ram_2p_0",
    "lowrisc_prim_lfsr_0.1",
    "lowrisc_prim_mubi_0.1",
    "lowrisc_prim_onehot_0",
    "lowrisc_prim_onehot_check_0",
    "lowrisc_prim_ram_1p_adv_0.1",
    "lowrisc_prim_ram_1p_pkg_0",
    "lowrisc_prim_ram_1p_scr_0.1",
    "lowrisc_prim_ram_2p_pkg_0",
    "lowrisc_prim_secded_0.1",
    "lowrisc_prim_util_0.1",
    "lowrisc_prim_util_get_scramble_params_0",
    "lowrisc_prim_util_memload_0",
    "lowrisc_prim_xilinx_and2_0",
    "lowrisc_prim_xilinx_buf_0",
    "lowrisc_prim_xilinx_clock_gating_0",
    "lowrisc_prim_xilinx_clock_mux2_0",
    "lowrisc_prim_xilinx_flop_0",
    "lowrisc_tool_check_tool_requirements_0.1",
    "pulp_riscv_debug_module_0"
]

extensions = (".sv", ".v", ".svh")

rtl_dir = os.path.abspath("rtl")
os.makedirs(rtl_dir, exist_ok=True)

found_files = []

for directory in directories:
    search_dir = os.path.join(src_dir, directory)

    if not os.path.isdir(search_dir):
        print(f"Ordner nicht gefunden: {search_dir}")
        continue

    for root, dirs, files in os.walk(search_dir):
        for filename in files:

            # Ausschließlich HDL-Dateien berücksichtigen
            if filename.lower().endswith(extensions):
                filepath = os.path.join(root, filename)
                found_files.append(filepath)

found_files = sorted(set(found_files))

copied = 0

for filepath in found_files:
    filename = os.path.basename(filepath)
    destination = os.path.join(rtl_dir, filename)

    shutil.copy2(filepath, destination)
    copied += 1

print(f"\n{len(found_files)} HDL-Dateien gefunden.")
print(f"{copied} HDL-Dateien nach rtl kopiert.")

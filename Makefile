TOP = top_gatemate
GATEMATE_PRIM_LIB = /home/kasachstan_horse67/toolchains/oss-cad-suite/share/yosys/gatemate/
RTL_DIR            = rtl
READ_VERILOG_FILES =
IMPLEMENT_FLAGS = -l build/routing.txt --verbose --device=CCGM1A1 --seed 2 --vopt allow-unconstrained --json build/gatemate_synth.json
ALL_FILES          = $(wildcard $(RTL_DIR)/*.sv) $(wildcard $(RTL_DIR)/*.v)
READ_SLANG_FILES   = $(filter-out $(READ_VERILOG_FILES),$(ALL_FILES))
GATE_MATE_PIN_CONSTRAINTS = constraints/gatemate_pins.ccf
GATE_MATE_TIMING_CONSTRAINTS = constraints/gatemate_timing.sdc
soc:
	yosys -m slang -ql build/synth_log.txt -p "\
		read_verilog -lib $(GATEMATE_PRIM_LIB)*.v; \
		read_slang --std latest --ignore-initial --allow-use-before-declare -I $(RTL_DIR) --top $(TOP) $(READ_SLANG_FILES); \
		synth_gatemate -top $(TOP) -luttree -nomx8; \
		write_json build/gatemate_synth.json"

	nextpnr-himbaechel $(IMPLEMENT_FLAGS) -o ccf=$(GATE_MATE_PIN_CONSTRAINTS) \
		-o out=build/impl.txt --sdc $(GATE_MATE_TIMING_CONSTRAINTS) --router router2

	gmpack build/impl.txt build/impl.bit

clean:
	rm build/gatemate_synth.json build/synth_log.txt build/impl.bit build/impl.txt build/routing.txt
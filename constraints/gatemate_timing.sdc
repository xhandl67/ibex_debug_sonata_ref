create_clock -name sys -period 100 [get_ports main_clk]
create_clock -name jtag -period 10000 [get_ports tck_i]
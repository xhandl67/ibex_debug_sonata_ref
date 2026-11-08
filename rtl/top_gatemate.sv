// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0

// Ibex demo system top level for the GateMate  board
module top_gatemate #(
    parameter SRAMInitFile = "firmware_mem_init.svh"
)(
  input         main_clk,

  output logic  led_user,

  output logic uart_tx,
  input  logic uart_rx,

  input  logic tck_i,
  input  logic tms_i,
  input  logic td_i,
  output logic td_o
);

  wire rst_sys_n;




  //Reset is gonna be active for some cycles in the beginning
  logic [7:0] por_cnt = 8'd0;
  always @(posedge main_clk) begin
    if (!por_cnt[7]) por_cnt <= por_cnt + 8'd1;
  end
  assign rst_sys_n = por_cnt[7];
  ibex_demo_system #(
    .GpiWidth(0),
    .GpoWidth(1),
    .PwmWidth(0),
    .SRAMInitFile(SRAMInitFile),
    .ClockFrequency(10_000_000)
  ) u_ibex_demo_system (
    .clk_sys_i(main_clk),
    .rst_sys_ni(rst_sys_n),

    .gp_o(led_user),

    .uart_rx_i(uart_rx),
    .uart_tx_o(uart_tx),

    .trst_ni(rst_sys_n),
    .tms_i(tms_i),
    .tck_i(tck_i),
    .td_i(td_i),
    .td_o(td_o)
  );

endmodule

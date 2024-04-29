`timescale 1us/1ns

module regFile(
  input        clock,
  input        reset,
  input  [3:0] io_in_a,
  input  [3:0] io_in_b,
  output [3:0] io_out
);

  initial begin
    $fsdbDumpfile("./test.fsdb");
    $fsdbDumpvars("+all");
  end

  assign io_out = io_in_a + io_in_b; // @[RegFile.scala 36:21]
endmodule

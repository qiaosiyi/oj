`timescale 1ns/1ps

module yuv2rgb #(
	parameter	DSIZE	= 8,
	parameter	MSIZE	= 12
)(
	input				                                              clock ,

	input				                                                y_cb_cr_vld ,
	input                                         [DSIZE*3-1:0]	y_cb_cr ,
	
  output				                                              rgb_vld ,
	output reg                                    [DSIZE*3-1:0]	rgb ,
);
//  R = 1.164 *(Y - 16) + 0                 + 1.792 *(Cr - 128)//
//  G = 1.164 *(Y - 16) - 0.213 *(Cb - 128) - 0.534 *(Cr - 128)//
//  B = 1.164 *(Y - 16) + 2.114 *(Cb - 128) + 0                //

//  R = 1.164 * Y + 0          + 1.792 * CR - 248
//  G = 1.164 * Y - 0.213 * CB - 0.534 * CR + 76.992
//  B = 1.164 * Y + 2.114 * CB + 0          - 289.216


localparam                  [MSIZE-1:0] M00 = 1.164 * 2**MSIZE,
                                        M10 = 1.164 * 2**MSIZE,
                                        M20 = 1.164 * 2**MSIZE;

localparam                  [MSIZE-1:0] M01 = 0     * 2**MSIZE,
                                        M11 = 0.213 * 2**MSIZE,
                                        M21 = 2.114 * 2**MSIZE;

localparam                  [MSIZE-1:0] M02 = 1.792 * 2**MSIZE,
                                        M12 = 0.534 * 2**MSIZE,
                                        M22 = 0     * 2**MSIZE;

localparam        [DSIZE + MSIZE - 1:0] M248 = 248 * 2**MSIZE,
                                        M76992 = 76.992 * 2**MSIZE,
                                        M289 = 289.216 * 2**MSIZE;

reg valid1;

always @(posedge clock) begin
  YY1 <= M00 * y_cb_cr[DSIZE*3-1:DSIZE*2];
  YY2 <= M10 * y_cb_cr[DSIZE*3-1:DSIZE*2]; 
  YY3 <= M20 * y_cb_cr[DSIZE*3-1:DSIZE*2];
  valid1 <= y_cb_cr_vld;
end

always @(posedge clock) begin
  CB1 <= M01 * y_cb_cr[DSIZE*2-1:DSIZE*1];
  CB2 <= M11 * y_cb_cr[DSIZE*2-1:DSIZE*1]; 
  CB3 <= M21 * y_cb_cr[DSIZE*2-1:DSIZE*1];

end

always @(posedge clock) begin
  CR1 <= M02 * y_cb_cr[DSIZE*1-1:DSIZE*0];
  CR2 <= M12 * y_cb_cr[DSIZE*1-1:DSIZE*0]; 
  CR3 <= M22 * y_cb_cr[DSIZE*1-1:DSIZE*0];

end
wire [DSIZE + MSIZE - 1:0] RR;
wire [DSIZE + MSIZE - 1:0] GG;
wire [DSIZE + MSIZE - 1:0] BB;
assign RR = YY1 + CR1 - M248;
assign GG = YY2 + M76992 - CB2 - CR2;
assign BB = YY3 + CB3 - M289 ;

always @(posedge clock) begin
  if(YY1 + CR1 <= M248)begin
    rgb[DSIZE*3-1:DSIZE*2] <= 0;
  end else if(YY1 + CR1 - M248 > 255 * 2**MSIZE)begin
    rgb[DSIZE*3-1:DSIZE*2] <= 255;
  end else begin
    rgb[DSIZE*3-1:DSIZE*2] <= RR[DSIZE + MSIZE - 1:MSIZE];
  end

  if(YY2 + M76992 <= CB2 + CR2)begin
    rgb[DSIZE*2-1:DSIZE*1] <= 0;
  end else if(YY2 + M76992 - CB2 - CR2 > 255 * 2**MSIZE)begin
    rgb[DSIZE*2-1:DSIZE*1] <= 255;
  end else begin
    rgb[DSIZE*2-1:DSIZE*1] <= GG[DSIZE + MSIZE - 1:MSIZE];
  end  

  if(YY3 + CB3 <= M289)begin
    rgb[DSIZE*1-1:DSIZE*0] <= 0;
  end else if(YY3 + CB3 - M289 > 255 * 2**MSIZE)begin
    rgb[DSIZE*1-1:DSIZE*0] <= 255;
  end else begin
    rgb[DSIZE*1-1:DSIZE*0] <= BB[DSIZE + MSIZE - 1:MSIZE];
  end  

  rgb_vld <= valid1;

end


endmodule

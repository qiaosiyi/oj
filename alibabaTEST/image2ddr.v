`timescale 1ns/1ps

module image2ddr #(
	parameter	DSIZE	= 24,
	parameter	MSIZE	= 12
)(
	input				                                                clk_300,
  input                                                       rst_300,
  input                                                       clk_266,
  input                                                       rst_266,

	input				                                                in_valid,
	input                                               [23:0]	inrgb,
	
  
  
);

reg [23:0] picbuf0 [0:1280*16-1];
reg [23:0] picbuf1 [0:1280*16-1];

reg [31:0] picpoint1;
reg [31:0] piccounter1;
reg picfinish0;
reg picfinish1;
reg picflag1sttime;

always@(posedge clk_300)begin
  if(!rst_300)begin
    picpoint1 <= 0;
    piccounter1 <= 0;
    picfinish0 <= 0;//finish storing pic buf0
    picfinish1 <= 0;
    picflag1sttime <= 1;
  end else begin
    if (in_valid) begin
      if(picpoint1 == 0)begin
        picbuf0[piccounter1] <= inrgb;
        piccounter1 <= piccounter1 + 1;
      end else begin //picpoint1 == 1
        picbuf1[piccounter1] <= inrgb;
        piccounter1 <= piccounter1 + 1;
      end
      if(piccounter1 == 1280*16 - 1)begin
        picpoint1 <= !picpoint1;
        piccounter1 <= 0;
        if(picflag1sttime)begin
          picfinish0 <= 1;
          picfinish1 <= 0;
          picflag1sttime <= 0;
        end else begin
          picfinish0 <= !picfinish0;
          picfinish1 <= !picfinish1;
        end
      end
    end
  end
end

always@(posedge clk_266)begin
  if(!rst_266)begin
    scnt <= 0;
    picreading1 <= 0;
  end else begin
    if(picfinish0 && !picfinish1)begin
      if(scnt < 12*80)begin
        scnt <= scnt + 1;
        picreading1 <= 1;
      end else begin
        scnt <= 0;
        picreading1 <= 0;
      end
    end
  end
end


always @(posedge clk_266)begin
  if(!rst_266)begin
    ssscnt1 <= 0;
    sscnt1 <= 0;
  end else begin
    if(picreading1 )begin
      if(ssscnt1 < 11)begin
        ssscnt1 <= ssscnt1 + 1; // 0 ---- 11
      end else begin
        ssscnt1 <= 0;
        sscnt1 <= sscnt1 + 1; // 0 ---- 80
      end
    end else begin
      ssscnt1 <= 0;
      sscnt1 <= 0;
    end
  end
end

always @(posedge clk_266)begin
  if(!rst_266)begin
    outdata <= 0;
  end else begin
    if(picreading1)begin
      if(ssscnt1 == 0)begin
        outdata <= {picbuf0[0][sscnt1:sscnt1+16*24-1],picbuf0[1][sscnt1:sscnt1+16*24/3-1]};
      end else if (ssscnt1 == 1) begin
        outdata <= {picbuf0[1][sscnt1+16*24/3:sscnt1+16*24-1],picbuf0[2][sscnt1:sscnt1+16*24/3*2-1]};
      end else if (ssscnt1 == 2) begin
        outdata <= {picbuf0[2][sscnt1+16*24/3*2:sscnt1+16*24-1],picbuf0[3][sscnt1:sscnt1+16*24-1]};
      end else if (ssscnt1 == 3) begin
        outdata <= {picbuf0[4][sscnt1:sscnt1+16*24-1],picbuf0[5][sscnt1:sscnt1+16*24/3-1]};
      end else if (ssscnt1 == 4) begin
        outdata <= {picbuf0[5][sscnt1+16*24/3:sscnt1+16*24-1],picbuf0[6][sscnt1:sscnt1+16*24/3*2-1]};
      end else if (ssscnt1 == 5) begin
        outdata <= {picbuf0[6][sscnt1+16*24/3*2:sscnt1+16*24-1],picbuf0[7][sscnt1:sscnt1+16*24-1]};
      end else if (ssscnt1 == 6) begin
        outdata <= {picbuf0[8][sscnt1:sscnt1+16*24-1],picbuf0[9][sscnt1:sscnt1+16*24/3-1]};
      end else if (ssscnt1 == 7) begin
        outdata <= {picbuf0[9][sscnt1+16*24/3:sscnt1+16*24-1],picbuf0[10][sscnt1:sscnt1+16*24/3*2-1]};
      end else if (ssscnt1 == 8) begin
        outdata <= {picbuf0[10][sscnt1+16*24/3*2:sscnt1+16*24-1],picbuf0[11][sscnt1:sscnt1+16*24-1]};
      end else if (ssscnt1 == 9) begin
        outdata <= {picbuf0[12][sscnt1:sscnt1+16*24-1],picbuf0[13][sscnt1:sscnt1+16*24/3-1]};
      end else if (ssscnt1 == 10) begin
        outdata <= {picbuf0[13][sscnt1+16*24/3:sscnt1+16*24-1],picbuf0[14][sscnt1:sscnt1+16*24/3*2-1]};
      end else if (ssscnt1 == 11) begin
        outdata <= {picbuf0[14][sscnt1+16*24/3*2:sscnt1+16*24-1],picbuf0[15][sscnt1:sscnt1+16*24-1]};
      end
    end else begin
      outdata <= 0;
    end
  end
end


endmodule

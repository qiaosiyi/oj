module a();

    reg [15:0] mm [0:100*1000];


    always@(posedge clk_a)begin
        if(reset_n)begin

        end else begin
            if (wr_pos == 100*1000)
                wr_pos <= 0;
            else
                wr_pos <= wr_pos + 1;
        end
    end 

    always@(posedge clk_a)begin
        if(reset_n)begin
            reg_delay <= 0;
        end else begin
            if (reg_delay < DELAY) begin
                reg_delay <= reg_delay + 1;
                rd_enable <= 0
            end else begin
                rd_enable <= 1;
            end
        end
    end 

    always@(posedge clk_b)begin//clk b read block
        if(reset_n)begin

        end else begin
            if(rd_enable)begin
                if(reg_delay == 100*1000)
                    rd_pos <= 0;
                else
                    rd_pos <= rd_pos + 1;
                rd_pos <= rd_pos + 1;
                out <= mm[rd_pos];
            end
        end
    end 
endmodule
# all possible rules for Moore neighborhood
def rule_gen(rule_code):
    # rule_code is a 512-bit binary number
    # establish rule dictionary base on rule_code
    rule_dict = {0b000000000: int(rule_code[0]), 0b000000001: int(rule_code[1]), 0b000000010: int(rule_code[2]), 0b000000011: int(rule_code[3]),\
                    0b000000100: int(rule_code[4]), 0b000000101: int(rule_code[5]), 0b000000110: int(rule_code[6]), 0b000000111: int(rule_code[7]),\
                    0b000001000: int(rule_code[8]), 0b000001001: int(rule_code[9]), 0b000001010: int(rule_code[10]), 0b000001011: int(rule_code[11]),\
                    0b000001100: int(rule_code[12]), 0b000001101: int(rule_code[13]), 0b000001110: int(rule_code[14]), 0b000001111: int(rule_code[15]),\
                    0b000010000: int(rule_code[16]), 0b000010001: int(rule_code[17]), 0b000010010: int(rule_code[18]), 0b000010011: int(rule_code[19]),\
                    0b000010100: int(rule_code[20]), 0b000010101: int(rule_code[21]), 0b000010110: int(rule_code[22]), 0b000010111: int(rule_code[23]),\
                    0b000011000: int(rule_code[24]), 0b000011001: int(rule_code[25]), 0b000011010: int(rule_code[26]), 0b000011011: int(rule_code[27]),\
                    0b000011100: int(rule_code[28]), 0b000011101: int(rule_code[29]), 0b000011110: int(rule_code[30]), 0b000011111: int(rule_code[31]),\
                    0b000100000: int(rule_code[32]), 0b000100001: int(rule_code[33]), 0b000100010: int(rule_code[34]), 0b000100011: int(rule_code[35]),\
                    0b000100100: int(rule_code[36]), 0b000100101: int(rule_code[37]), 0b000100110: int(rule_code[38]), 0b000100111: int(rule_code[39]), \
                    0b000101000: int(rule_code[40]), 0b000101001: int(rule_code[41]), 0b000101010: int(rule_code[42]), 0b000101011: int(rule_code[43]), \
                    0b000101100: int(rule_code[44]), 0b000101101: int(rule_code[45]), 0b000101110: int(rule_code[46]), 0b000101111: int(rule_code[47]), \
                    0b000110000: int(rule_code[48]), 0b000110001: int(rule_code[49]), 0b000110010: int(rule_code[50]), 0b000110011: int(rule_code[51]), \
                    0b000110100: int(rule_code[52]), 0b000110101: int(rule_code[53]), 0b000110110: int(rule_code[54]), 0b000110111: int(rule_code[55]), \
                    0b000111000: int(rule_code[56]), 0b000111001: int(rule_code[57]), 0b000111010: int(rule_code[58]), 0b000111011: int(rule_code[59]), \
                    0b000111100: int(rule_code[60]), 0b000111101: int(rule_code[61]), 0b000111110: int(rule_code[62]), 0b000111111: int(rule_code[63]), \
                    0b001000000: int(rule_code[64]), 0b001000001: int(rule_code[65]), 0b001000010: int(rule_code[66]), 0b001000011: int(rule_code[67]), \
                    0b001000100: int(rule_code[68]), 0b001000101: int(rule_code[69]), 0b001000110: int(rule_code[70]), 0b001000111: int(rule_code[71]), \
                    0b001001000: int(rule_code[72]), 0b001001001: int(rule_code[73]), 0b001001010: int(rule_code[74]), 0b001001011: int(rule_code[75]), \
                    0b001001100: int(rule_code[76]), 0b001001101: int(rule_code[77]), 0b001001110: int(rule_code[78]), 0b001001111: int(rule_code[79]), \
                    0b001010000: int(rule_code[80]), 0b001010001: int(rule_code[81]), 0b001010010: int(rule_code[82]), 0b001010011: int(rule_code[83]), \
                    0b001010100: int(rule_code[84]), 0b001010101: int(rule_code[85]), 0b001010110: int(rule_code[86]), 0b001010111: int(rule_code[87]), \
                    0b001011000: int(rule_code[88]), 0b001011001: int(rule_code[89]), 0b001011010: int(rule_code[90]), 0b001011011: int(rule_code[91]), \
                    0b001011100: int(rule_code[92]), 0b001011101: int(rule_code[93]), 0b001011110: int(rule_code[94]), 0b001011111: int(rule_code[95]), \
                    0b001100000: int(rule_code[96]), 0b001100001: int(rule_code[97]), 0b001100010: int(rule_code[98]), 0b001100011: int(rule_code[99]), \
                    0b001100100: int(rule_code[100]), 0b001100101: int(rule_code[101]), 0b001100110: int(rule_code[102]), 0b001100111: int(rule_code[103]), \
                    0b001101000: int(rule_code[104]), 0b001101001: int(rule_code[105]), 0b001101010: int(rule_code[106]), 0b001101011: int(rule_code[107]), \
                    0b001101100: int(rule_code[108]), 0b001101101: int(rule_code[109]), 0b001101110: int(rule_code[110]), 0b001101111: int(rule_code[111]), \
                    0b001110000: int(rule_code[112]), 0b001110001: int(rule_code[113]), 0b001110010: int(rule_code[114]), 0b001110011: int(rule_code[115]), \
                    0b001110100: int(rule_code[116]), 0b001110101: int(rule_code[117]), 0b001110110: int(rule_code[118]), 0b001110111: int(rule_code[119]), \
                    0b001111000: int(rule_code[120]), 0b001111001: int(rule_code[121]), 0b001111010: int(rule_code[122]), 0b001111011: int(rule_code[123]), \
                    0b001111100: int(rule_code[124]), 0b001111101: int(rule_code[125]), 0b001111110: int(rule_code[126]), 0b001111111: int(rule_code[127]), \
                    0b010000000: int(rule_code[128]), 0b010000001: int(rule_code[129]), 0b010000010: int(rule_code[130]), 0b010000011: int(rule_code[131]), \
                    0b010000100: int(rule_code[132]), 0b010000101: int(rule_code[133]), 0b010000110: int(rule_code[134]), 0b010000111: int(rule_code[135]), \
                    0b010001000: int(rule_code[136]), 0b010001001: int(rule_code[137]), 0b010001010: int(rule_code[138]), 0b010001011: int(rule_code[139]), \
                    0b010001100: int(rule_code[140]), 0b010001101: int(rule_code[141]), 0b010001110: int(rule_code[142]), 0b010001111: int(rule_code[143]), \
                    0b010010000: int(rule_code[144]), 0b010010001: int(rule_code[145]), 0b010010010: int(rule_code[146]), 0b010010011: int(rule_code[147]), \
                    0b010010100: int(rule_code[148]), 0b010010101: int(rule_code[149]), 0b010010110: int(rule_code[150]), 0b010010111: int(rule_code[151]), \
                    0b010011000: int(rule_code[152]), 0b010011001: int(rule_code[153]), 0b010011010: int(rule_code[154]), 0b010011011: int(rule_code[155]), \
                    0b010011100: int(rule_code[156]), 0b010011101: int(rule_code[157]), 0b010011110: int(rule_code[158]), 0b010011111: int(rule_code[159]), \
                    0b010100000: int(rule_code[160]), 0b010100001: int(rule_code[161]), 0b010100010: int(rule_code[162]), 0b010100011: int(rule_code[163]), \
                    0b010100100: int(rule_code[164]), 0b010100101: int(rule_code[165]), 0b010100110: int(rule_code[166]), 0b010100111: int(rule_code[167]), \
                    0b010101000: int(rule_code[168]), 0b010101001: int(rule_code[169]), 0b010101010: int(rule_code[170]), 0b010101011: int(rule_code[171]), \
                    0b010101100: int(rule_code[172]), 0b010101101: int(rule_code[173]), 0b010101110: int(rule_code[174]), 0b010101111: int(rule_code[175]), \
                    0b010110000: int(rule_code[176]), 0b010110001: int(rule_code[177]), 0b010110010: int(rule_code[178]), 0b010110011: int(rule_code[179]), \
                    0b010110100: int(rule_code[180]), 0b010110101: int(rule_code[181]), 0b010110110: int(rule_code[182]), 0b010110111: int(rule_code[183]), \
                    0b010111000: int(rule_code[184]), 0b010111001: int(rule_code[185]), 0b010111010: int(rule_code[186]), 0b010111011: int(rule_code[187]), \
                    0b010111100: int(rule_code[188]), 0b010111101: int(rule_code[189]), 0b010111110: int(rule_code[190]), 0b010111111: int(rule_code[191]), \
                    0b011000000: int(rule_code[192]), 0b011000001: int(rule_code[193]), 0b011000010: int(rule_code[194]), 0b011000011: int(rule_code[195]), \
                    0b011000100: int(rule_code[196]), 0b011000101: int(rule_code[197]), 0b011000110: int(rule_code[198]), 0b011000111: int(rule_code[199]), \
                    0b011001000: int(rule_code[200]), 0b011001001: int(rule_code[201]), 0b011001010: int(rule_code[202]), 0b011001011: int(rule_code[203]), \
                    0b011001100: int(rule_code[204]), 0b011001101: int(rule_code[205]), 0b011001110: int(rule_code[206]), 0b011001111: int(rule_code[207]), \
                    0b011010000: int(rule_code[208]), 0b011010001: int(rule_code[209]), 0b011010010: int(rule_code[210]), 0b011010011: int(rule_code[211]), \
                    0b011010100: int(rule_code[212]), 0b011010101: int(rule_code[213]), 0b011010110: int(rule_code[214]), 0b011010111: int(rule_code[215]), \
                    0b011011000: int(rule_code[216]), 0b011011001: int(rule_code[217]), 0b011011010: int(rule_code[218]), 0b011011011: int(rule_code[219]), \
                    0b011011100: int(rule_code[220]), 0b011011101: int(rule_code[221]), 0b011011110: int(rule_code[222]), 0b011011111: int(rule_code[223]), \
                    0b011100000: int(rule_code[224]), 0b011100001: int(rule_code[225]), 0b011100010: int(rule_code[226]), 0b011100011: int(rule_code[227]), \
                    0b011100100: int(rule_code[228]), 0b011100101: int(rule_code[229]), 0b011100110: int(rule_code[230]), 0b011100111: int(rule_code[231]), \
                    0b011101000: int(rule_code[232]), 0b011101001: int(rule_code[233]), 0b011101010: int(rule_code[234]), 0b011101011: int(rule_code[235]), \
                    0b011101100: int(rule_code[236]), 0b011101101: int(rule_code[237]), 0b011101110: int(rule_code[238]), 0b011101111: int(rule_code[239]), \
                    0b011110000: int(rule_code[240]), 0b011110001: int(rule_code[241]), 0b011110010: int(rule_code[242]), 0b011110011: int(rule_code[243]), \
                    0b011110100: int(rule_code[244]), 0b011110101: int(rule_code[245]), 0b011110110: int(rule_code[246]), 0b011110111: int(rule_code[247]), \
                    0b011111000: int(rule_code[248]), 0b011111001: int(rule_code[249]), 0b011111010: int(rule_code[250]), 0b011111011: int(rule_code[251]), \
                    0b011111100: int(rule_code[252]), 0b011111101: int(rule_code[253]), 0b011111110: int(rule_code[254]), 0b011111111: int(rule_code[255]), \
                    0b100000000: int(rule_code[256]), 0b100000001: int(rule_code[257]), 0b100000010: int(rule_code[258]), 0b100000011: int(rule_code[259]), \
                    0b100000100: int(rule_code[260]), 0b100000101: int(rule_code[261]), 0b100000110: int(rule_code[262]), 0b100000111: int(rule_code[263]), \
                    0b100001000: int(rule_code[264]), 0b100001001: int(rule_code[265]), 0b100001010: int(rule_code[266]), 0b100001011: int(rule_code[267]), \
                    0b100001100: int(rule_code[268]), 0b100001101: int(rule_code[269]), 0b100001110: int(rule_code[270]), 0b100001111: int(rule_code[271]), \
                    0b100010000: int(rule_code[272]), 0b100010001: int(rule_code[273]), 0b100010010: int(rule_code[274]), 0b100010011: int(rule_code[275]), \
                    0b100010100: int(rule_code[276]), 0b100010101: int(rule_code[277]), 0b100010110: int(rule_code[278]), 0b100010111: int(rule_code[279]), \
                    0b100011000: int(rule_code[280]), 0b100011001: int(rule_code[281]), 0b100011010: int(rule_code[282]), 0b100011011: int(rule_code[283]), \
                    0b100011100: int(rule_code[284]), 0b100011101: int(rule_code[285]), 0b100011110: int(rule_code[286]), 0b100011111: int(rule_code[287]), \
                    0b100100000: int(rule_code[288]), 0b100100001: int(rule_code[289]), 0b100100010: int(rule_code[290]), 0b100100011: int(rule_code[291]), \
                    0b100100100: int(rule_code[292]), 0b100100101: int(rule_code[293]), 0b100100110: int(rule_code[294]), 0b100100111: int(rule_code[295]), \
                    0b100101000: int(rule_code[296]), 0b100101001: int(rule_code[297]), 0b100101010: int(rule_code[298]), 0b100101011: int(rule_code[299]), \
                    0b100101100: int(rule_code[300]), 0b100101101: int(rule_code[301]), 0b100101110: int(rule_code[302]), 0b100101111: int(rule_code[303]), \
                    0b100110000: int(rule_code[304]), 0b100110001: int(rule_code[305]), 0b100110010: int(rule_code[306]), 0b100110011: int(rule_code[307]), \
                    0b100110100: int(rule_code[308]), 0b100110101: int(rule_code[309]), 0b100110110: int(rule_code[310]), 0b100110111: int(rule_code[311]), \
                    0b100111000: int(rule_code[312]), 0b100111001: int(rule_code[313]), 0b100111010: int(rule_code[314]), 0b100111011: int(rule_code[315]), \
                    0b100111100: int(rule_code[316]), 0b100111101: int(rule_code[317]), 0b100111110: int(rule_code[318]), 0b100111111: int(rule_code[319]), \
                    0b101000000: int(rule_code[320]), 0b101000001: int(rule_code[321]), 0b101000010: int(rule_code[322]), 0b101000011: int(rule_code[323]), \
                    0b101000100: int(rule_code[324]), 0b101000101: int(rule_code[325]), 0b101000110: int(rule_code[326]), 0b101000111: int(rule_code[327]), \
                    0b101001000: int(rule_code[328]), 0b101001001: int(rule_code[329]), 0b101001010: int(rule_code[330]), 0b101001011: int(rule_code[331]), \
                    0b101001100: int(rule_code[332]), 0b101001101: int(rule_code[333]), 0b101001110: int(rule_code[334]), 0b101001111: int(rule_code[335]), \
                    0b101010000: int(rule_code[336]), 0b101010001: int(rule_code[337]), 0b101010010: int(rule_code[338]), 0b101010011: int(rule_code[339]), \
                    0b101010100: int(rule_code[340]), 0b101010101: int(rule_code[341]), 0b101010110: int(rule_code[342]), 0b101010111: int(rule_code[343]), \
                    0b101011000: int(rule_code[344]), 0b101011001: int(rule_code[345]), 0b101011010: int(rule_code[346]), 0b101011011: int(rule_code[347]), \
                    0b101011100: int(rule_code[348]), 0b101011101: int(rule_code[349]), 0b101011110: int(rule_code[350]), 0b101011111: int(rule_code[351]), \
                    0b101100000: int(rule_code[352]), 0b101100001: int(rule_code[353]), 0b101100010: int(rule_code[354]), 0b101100011: int(rule_code[355]), \
                    0b101100100: int(rule_code[356]), 0b101100101: int(rule_code[357]), 0b101100110: int(rule_code[358]), 0b101100111: int(rule_code[359]), \
                    0b101101000: int(rule_code[360]), 0b101101001: int(rule_code[361]), 0b101101010: int(rule_code[362]), 0b101101011: int(rule_code[363]), \
                    0b101101100: int(rule_code[364]), 0b101101101: int(rule_code[365]), 0b101101110: int(rule_code[366]), 0b101101111: int(rule_code[367]), \
                    0b101110000: int(rule_code[368]), 0b101110001: int(rule_code[369]), 0b101110010: int(rule_code[370]), 0b101110011: int(rule_code[371]), \
                    0b101110100: int(rule_code[372]), 0b101110101: int(rule_code[373]), 0b101110110: int(rule_code[374]), 0b101110111: int(rule_code[375]), \
                    0b101111000: int(rule_code[376]), 0b101111001: int(rule_code[377]), 0b101111010: int(rule_code[378]), 0b101111011: int(rule_code[379]), \
                    0b101111100: int(rule_code[380]), 0b101111101: int(rule_code[381]), 0b101111110: int(rule_code[382]), 0b101111111: int(rule_code[383]), \
                    0b110000000: int(rule_code[384]), 0b110000001: int(rule_code[385]), 0b110000010: int(rule_code[386]), 0b110000011: int(rule_code[387]), \
                    0b110000100: int(rule_code[388]), 0b110000101: int(rule_code[389]), 0b110000110: int(rule_code[390]), 0b110000111: int(rule_code[391]), \
                    0b110001000: int(rule_code[392]), 0b110001001: int(rule_code[393]), 0b110001010: int(rule_code[394]), 0b110001011: int(rule_code[395]), \
                    0b110001100: int(rule_code[396]), 0b110001101: int(rule_code[397]), 0b110001110: int(rule_code[398]), 0b110001111: int(rule_code[399]), \
                    0b110010000: int(rule_code[400]), 0b110010001: int(rule_code[401]), 0b110010010: int(rule_code[402]), 0b110010011: int(rule_code[403]), \
                    0b110010100: int(rule_code[404]), 0b110010101: int(rule_code[405]), 0b110010110: int(rule_code[406]), 0b110010111: int(rule_code[407]), \
                    0b110011000: int(rule_code[408]), 0b110011001: int(rule_code[409]), 0b110011010: int(rule_code[410]), 0b110011011: int(rule_code[411]), \
                    0b110011100: int(rule_code[412]), 0b110011101: int(rule_code[413]), 0b110011110: int(rule_code[414]), 0b110011111: int(rule_code[415]), \
                    0b110100000: int(rule_code[416]), 0b110100001: int(rule_code[417]), 0b110100010: int(rule_code[418]), 0b110100011: int(rule_code[419]), \
                    0b110100100: int(rule_code[420]), 0b110100101: int(rule_code[421]), 0b110100110: int(rule_code[422]), 0b110100111: int(rule_code[423]), \
                    0b110101000: int(rule_code[424]), 0b110101001: int(rule_code[425]), 0b110101010: int(rule_code[426]), 0b110101011: int(rule_code[427]), \
                    0b110101100: int(rule_code[428]), 0b110101101: int(rule_code[429]), 0b110101110: int(rule_code[430]), 0b110101111: int(rule_code[431]), \
                    0b110110000: int(rule_code[432]), 0b110110001: int(rule_code[433]), 0b110110010: int(rule_code[434]), 0b110110011: int(rule_code[435]), \
                    0b110110100: int(rule_code[436]), 0b110110101: int(rule_code[437]), 0b110110110: int(rule_code[438]), 0b110110111: int(rule_code[439]), \
                    0b110111000: int(rule_code[440]), 0b110111001: int(rule_code[441]), 0b110111010: int(rule_code[442]), 0b110111011: int(rule_code[443]), \
                    0b110111100: int(rule_code[444]), 0b110111101: int(rule_code[445]), 0b110111110: int(rule_code[446]), 0b110111111: int(rule_code[447]), \
                    0b111000000: int(rule_code[448]), 0b111000001: int(rule_code[449]), 0b111000010: int(rule_code[450]), 0b111000011: int(rule_code[451]), \
                    0b111000100: int(rule_code[452]), 0b111000101: int(rule_code[453]), 0b111000110: int(rule_code[454]), 0b111000111: int(rule_code[455]), \
                    0b111001000: int(rule_code[456]), 0b111001001: int(rule_code[457]), 0b111001010: int(rule_code[458]), 0b111001011: int(rule_code[459]), \
                    0b111001100: int(rule_code[460]), 0b111001101: int(rule_code[461]), 0b111001110: int(rule_code[462]), 0b111001111: int(rule_code[463]), \
                    0b111010000: int(rule_code[464]), 0b111010001: int(rule_code[465]), 0b111010010: int(rule_code[466]), 0b111010011: int(rule_code[467]), \
                    0b111010100: int(rule_code[468]), 0b111010101: int(rule_code[469]), 0b111010110: int(rule_code[470]), 0b111010111: int(rule_code[471]), \
                    0b111011000: int(rule_code[472]), 0b111011001: int(rule_code[473]), 0b111011010: int(rule_code[474]), 0b111011011: int(rule_code[475]), \
                    0b111011100: int(rule_code[476]), 0b111011101: int(rule_code[477]), 0b111011110: int(rule_code[478]), 0b111011111: int(rule_code[479]), \
                    0b111100000: int(rule_code[480]), 0b111100001: int(rule_code[481]), 0b111100010: int(rule_code[482]), 0b111100011: int(rule_code[483]), \
                    0b111100100: int(rule_code[484]), 0b111100101: int(rule_code[485]), 0b111100110: int(rule_code[486]), 0b111100111: int(rule_code[487]), \
                    0b111101000: int(rule_code[488]), 0b111101001: int(rule_code[489]), 0b111101010: int(rule_code[490]), 0b111101011: int(rule_code[491]), \
                    0b111101100: int(rule_code[492]), 0b111101101: int(rule_code[493]), 0b111101110: int(rule_code[494]), 0b111101111: int(rule_code[495]), \
                    0b111110000: int(rule_code[496]), 0b111110001: int(rule_code[497]), 0b111110010: int(rule_code[498]), 0b111110011: int(rule_code[499]), \
                    0b111110100: int(rule_code[500]), 0b111110101: int(rule_code[501]), 0b111110110: int(rule_code[502]), 0b111110111: int(rule_code[503]), \
                    0b111111000: int(rule_code[504]), 0b111111001: int(rule_code[505]), 0b111111010: int(rule_code[506]), 0b111111011: int(rule_code[507]), \
                    0b111111100: int(rule_code[508]), 0b111111101: int(rule_code[509]), 0b111111110: int(rule_code[510]), 0b111111111: int(rule_code[511])}

    def rule_func(state):
        return rule_dict[state]
    
    return rule_func


# 64 additive rules for Neumann neighborhood
def additive_rule_gen(rule_code):
    # rule_code is a 6-bit binary number: XCNWSE
    def rule(state):
        # state is 5-bit binary number
        # 1st bit is the value of (i-1,j) cell, note as N_v
        # 2nd bit is the value of (i,j-1) cell, note as W_V
        # 3st bit is the value of (i,j)   cell, note as C_v
        # 4th bit is the value of (i,j+1) cell, note as E_v
        # 5th bit is the value of (i+1,j) cell, note as S_v

        X, C, N, W, S, E = [int(i) for i in bin(rule_code)[2:].zfill(6)]        
        N_v, W_v, C_v, E_v, S_v = [int(i) for i in bin(state)[2:].zfill(5)]
        
        next_state = X ^ (C and C_v) ^ (N and N_v) ^ (W and W_v) ^ (S and S_v) ^ (E and E_v)
        
        return next_state
    
    return rule
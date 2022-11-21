

def cleanInstructions(originalSize, instruction_bytes,twobyteInstructions):
    
    index = 0

    while index < originalSize:
        testString = (bin((instruction_bytes[index] << 8) + instruction_bytes[index + 1])) # creating binary string from two bytes
        testString = testString[2:len(testString)] # removing 0b from binary string
        stringLen = len(testString)
        # adding extra zeros to front of byte
        if stringLen < 16:
            zeros = "0" * (16 - stringLen)
            testString = zeros + testString
        twobyteInstructions.append(testString)
        index+=2

    
def machine_to_assembly(instruction):
    
    
    threeSBits = instruction[0:3] #gathering 3 most significant bits
    #print(threeSBits)
    if (threeSBits == "000"):
        # 1, 2
        nextTwoBits = instruction[3:5]

        if (nextTwoBits == "11"):
            # add/subtract
            rd = int(instruction[13:16], 2)
            rs = int(instruction[10:13], 2)
            offset3 = int(instruction[7:10], 2)
            if (instruction[5] == "0"):
                
                if (instruction[6] == "0"):
                    #ADD Rd, Rs, Rn
                    rn = offset3
                    thumbInstruction = ("ADD R%d, R%d, R%d"%(rd,rs,rn))
                    
                elif (instruction[6] == "1"):
                    #ADD Rd, Rs, #Offset3                  
                    thumbInstruction = ("ADD R%d, R%d, #%d"%(rd,rs,offset3))
                    
            elif (instruction[5] == "1"):

                if (instruction[6] == "0"):
                    #SUB Rd, Rs, Rn
                    rn = offset3
                    thumbInstruction = ("SUB R%d, R%d, R%d"%(rd,rs,rn))
                    
                elif (instruction[6] == "1"):
                    #SUB Rd, Rs, #Offset3
                    thumbInstruction = ("SUB R%d, R%d, #%d"%(rd,rs,offset3))
                    
        else:
            rd = int(instruction[13:16], 2)
            rs = int(instruction[10:13], 2)
            offset5 = int(instruction[5:10], 2)
            if (nextTwoBits == "00"):
                #LSL Rd, Rs, #Offset5
                thumbInstruction = ("LSL R%d, R%d, #%d"%(rd,rs,offset5))
                
            elif (nextTwoBits == "01"):
                #LSR Rd, Rs, #Offset5
                thumbInstruction = ("LSR R%d, R%d, #%d"%(rd,rs,offset5))
                
            elif (nextTwoBits == "10"):
                #ASR Rd, Rs, #Offset5
                thumbInstruction = ("ASR R%d, R%d, #%d"%(rd,rs,offset5))
                
    elif(threeSBits == "001"):
        offset8 = int(instruction[8:16], 2)
        rd = int(instruction[5:8], 2)
        nextTwoBits = instruction[3:5]
        if(nextTwoBits == "00"):
            #MOV Rd, #Offset8
            thumbInstruction = ("MOV R%d, #%d"%(rd,offset8))
            
        elif(nextTwoBits == "01"):
            #CMP Rd, #Offset8
            thumbInstruction = ("CMP R%d, #%d"%(rd,offset8))
            
        elif(nextTwoBits == "10"):
            #ADD Rd, #Offset8
            thumbInstruction = ("ADD R%d, #%d"%(rd,offset8))
            
        elif(nextTwoBits == "11"):
            #SUB Rd, #Offset8
            thumbInstruction = ("SUB R%d, #%d"%(rd,offset8))
            

    elif(threeSBits == "010"):
        nextBit = instruction[3]
        if(nextBit=="0"):
            nextBit = instruction[4]
            if(nextBit=="0"):
                nextBit = instruction[5]
                if (nextBit=="0"):
                    rd = int(instruction[13:16], 2)
                    rs = int(instruction[10:13], 2)
                    opCode = instruction[6:10]
                    if (opCode=="0000"):
                        # AND Rd, Rs
                        thumbInstruction = ("AND R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="0001"):
                        #EOR Rd, Rs
                        thumbInstruction = ("EOR R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="0010"):
                        # LSL Rd, Rs
                        thumbInstruction = ("LSL R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="0011"):
                        # LSR Rd, Rs
                        thumbInstruction = ("LSR R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="0100"):
                        # ASR Rd, Rs
                        thumbInstruction = ("ASR R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="0101"):
                        # ADC Rd, Rs
                        thumbInstruction = ("ADC R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="0110"):
                        # SBC Rd, Rs
                        thumbInstruction = ("SBC R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="0111"):
                        # ROR Rd, Rs
                        thumbInstruction = ("ROR R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="1000"):
                        # TST Rd, Rs
                        thumbInstruction = ("TST R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="1001"):
                        # NEG Rd, Rs
                        thumbInstruction = ("NEG R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="1010"):
                        # CMP Rd, Rs
                        thumbInstruction = ("CMP R%d, R%d"%(rd,rs))
                         
                    elif (opCode=="1011"):
                        # CMN Rd, Rs
                        thumbInstruction = ("CMN R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="1100"):
                        # ORR Rd, Rs
                        thumbInstruction = ("ORR R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="1101"):
                        # MUL Rd, Rs
                        thumbInstruction = ("MUL R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="1110"):
                        # BIC Rd, Rs
                        thumbInstruction = ("BIC R%d, R%d"%(rd,rs))
                        
                    elif (opCode=="1111"):
                        # MVN Rd, Rs
                        thumbInstruction = ("MVN R%d, R%d"%(rd,rs))
                        
                    
                elif (nextBit=="1"):
                    opCode = instruction[6:8]
                    h1 = instruction[8]
                    h2 = instruction[9]
                    rshs = int(instruction[10:13], 2)
                    rdhd = int(instruction[13:16], 2)
                    
                    if (opCode == "00"):
                        if ((h1 == "0") and (h2 == "1")):
                            #ADD Rd, Hs
                            thumbInstruction = ("ADD R%d, H%d"%(rdhd,rshs))
                            
                        elif ((h1 == "1") and (h2 == "0")):
                            # ADD Hd, Rs
                            thumbInstruction = ("ADD H%d, R%d"%(rdhd,rshs))
                            
                        elif ((h1 == "1") and (h2 == "1")):
                            #ADD Hd, Hs
                            thumbInstruction = ("ADD H%d, H%d"%(rdhd,rshs))
                            
                    elif (opCode == "01"):
                        if ((h1 == "0") and (h2 == "1")):
                            # CMP Rd, Hs
                            thumbInstruction = ("CMP R%d, H%d"%(rdhd,rshs))
                            
                        elif ((h1 == "1") and (h2 == "0")):
                            # CMP Hd, Rs
                            thumbInstruction = ("CMP H%d, R%d"%(rdhd,rshs))
                            
                        elif ((h1 == "1") and (h2 == "1")):
                            # CMP Hd, Hs
                            thumbInstruction = ("CMP H%d, H%d"%(rdhd,rshs))
                            
                    elif (opCode == "10"):
                        if ((h1 == "0") and (h2 == "1")):
                            # MOV Rd, Hs
                            thumbInstruction = ("MOV R%d, H%d"%(rdhd,rshs))
                            
                        elif ((h1 == "1") and (h2 == "0")):
                            # MOV Hd, Rs
                            thumbInstruction = ("MOV H%d, R%d"%(rdhd,rshs))
                            
                        elif ((h1 == "1") and (h2 == "1")):
                            # MOV Hd, Hs
                            thumbInstruction = ("MOV H%d, H%d"%(rdhd,rshs))
                            
                    elif (opCode == "11"):
                        if ((h1 == "0") and (h2 == "0")):
                            # BX Rs
                            thumbInstruction = ("BX R%d"%rshs)
                            
                        elif ((h1 == "0") and (h2 == "1")):
                            # BX Hs
                            thumbInstruction = ("BX H%d"%rshs)
                              
            elif(nextBit=="1"):
                #LDR Rd, [PC, #Imm]
                word8 = int(instruction[8:16], 2)
                rd = int(instruction[5:8], 2)
                thumbInstruction = ("LDR R%d, [PC, #%d]"%(rd,word8))
                
        elif(nextBit=="1"):
            # 7, 8
            rd = int(instruction[13:16], 2)
            rb = int(instruction[10:13], 2)
            ro = int(instruction[7:10], 2)
            if (instruction[6] == "0"):
                #7
                lb = int(instruction[4:6], 2)
                if (lb == "00"):
                    # STR Rd, [Rb, Ro]
                    thumbInstruction = ("STR R%d, [R%d, R%d]"%(rd,rb,ro))
                    
                elif (lb == "01"):
                    # STRB Rd, [Rb, Ro]
                    thumbInstruction = ("STRB R%d, [R%d, R%d]"%(rd,rb,ro))
                    
                elif (lb == "10"):
                    # LDR Rd, [Rb, Ro]
                    thumbInstruction = ("LDR R%d, [R%d, R%d]"%(rd,rb,ro))
                    
                elif (lb == "11"):
                    # LDRB Rd, [Rb, Ro]
                    thumbInstruction = ("LDRB R%d, [R%d, R%d]"%(rd,rb,ro))
                    
            else:
                #8
                hs = int(instruction[4:6], 2)
                if (hs == "00"):
                    # STRH Rd, [Rb, Ro]
                    thumbInstruction = ("STRH R%d, [R%d, R%d]"%(rd,rb,ro))
                    
                elif (hs == "01"):
                    # LDRH Rd, [Rb, Ro]
                    thumbInstruction = ("LDRH R%d, [R%d, R%d]"%(rd,rb,ro))
                    
                elif (hs == "10"):
                    # LDSB Rd, [Rb, Ro]
                    thumbInstruction = ("LDSB R%d, [R%d, R%d]"%(rd,rb,ro))
                   
                elif (hs == "11"):
                    # LDSH Rd, [Rb, Ro]
                    thumbInstruction = ("LDSH R%d, [R%d, R%d]"%(rd,rb,ro))
                    
    elif(threeSBits == "011"):
        bl = instruction[3:5]
        rd = int(instruction[13:16], 2)
        rb = int(instruction[10:13], 2)
        offset5 = int(instruction[5:10], 2)
        if (bl == "00"):
            # STR Rd, [Rb, #Imm]
            thumbInstruction = ("STR R%d, [R%d, #%d]"%(rd,rb,offset5))
            
        elif (bl == "01"):
            # LDR Rd, [Rb, #Imm]
            thumbInstruction = ("LDR R%d, [R%d, #%d]"%(rd,rb,offset5))
            
        elif (bl == "10"):
            # STRB Rd, [Rb, #Imm]
            thumbInstruction = ("STRB R%d, [R%d, #%d]"%(rd,rb,offset5))
            
        elif (bl == "11"):
            # LDRB Rd, [Rb, #Imm]
            thumbInstruction = ("LDRB R%d, [R%d, #%d]"%(rd,rb,offset5))
            
    elif(threeSBits == "100"):
        #10, 11
        l = instruction[4]
        if (instruction[3] == "0"):
            rd = int(instruction[13:16], 2)
            rb = int(instruction[10:13], 2)
            offset5 = int(instruction[5:10], 2)
            if (l == "0"):
                # STRH Rd, [Rb, #Imm]
                thumbInstruction = ("STRH R%d, [R%d, #%d]"%(rd,rb,offset5))

            elif (l == "1"):
                # LDRH Rd, [Rb, #Imm]
                thumbInstruction = ("LDRH R%d, [R%d, #%d]"%(rd,rb,offset5))
                
        elif (instruction[3] == "1"):
            word8 = int(instruction[8:16], 2)
            rd = int(instruction[5:8], 2)
            if (l == "0"):
                # STR Rd, [SP, #Imm]
                thumbInstruction = ("STR R%d, [SP, #%d]"%(rd,word8))
                
            elif (l == "1"):
                # LDR Rd, [SP, #Imm]
                thumbInstruction = ("LDR R%d, [SP, #%d]"%(rd,word8))
                

    elif(threeSBits == "101"):
        if (instruction[3] == "0"):          
            word8 = int(instruction[8:16], 2)
            rd = int(instruction[5:8], 2)
            sp = instruction[4]
            if(sp == "0"):
                # ADD Rd, PC, #Imm
                thumbInstruction = ("ADD R%d, PC, #%d"%(rd,word8))
                
            elif (sp == "1"):
                # ADD Rd, SP, #Imm
                thumbInstruction = ("ADD R%d, SP, #%d"%(rd,word8))
                
        elif (instruction[3] == "1"):
            if (instruction[4:8]=="0000"):
                s = instruction[8]
                sword7 = int(instruction[9:16], 2)

                if (s == "0"):
                    # ADD SP, #Imm
                    thumbInstruction = ("ADD SP, #%d"%(sword7))
                    
                elif(s == "1"):
                    # ADD SP, #-Imm
                    thumbInstruction = ("ADD SP, #%d"%(-1 * sword7))
                    
            elif (instruction[5:7]=="10"):
                l = instruction[4]
                r = instruction[7]
                rlist = instruction[8:16]
                if (l == "0" and r == "0"):
                    # PUSH { Rlist }
                    thumbInstruction = "PUSH {"
                    length = len(rlist)
                    for i in range(length):
                        if (rlist[length - i - 1] == "1"):
                            thumbInstruction += ("R%d"%i)
                            if ( i != length - 1):
                                thumbInstruction += ", "
                    thumbInstruction += "}"
                    
                elif (l == "0" and r == "1"):
                    # PUSH { Rlist, LR }
                    thumbInstruction = "PUSH {"
                    length = len(rlist)
                    for i in range(length):
                        if (rlist[length - i - 1] == "1"):
                            thumbInstruction += ("R%d, "%i)
                    thumbInstruction += "LR}"
                    
                elif (l == "1" and r == "0"):
                    # POP { Rlist }
                    thumbInstruction = "POP {"
                    length = len(rlist)
                    for i in range(length):
                        if (rlist[length - i - 1] == "1"):
                            thumbInstruction += ("R%d"%i)
                            if ( i != length - 1):
                                thumbInstruction += ", "
                    thumbInstruction += "}"
                    
                elif (l == "1" and r == "1"):
                    # POP { Rlist, PC }
                    thumbInstruction = "POP {"
                    length = len(rlist)
                    for i in range(length):
                        if (rlist[length - i - 1] == "1"):
                            thumbInstruction += ("R%d, "%i)
                    thumbInstruction += "PC}"
                    
    elif(threeSBits == "110"):
        if (instruction[3] == "0"):
        #15
            l = instruction[4]
            rb = int(instruction[5:8], 2)
            rlist = instruction[8:16]
            if (l == "0"):
                # STMIA Rb!, { Rlist }
                thumbInstruction = ("STMIA R%d!, {"%rb)
                length = len(rlist)
                for i in range(length):
                    if (rlist[length - i - 1] == "1"):
                        thumbInstruction += ("R%d"%i)
                        if ( i != length - 1):
                            thumbInstruction += ", "
                thumbInstruction += "}"
                
            elif (l == "1"):
                # LDMIA Rb!, { Rlist }
                thumbInstruction = ("LDMIA R%d!, {"%rb)
                length = len(rlist)
                for i in range(length):
                    if (rlist[length - i - 1] == "1"):
                        thumbInstruction += ("R%d"%i)
                        if ( i != length - 1):
                            thumbInstruction += ", "
                thumbInstruction += "}"
                
        elif (instruction[3:8] == "11111"):
            #17
            value8 = int(instruction[8:16], 2)
            thumbInstruction = "SWI %d"%value8
            
            
        elif (instruction[3] == "1"):
            #16
            cond = instruction[4:8]
            soffset8 = int(instruction[8:16], 2)
            if (cond == "0000"):
                # BEQ label
                thumbInstruction = "BEQ %d"%soffset8
                
            elif (cond == "0001"):
                # BNE label
                thumbInstruction = "BNE %d"%soffset8
                
            elif (cond == "0010"):
                # BCC label
                thumbInstruction = "BCS %d"%soffset8
                
            elif (cond == "0011"):
                # BCC label
                thumbInstruction = "BCC %d"%soffset8
                
            elif (cond == "0100"):
                # BMI label
                thumbInstruction = "BMI %d"%soffset8
                
            elif (cond == "0101"):
                # BPL label
                thumbInstruction = "BPL %d"%soffset8
                
            elif (cond == "0110"):
                # BVS label
                thumbInstruction = "BVS %d"%soffset8
                
            elif (cond == "0111"):
                # BVC label
                thumbInstruction = "BVC %d"%soffset8
                
            elif (cond == "1000"):
                # BHI label
                thumbInstruction = "BHI %d"%soffset8
                
            elif (cond == "1001"):
                # BLS labeL
                thumbInstruction = "BLS %d"%soffset8
               
            elif (cond == "1010"):
                # BGE label
                thumbInstruction = "BGE %d"%soffset8
                
            elif (cond == "1011"):
                # BLT label
                thumbInstruction = "BLT %d"%soffset8
                
            elif (cond == "1100"):
                # BGT label
                thumbInstruction = "BGT %d"%soffset8
                
            elif (cond == "1101"):
                # BLE label
                thumbInstruction = "BLE %d"%soffset8
                
        
    elif(threeSBits == "111"):
        offset11 = int(instruction[5:16], 2)
        if (instruction[3:5] == "00"):
            #18
            thumbInstruction = "B %d"%offset11
            
        elif (instruction[3] == "1"):
            #19
            h = instruction[4]
            if (h == "0"):
                thumbInstruction = "BL %d"%offset11
                

    return thumbInstruction

    

instruction_bytes = []
twobyteInstructions = []
thumbInstructions = []

import os

absolute_path = os.path.dirname(__file__)
relative_path = "input_files/arm_thumb_instructions.bin"
full_path = os.path.join(absolute_path, relative_path)

with open(full_path, 'rb') as inst_file:
    instr_str = inst_file.readlines()[0]
for byte in bytearray(instr_str):
    instruction_bytes.append(byte)

originalSize = len(instruction_bytes)
cleanInstructions(originalSize,instruction_bytes,twobyteInstructions)
newSize = len(twobyteInstructions)

for index in range(newSize):
    instruction = twobyteInstructions[index]
    thumbInstructions.append(machine_to_assembly(instruction))

for instruct in thumbInstructions:
    print(instruct)

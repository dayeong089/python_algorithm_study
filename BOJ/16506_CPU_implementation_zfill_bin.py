import sys
r = sys.stdin.readline

n = int(r())
for _ in range(n):
    oper, rd, ra, rb = r().split(" ")
    result = ""

    c_check = False
    if oper[-1] == 'C':
        c_check = True
        oper = oper[:-1]

    if oper == 'ADD':
        result += "0000"
    elif oper == "SUB":
        result += "0001"
    elif oper == "MOV":
        result += "0010"
    elif oper == "AND":
        result += "0011"
    elif oper == "OR":
        result += "0100"
    elif oper == "NOT":
        result += "0101"
    elif oper == "MULT":
        result += "0110"
    elif oper == "LSFTL":
        result += "0111"
    elif oper == "LSFTR":
        result += "1000"
    elif oper == "ASFTR":
        result += "1001"
    elif oper == "RL":
        result += "1010"
    elif oper == "RR":
        result += "1011"

    if c_check:
        result += "10"
    else:
        result += "00"

    rd_bin = bin(int(rd))
    ra_bin = bin(int(ra))
    rb_bin = bin(int(rb))

    rd_bin = str(rd_bin[2:]).zfill(3)
    ra_bin = str(ra_bin[2:]).zfill(3)
    
    if c_check:
        rb_bin = str(rb_bin[2:]).zfill(4)
    else:
        rb_bin = str(rb_bin[2:]).zfill(3) + "0"

    result += rd_bin + ra_bin + rb_bin
    print(result)
    
    
# 이런식으로 dictionary 만들어서 해결도 가능
OP = {"ADD": 0, "ADDC": 1, "SUB": 2, "SUBC": 3, "MOV": 4, "MOVC": 5,
      "AND": 6, "ANDC": 7, "OR": 8, "ORC": 9, "NOT": 10, "MULT": 12,
      "MULTC": 13, "LSFTL": 14, "LSFTLC": 15, "LSFTR": 16, "LSFTRC": 17,
      "ASFTR": 18, "ASFTRC": 19, "RL": 20, "RLC": 21, "RR": 22, "RRC": 23}
    


key_hex = 0x31465f57655f63344e5f6e30745f4c3176455f744f6733746833525f77455f3472455f6730316e475f744f5f4431655f614c306e65
#key_hex = 0x31465f57655f63344e5f6e30745f733076455f744f6733746832525f77455f3472455f6730316e475f744f5f4431655f614c306e650a # a
msg_hex = 0x727f00340e075a6b3a69146f2d3e3a67403c343e101d052b1a58623d3c1a0e53087c00245b6e00771d1f1005316e08693e24000714 # b

sum_cal = key_hex + msg_hex 
and_calc = key_hex & msg_hex 
min_calc = key_hex  - msg_hex 
xor_calc = key_hex ^ msg_hex 
or_calc = key_hex | msg_hex 

print("and ", str(hex(and_calc)))
print("sum ", str(hex(sum_cal)))
print("min ", str(hex(min_calc)))
print("xor ", str(hex(xor_calc)))
print("or ", str(hex(or_calc)))

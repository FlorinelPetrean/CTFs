buf = []
buf.append("585858587b667463")
buf.append("5858585836646166")
buf.append("5858585830343335")
buf.append("5858585866303831")
buf.append("5858585863346236")
buf.append("5858585839346636")
buf.append("5858585831646164")
buf.append("5858585861643833")
buf.append("5858585834646565")
buf.append("5858585866633734")
buf.append("5858585839663332")
buf.append("5858585833363439")
buf.append("5858585831383435")
buf.append("5858585835323966")
buf.append("5858585830663135")
buf.append("5858585863626435")
buf.append("5858585830373036")
buf.append("585858587d")

bytes_arr = ""
for line in buf:
    bytes_arr = line + bytes_arr
enc_flag = bytearray.fromhex(bytes_arr)
flag = enc_flag[::-1].decode()
flag = flag.replace("XXXX", "")
print(flag)
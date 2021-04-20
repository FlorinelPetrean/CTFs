
from pwn import *
import sys
from string import *


# extended_ascii = [
# 128 "Ç"
# 129 ü
# 130 é 	letter e with acute
# 131 â 	letter a with circumflex
# 132	ä 	letter a with diaeresis
# 133 à 	letter a with grave
# 134 å 	letter a with ring above
# 135	ç 	letter c with cedilla
# 136	ê 	letter e with circumflex
# 137	ë 	letter e with diaeresis
# 138	è 	letter e with grave
# 139	ï 	letter i with diaeresis
# 140	î 	letter i with circumflex
# 141	ì 	letter i with grave
# 142	Ä 	capital letter a with diaeresis
# 143	Å 	capital letter a with ring above
# 144	É 	capital letter e with acute
# 145	æ 	letter ae
# 146	Æ 	capital letter ae
# 147	ô 	letter o with circumflex
# 148	ö 	letter o with diaeresis
# 149	ò 	letter o with grave
# 150	û 	letter u with circumflex
# 151	ù 	letter u with grave
# 152	ÿ 	letter y with diaeresis
# 153	Ö 	capital letter o with diaeresis
# 154	Ü 	capital letter u with diaeresis
# 155	¢ 	letter o with stroke
# 156	£ 	pound sign
# 157	¥ 	yen sign
# 158	₧ 	peseta sign
# 159	ƒ 	letter f with hook
# 160	á 	letter a with acute
# 161	í 	letter i with acute
# 162	ó 	letter o with acute
# 163	ú 	letter u with acute
# 164	ñ 	letter n with tilde
# 165	Ñ 	capital letter n with tilde
# 166	ª 	feminine ordinal indicator
# 167	º 	masculine ordinal indicator
# 168	¿ 	inverted question mark
# 169	⌐ 	reversed not sign
# 170	¬ 	not sign
# 171	½ 	one half
# 172	¼ 	one quarter
# 173	¡ 	inverted exclamation mark
# 174	« 	left double angle quotation mark
# 175	» 	right double angle quotation mark
# 176	░ 	light shade
# 177	▒ 	medium shade
# 178	▓ 	dark shade
# 179	│ 	single vertical
# 180	┤ 	single vertical and left
# 181	╡ 	single vertical and double left
# 182	╢ 	double vertical and single left
# 183	╖ 	double down and single left
# 184	╕ 	single down and double left
# 185 ╣ 	double vertical and left
# 186 ║ 	double vertical
# 187 ╗ 	double down and left
# 188 ╝ 	double up and left
# 189 ╜ 	double up and single left
# 190 ╛ 	single up and double left
# 191 	277 	BF 	1011 1111 	┐ 	single down and left
# 192 	300 	C0 	1100 0000 	└ 	single up and right
# 193 	301 	C1 	1100 0001 	┴ 	single up and horizontal
# 194 	302 	C2 	1100 0010 	┬ 	single down and horizontal
# 195 	303 	C3 	1100 0011 	├ 	single vertical and right
# 196 	304 	C4 	1100 0100 	─ 	single horizontal
# 197 	305 	C5 	1100 0101 	┼ 	single vertical and horizontal
# 198 	306 	C6 	1100 0110 	╞ 	single vertical and double right
# 199 	307 	C7 	1100 0111 	╟ 	double vertical and single right
# 200 	310 	C8 	1100 1000 	╚ 	double up and right
# 201 	311 	C9 	1100 1001 	╔ 	double down and right
# 202 	312 	CA 	1100 1010 	╩ 	double up and horizontal
# 203 	313 	CB 	1100 1011 	╦ 	double down and horizontal
# 204 	314 	CC 	1100 1100 	╠ 	double vertical and right
# 205 	315 	CD 	1100 1101 	═ 	double horizontal
# 206 	316 	CE 	1100 1110 	╬ 	double vertical and horizontal
# 207 	317 	CF 	1100 1111 	╧ 	single up and double horizontal
# 208 	320 	D0 	1101 0000 	╨ 	double up and single horizontal
# 209 	321 	D1 	1101 0001 	╤ 	single down and double horizontal
# 210 	322 	D2 	1101 0010 	╥ 	double down and single horizontal
# 211 	323 	D3 	1101 0011 	╙ 	double up and single right
# 212 	324 	D4 	1101 0100 	╘ 	single up and double right
# 213 	325 	D5 	1101 0101 	╒ 	single down and double right
# 214 	326 	D6 	1101 0110 	╓ 	double down and single right
# 215 	327 	D7 	1101 0111 	╫ 	double vertical and single horizontal
# 216 	330 	D8 	1101 1000 	╪ 	single vertical and double horizontal
# 217 	331 	D9 	1101 1001 	┘ 	single up and left
# 218 	332 	DA 	1101 1010 	┌ 	single down and right
# 219 	333 	DB 	1101 1011 	█ 	full block
# 220 	334 	DC 	1101 1100 	▄ 	bottom half block
# 221 	335 	DD 	1101 1101 	▌ 	left half block
# 222 	336 	DE 	1101 1110 	▐ 	right half block
# 223 	337 	DF 	1101 1111 	▀ 	top half block
# 224 	340 	E0 	1110 0000 	α 	greek letter alpha
# 225 	341 	E1 	1110 0001 	ß 	letter sharp s
# 226 	342 	E2 	1110 0010 	Γ 	greek capital letter gamma
# 227 	343 	E3 	1110 0011 	π 	greek letter pi
# 228 	344 	E4 	1110 0100 	Σ 	greek capital letter sigma
# 229 	345 	E5 	1110 0101 	σ 	greek letter sigma
# 230 	346 	E6 	1110 0110 	µ 	micro sign
# 231 	347 	E7 	1110 0111 	τ 	greek letter tau
# 232 	350 	E8 	1110 1000 	Φ 	greek capital letter phi
# 233 	351 	E9 	1110 1001 	Θ 	greek capital letter theta
# 234 	352 	EA 	1110 1010 	Ω 	greek capital letter omega
# 235 	353 	EB 	1110 1011 	δ 	greek letter delta
# 236 	354 	EC 	1110 1100 	∞ 	infinity
# 237 	355 	ED 	1110 1101 	φ 	greek letter phi
# 238 	356 	EE 	1110 1110 	ε 	greek letter epsilon
# 239 	357 	EF 	1110 1111 	∩ 	intersection
# 240 	360 	F0 	1111 0000 	≡ 	identical to
# 241 	361 	F1 	1111 0001 	± 	plus-minus sign
# 242 	362 	F2 	1111 0010 	≥ 	greater than or equal to
# 243 	363 	F3 	1111 0011 	≤ 	less than or equal to
# 244 	364 	F4 	1111 0100 	⌠ 	top half integral
# 245 	365 	F5 	1111 0101 	⌡ 	bottom half integral
# 246 	366 	F6 	1111 0110 	÷ 	division sign
# 247 	367 	F7 	1111 0111 	≈ 	almost equal to
# 248 	370 	F8 	1111 1000 	° 	degree sign
# 249 	371 	F9 	1111 1001 	∙ 	bullet operator
# 250 	372 	FA 	1111 1010 	· 	middle dot
# 251 	373 	FB 	1111 1011 	√ 	square root
# 252 	374 	FC 	1111 1100 	ⁿ 	superscript n
# 253 	375 	FD 	1111 1101 	² 	superscript 2
# 254 	376 	FE 	1111 1110 	■ 	black square
# 255 	377 	FF 	1111 1111 		no-break space
# ]

IP = "35.198.162.194"
port =31489

p = remote(IP, port)

p.recvuntil("What is the value of <<")
number = p.recvuntil(">>")
print(number[:-2])

hex_value = hex(int(number[:-2]))
print(f"hex number: {hex_value}\n")
p.recvuntil("Input: ")
p.sendline(str(hex_value))

p.recvuntil("What is the value of <<")
string = p.recvuntil(">>")[:-2]
p.recv
print(string)
string_value = ""

for i in range(0, len(string), 2):
    ascii_aux = string[i:i+2]
    number = int(ascii_aux, base=16)
    char = chr(number)
    string_value = string_value + char
print(string_value)
p.recvuntil("\n")
p.recvuntil("Input:")
p.sendline(string_value)


another_string = u''
p.recvuntil("What is the value of <<")
for i in range(10):
    if i != 10:
        aux = p.recvuntil(" ")
    else:
        aux = p.recvuntil(">>")
    print(aux[1:-1])
    number = int(aux[1:-1])
    char = chr(number)
    another_string = another_string + char.decode('latin-1')
print(another_string)

p.recvuntil("Input:")
p.sendline(another_string)

flag = str(p.recv())
print(flag)
p.interactive()
    

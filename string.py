#string conversions
#string datatype to another datatype


#implicit
a = "Navya"
print(a)
print(type(a))

#explicit
a = str("Navya")
print(a)
print(type(a))

#Data type /variable annotation
a: str = "Navya"
print(a)
print(type(a))

#binary
a = str(0b1100)
print(a)
print(type(a))

#octal
a = str(0o456)
print(a)
print(type(a))

#hexa
a = str(0xface)
print(a)
print(type(a))

#boolean
a = str(False)
print(a)
print(type(a))

#b00lean conversion
a = bool(1)
print(a)
print(type(a))

#hexa conversion
a = hex(0x34)
print(a)
print(type(a))

#octal conversion
a = oct(0o45)
print(a)
print(type(a))

#binary conversion
a = bin(0b1001)
print(a)
print(type(a))
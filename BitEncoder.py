import streamlit as st
import pandas as pd

st.title("Text-To-Bit Encoder")
st.write("---")

sep = st.radio("Character Separators", ["Off (Default)", "On"])
uin = list(st.text_input("Enter text to convert here:"))
uout = []
err = 0

for i in uin:
	
	if i == " ":
		uout.append(32)
	
	elif i == "!":
		uout.append(33)
	
	elif i == "\"":
		uout.append(34)
	
	elif i == "#":
		uout.append(35)
	
	elif i == "$":
		uout.append(36)
	
	elif i == "%":
		uout.append(37)
	
	elif i == "&":
		uout.append(38)
	
	elif i == "'":
		uout.append(39)
	
	elif i == "(":
		uout.append(40)
	
	elif i == ")":
		uout.append(41)
	
	elif i == "*":
		uout.append(42)
	
	elif i == "+":
		uout.append(43)
	
	elif i == ",":
		uout.append(44)
	
	elif i == "-":
		uout.append(45)
	
	elif i == ".":
		uout.append(46)
	
	elif i == "/":
		uout.append(47)
	
	elif i == "0":
		uout.append(48)
	
	elif i == "1":
		uout.append(49)
	
	elif i == "2":
		uout.append(50)
	
	elif i == "3":
		uout.append(51)
	
	elif i == "4":
		uout.append(52)
	
	elif i == "5":
		uout.append(53)
	
	elif i == "6":
		uout.append(54)
	
	elif i == "7":
		uout.append(55)
	
	elif i == "8":
		uout.append(56)
	
	elif i == "9":
		uout.append(57)
	
	elif i == ":":
		uout.append(58)
	
	elif i == ";":
		uout.append(59)
	
	elif i == "<":
		uout.append(60)
	
	elif i == "=":
		uout.append(61)
	
	elif i == ">":
		uout.append(62)
	
	elif i == "?":
		uout.append(63)
	
	elif i == "@":
		uout.append(64)
		
	elif i == "A":
		uout.append(65)

	elif i == "B":
		uout.append(66)

	elif i == "C":
		uout.append(67)

	elif i == "D":
		uout.append(68)

	elif i == "E":
		uout.append(69)

	elif i == "F":
		uout.append(70)

	elif i == "G":
		uout.append(71)

	elif i == "H":
		uout.append(72)

	elif i == "I":
		uout.append(73)

	elif i == "J":
		uout.append(74)

	elif i == "K":
		uout.append(75)

	elif i == "L":
		uout.append(76)

	elif i == "M":
		uout.append(77)

	elif i == "N":
		uout.append(78)

	elif i == "O":
		uout.append(79)

	elif i == "P":
		uout.append(80)

	elif i == "Q":
		uout.append(81)

	elif i == "R":
		uout.append(82)

	elif i == "S":
		uout.append(83)

	elif i == "T":
		uout.append(84)

	elif i == "U":
		uout.append(85)

	elif i == "V":
		uout.append(86)

	elif i == "W":
		uout.append(87)

	elif i == "X":
		uout.append(88)

	elif i == "Y":
		uout.append(89)

	elif i == "Z":
		uout.append(90)

	elif i == "[":
		uout.append(91)

	elif i == "/":
		uout.append(92)

	elif i == "]":
		uout.append(93)

	elif i == "^":
		uout.append(94)

	elif i == "_":
		uout.append(95)

	elif i == "`":
		uout.append(96)

	elif i == "a":
		uout.append(97)

	elif i == "b":
		uout.append(98)

	elif i == "c":
		uout.append(99)

	elif i == "d":
		uout.append(100)

	elif i == "e":
		uout.append(101)

	elif i == "f":
		uout.append(102)

	elif i == "g":
		uout.append(103)

	elif i == "h":
		uout.append(104)

	elif i == "i":
		uout.append(105)

	elif i == "j":
		uout.append(106)

	elif i == "k":
		uout.append(107)

	elif i == "l":
		uout.append(108)

	elif i == "m":
		uout.append(109)

	elif i == "n":
		uout.append(110)

	elif i == "o":
		uout.append(111)

	elif i == "p":
		uout.append(112)

	elif i == "q":
		uout.append(113)

	elif i == "r":
		uout.append(114)

	elif i == "s":
		uout.append(115)

	elif i == "t":
		uout.append(116)

	elif i == "u":
		uout.append(117)

	elif i == "v":
		uout.append(118)

	elif i == "w":
		uout.append(119)

	elif i == "x":
		uout.append(120)

	elif i == "y":
		uout.append(121)

	elif i == "z":
		uout.append(122)

	elif i == "{":
		uout.append(123)

	elif i == "|":
		uout.append(124)

	elif i == "}":
		uout.append(125)

	elif i == "~":
		uout.append(126)

	else:
		err = 1
		break

if err == 1:
	st.write("Invalid input. You may have characters that are not supported on this software.")

elif uin == []:
	pass

else:

	st.write("---")

	for i in range(len(uout)):

		conv = ["0", "0", "0", "0", "0", "0", "0", "0"]
		val = uout[i]

		if val >= 64:
			val -= 64
			conv[1] = "1"
		if val >= 32:
			val -= 32
			conv[2] = "1"
		if val >= 16:
			val -= 16
			conv[3] = "1"
		if val >= 8:
			val -= 8
			conv[4] = "1"
		if val >= 4:
			val -= 4
			conv[5] = "1"
		if val >= 2:
			val -= 2
			conv[6] = "1"
		if val >= 1:
			val -= 1
			conv[7] = "1"

		uout[i] = "".join(conv[:])

	if sep == "Off (Default)":
		uout = " ".join(uout)
	else:
		uout = " | ".join(uout)

	st.header("Output")
	st.write(uout)

	name = st.text_input("File Name:")

	if name == "":
		st.download_button(label="Download Message", data=uout, file_name="Message.txt", mime="text/plain")

	elif name[-4:] != ".txt":
		name = name + ".txt"
		st.download_button(label="Download Message", data=uout, file_name=name, mime="text/plain")

	else:
		st.download_button(label="Download Message", data=uout, file_name=name, mime="text/plain")

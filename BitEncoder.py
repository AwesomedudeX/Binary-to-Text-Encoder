
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Text-to-Bit Encoder")

try:

	st.title("Text-to-Bit Encoder")
	st.write("---")

	err = 0
	c1, c2, c3, c4, c5, c6 = st.columns(6)
	mode = c1.selectbox("Conversion Mode:", ["ASCII Text to Binary", "Binary to ASCII Text"])
	uout = []

	if mode == "ASCII Text to Binary":

		sep = st.radio("Character Separators", ["Off (Default)", "On"])
		uin = list(st.text_input("Enter text to encode here:"))

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


##################################################################################################################################################


	if mode == "Binary to ASCII Text":

		uin = st.text_input("Enter code to decode here:")
		txt = []

		if " | " in uin:
			uin = uin.split(" | ")

		else:
			uin = uin.split(" ")

		for x in range(len(uin)):
			
			bit = list(uin[x])
			val = 0

			for y in range(len(bit)):

				val = 0

				if bit[0] == "1":
					val += 128
				if bit[1] == "1":
					val += 64
				if bit[2] == "1":
					val += 32
				if bit[3] == "1":
					val += 16
				if bit[4] == "1":
					val += 8
				if bit[5] == "1":
					val += 4
				if bit[6] == "1":
					val += 2
				if bit[7] == "1":
					val += 1

			if val != 0:
				uout.append(val)


		for x in uout:

			if x == 32:
				txt.append(" ")
			
			elif x == 33:
				txt.append("!")
			
			elif x == 34:
				txt.append("\"")
			
			elif x == 35:
				txt.append("#")
			
			elif x == 36:
				txt.append("$")
			
			elif x == 37:
				txt.append("%")
			
			elif x == 38:
				txt.append("&")
			
			elif x == 39:
				txt.append("&")
			
			elif x == 40:
				txt.append("(")
			
			elif x == 41:
				txt.append(")")
			
			elif x == 42:
				txt.append("*")
			
			elif x == 43:
				txt.append("+")
			
			elif x == 44:
				txt.append(",")
			
			elif x == 45:
				txt.append("-")
			
			elif x == 46:
				txt.append(".")
			
			elif x == 47:
				txt.append("/")
			
			elif x == 48:
				txt.append("0")
			
			elif x == 49:
				txt.append("1")
			
			elif x == 50:
				txt.append("2")
			
			elif x == 51:
				txt.append("3")
			
			elif x == 52:
				txt.append("4")
			
			elif x == 53:
				txt.append("5")
			
			elif x == 54:
				txt.append("6")
			
			elif x == 55:
				txt.append("7")
			
			elif x == 56:
				txt.append("8")
			
			elif x == 57:
				txt.append("9")
			
			elif x == 58:
				txt.append(":")
			
			elif x == 59:
				txt.append(";")

			elif x == 60:
				txt.append("<")
			
			elif x == 61:
				txt.append("=")
			
			elif x == 62:
				txt.append(">")
			
			elif x == 63:
				txt.append("?")
			
			elif x == 64:
				txt.append("@")
				
			elif x == 65:
				txt.append("A")

			elif x == 66:
				txt.append("B")

			elif x == 67:
				txt.append("C")

			elif x == 68:
				txt.append("D")

			elif x == 69:
				txt.append("E")

			elif x == 70:
				txt.append("F")

			elif x == 71:
				txt.append("G")

			elif x == 72:
				txt.append("H")

			elif x == 73:
				txt.append("I")

			elif x == 74:
				txt.append("J")

			elif x == 75:
				txt.append("K")

			elif x == 76:
				txt.append("L")

			elif x == 77:
				txt.append("M")

			elif x == 78:
				txt.append("N")

			elif x == 79:
				txt.append("O")

			elif x == 80:
				txt.append("P")

			elif x == 81:
				txt.append("Q")

			elif x == 82:
				txt.append("R")

			elif x == 83:
				txt.append("S")

			elif x == 84:
				txt.append("T")

			elif x == 85:
				txt.append("U")

			elif x == 86:
				txt.append("V")

			elif x == 87:
				txt.append("W")

			elif x == 88:
				txt.append("X")

			elif x == 89:
				txt.append("Y")

			elif x == 90:
				txt.append("Z")

			elif x == 91:
				txt.append("[")

			elif x == 92:
				txt.append("/")

			elif x == 93:
				txt.append("]")

			elif x == 94:
				txt.append("^")

			elif x == 95:
				txt.append("_")

			elif x == 96:
				txt.append("`")

			elif x == 97:
				txt.append("a")

			elif x == 98:
				txt.append("b")

			elif x == 99:
				txt.append("c")

			elif x == 100:
				txt.append("d")

			elif x == 101:
				txt.append("e")

			elif x == 102:
				txt.append("f")

			elif x == 103:
				txt.append("g")

			elif x == 104:
				txt.append("h")

			elif x == 105:
				txt.append("i")

			elif x == 106:
				txt.append("j")

			elif x == 107:
				txt.append("k")

			elif x == 108:
				txt.append("l")

			elif x == 109:
				txt.append("m")

			elif x == 110:
				txt.append("n")

			elif x == 111:
				txt.append("o")

			elif x == 112:
				txt.append("p")

			elif x == 113:
				txt.append("q")

			elif x == 114:
				txt.append("r")

			elif x == 115:
				txt.append("s")

			elif x == 116:
				txt.append("t")

			elif x == 117:
				txt.append("u")

			elif x == 118:
				txt.append("v")

			elif x == 119:
				txt.append("w")

			elif x == 120:
				txt.append("x")

			elif x == 121:
				txt.append("y")

			elif x == 122:
				txt.append("z")

			elif x == 123:
				txt.append("{")

			elif x == 124:
				txt.append("|")

			elif x == 125:
				txt.append("}")

			elif x == 126:
				txt.append("~")

			else:
				err = 1
				break

		uout = "".join(txt)

		if err == 1:
			st.write("Invalid input. You may have bit codes that are not supported on this software.")

		elif uin == []:
			pass

		else:

			st.write("---")
			st.header("Output")
			st.write(uout)

			name = st.text_input("File Name:")

			if name == "":
				st.download_button(label="Download Message", data="uout", file_name="Message.txt", mime="text/plain")

			elif name[-4:] != ".txt":
				name = name + ".txt"
				st.download_button(label="Download Message", data="uout", file_name=name, mime="text/plain")

			else:
				st.download_button(label="Download Message", data="uout", file_name=name, mime="text/plain")

except:
	st.write("There was an error. Please refresh the page and try again.")

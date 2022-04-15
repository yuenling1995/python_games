import sys



bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""



print("Bitmap Message, by Al Sweigart al@inventwithpython.com")
message = input("Enter the message to display with the bitmap:\n")
if message == "":
	sys.exit()

# loop over each line in the bitmap
for line in bitmap.splitlines():
	for i, bit in enumerate(line):
		if bit == " ":
			# print an empty space since there's a space in the bitmap
			print(" ", end = "")
		else:
			# print a character from the message
			print(message[i % len(message)], end = "")





import qrcode

name = str(input("enter your name : "))
phone_number = input("enter your phone number: ")

qr_code = "name :" +" "+name+ " "+"phone number :"+ " " + phone_number

qr = qrcode.make(qr_code)
qr.save("myqr code.png")
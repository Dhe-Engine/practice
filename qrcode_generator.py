import qrcode

upi_id = input("enter upi id: ")

phone_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

#create qr code for each payment app
phone_qr = qrcode.make(phone_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save qr code
phone_qr.save('phone_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_qr.png')

phone_qr.show()
paytm_qr.show()
google_pay_qr.show()
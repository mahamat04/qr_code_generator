import qrcode

def generate_qrcode(text):
    code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=5,
    )

    code.add_data(text)
    code.make(fit=True)
    img = code.make_image(fill_color="gray", back_color="white")
    img.save("qrcode.png")


generate_qrcode('This is beta test!')
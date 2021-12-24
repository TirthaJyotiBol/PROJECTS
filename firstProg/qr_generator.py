
import qrcode as q   # -> Generate QR CODE
import cv2 as c      # -> Detect QR code

# Make QR code
img = q.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
img.save("firstQR.jpg")

img2 = q.make("Hello This is Tirtha")
img2.save("second2.jpg")


# Detect the QR code
d = c.QRCodeDetector()
val, points, qr = d.detectAndDecode(c.imread("second2.jpg"))
print(val)
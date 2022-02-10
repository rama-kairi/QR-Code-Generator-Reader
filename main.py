# Generate QR Code
import cv2

from qrcode import QRCode


def generate_qr(data: str, filename: str) -> None:
    """Generate QR Code"""
    qr = QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(filename)


def read_qr(img: str) -> str:
    """Read QR Code"""
    qr = cv2.imread(img)
    detecttor = cv2.QRCodeDetector()
    data, bbox, _ = detecttor.detectAndDecode(qr)

    return data


if __name__ == "__main__":
    generate_qr("Hello World!", "qr_code.png")
    generate_qr("Hello Rama!", "rama.png")
    print(read_qr("qr_code.png"))
    print(read_qr("rama.png"))

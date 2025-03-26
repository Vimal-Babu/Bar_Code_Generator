import barcode
from barcode.writer import ImageWriter
from PIL import Image

# Available barcode types
barcode_types = {
    "1" : "code128",
    "2" : "ean13",
    "3" : "ean8",
}

def generate_barcode(barcode_format, barcode_data):
    """Generates and saves a barcode."""
    barcode_class = barcode.get_barcode_class(barcode_format)
    barcode_obj = barcode_class(barcode_data, writer=ImageWriter())
    filename = barcode_obj.save(f"barcode_{barcode_data}")
    
    print(f"✅ Barcode saved as {filename}.png")
    
    # Open and display the barcode
    image = Image.open(f"{filename}")
    image.show()

# User input for barcode type
print("---📌 Choose a barcode format:---")
print(" 1️⃣  Code128 (alphanumeric)")
print(" 2️⃣  EAN-13 (only numbers, 13 digits)")
print(" 3️⃣  EAN-8 (only numbers, 8 digits)")
barcode_choice = input("Enter your choice (1 or 2 or 3): ")

if barcode_choice in barcode_types:
    barcode_format = barcode_types[barcode_choice]
    barcode_data = input(" 🔢  Enter barcode data: ")
    
    try:
        generate_barcode(barcode_format, barcode_data)
    except Exception as e:
        print(f"❌ Error: {e}")
else:
    print("⚠️ Invalid choice! Please enter 1, 2, or 3.")

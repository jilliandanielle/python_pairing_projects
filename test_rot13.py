from rot13 import rotate13

def test_simple_encryption():
    encrypted_text = rotate13("This is a banana fruitcake.")
    assert encrypted_text == "Guvf vf n onanan sehvgpnxr."

def test_simple_decryption():
    plaintext = rotate13("Guvf vf n onanan sehvgpnxr.")
    assert plaintext == "This is a banana fruitcake."

def test_empty_string():
    encrypted_text = rotate13("")
    assert encrypted_text == ""



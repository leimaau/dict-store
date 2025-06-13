# -*- coding: utf8 -*-

from __future__ import unicode_literals, print_function, absolute_import, division

# This file contains examples of how to use the different features of the writemdict library.
# Run it with "python examples.py". It will create various .mdx files in the example_output/
# directory.

from writemdict import MDictWriter, encrypt_key
from ripemd128 import ripemd128
import io


# This is the dictionary we will use.
d = {
    "alpha":"<i>alpha</i>",
    "beta":"Letter <b>beta</b>",
    "gamma":"Capital version is Γ &lt;"}




### Example 1: Basic writing. All options default.
outfile = open("example_output/basic.mdx", "wb")
writer = MDictWriter(d, "Basic dictionary", "This is a basic test dictionary.")
writer.write(outfile)
outfile.close()


### Example 2: Demonstrates the use of UTF-16 encoding.
outfile = open("example_output/utf16.mdx", "wb")
writer = MDictWriter(d, 
                     "UTF-16 dictionary", 
                     "This is a test for the \"UTF-16\" encoding.",
                     encoding="utf-16")
writer.write(outfile)
outfile.close()

### Example 3: This is a test to create a UTF-16 dictionary containing characters outside the
#              Basic Multilingual Plane
d2 = {"𩷶":"A fish"}
outfile = open("example_output/utf16nonbmp.mdx", "wb")
writer = MDictWriter(d2, 
                     "UTF16 non-BMP dictionary", 
                     "This test support for characters outside the Basic Multilingual Plane",
                     encoding="utf-16")
writer.write(outfile)
outfile.close()

### Example 4: Uses the Big5 encoding.
outfile = open("example_output/big5.mdx", "wb")
writer = MDictWriter(d, 
                     "Big5 dictionary",
                     "This is a test for the \"Big5\" encoding.",
                     encoding="big5")
writer.write(outfile)
outfile.close()

### Example 5: Uses the GBK encoding.
outfile = open("example_output/gbk.mdx", "wb")
writer = MDictWriter(d, 
                     "GBK dictionary", 
                     "This is a test for the \"GBK\" encoding", 
                     encoding="gbk")
writer.write(outfile)
outfile.close()


### Example 6: Demonstrate encryption of the keyword index. (Option "Disallow export" in MdxBuilder.)
outfile = open("example_output/key_index_encryption.mdx", "wb")
writer = MDictWriter(d, 
                     "Dictionary disallowing export",
                     "This dictionary demonstrates keyword index encryption",
                     encrypt_index=True)
writer.write(outfile)
outfile.close()

### Example 7: Use version 1.2 of the file format instead.
outfile = open("example_output/version12.mdx", "wb")
writer = MDictWriter(d, 
                     "Version 1.2 dictionary",
                     "This dictionary tests version 1.2 of the file format",
                     version="1.2")
writer.write(outfile)
outfile.close()

### Example 8: A version 1.2 dictionary using UTF-16.
outfile = open("example_output/version12utf16.mdx", "wb")
writer = MDictWriter(d, 
                     "Version 1.2 UTF-16 dictionary",
                     "This dictionary tests version 1.2 of the file format, using UTF-16",
                     encoding="utf16",
                     version="1.2")
writer.write(outfile)
outfile.close()

### Example 9: Encryption test, using an external .key file, and the user email.
#              This creates two files: encrypted_external_regcode.mdx and encrypted_external_regcode.key.
#              To open, the user needs to set his/her email to "example@example.com" in the MDict reader.
outfile = open("example_output/encrypted_external_regcode.mdx", "wb")
writer = MDictWriter(d,
                     "Encrypted dictionary",
                     "This dictionary tests encryption",
                     encoding="utf16",
                     version="2.0",
                     encrypt_key=b"abc",
                     register_by="email")
writer.write(outfile)
outfile.close()
key = encrypt_key(b"abc", email="example@example.com")
keyfile = io.open("example_output/encrypted_external_regcode.key", "w", encoding="ascii")
keyfile.write(key)
keyfile.close()

### Example 10: Encryption test, with the registration code supplied with the dictionary.
#               To open, the user needs to set his/her email to "example@example.com" in the MDict reader.
outfile = open("example_output/encrypted_internal_regcode.mdx", "wb")
writer = MDictWriter(d, 
                     "Encrypted dictionary",
                     "This dictionary tests encryption, with key supplied in dictionary header",
                     encoding="utf16",
                     version="2.0",
                     encrypt_key=b"abc",
                     register_by="email",
                     user_email="example@example.com")
writer.write(outfile)
outfile.close()


### Example 11: Encryption test, using an external .key file, and the DeviceID.
#              This creates two files: encrypted_external_regcode.mdx and encrypted_external_regcode.key.
#              To open, the user's deviceID (in the MDict client) needs to be
#              "12345678-9012-3456-7890-1234"      
outfile = open("example_output/encrypted_external_regcode_device_id.mdx", "wb")
writer = MDictWriter(d,
                     "Encrypted dictionary",
                     "This dictionary tests encryption, using the DeviceID method",
                     encoding="utf8",
                     version="2.0",
                     encrypt_key=b"abc",
                     register_by="device_id")
writer.write(outfile)
outfile.close()
key = encrypt_key(b"abc", device_id="")
keyfile = io.open("example_output/encrypted_external_regcode_device_id.key", "w", encoding="ascii")
keyfile.write(key)
keyfile.close()

### Example 12: Encryption test, with the registration code supplied with the dictionary.
#              To open, the user's deviceID (in the MDict client) needs to be
#              "12345678-9012-3456-7890-1234"      
outfile = open("example_output/encrypted_internal_regcode_device_id.mdx", "wb")
writer = MDictWriter(d, 
                     "Encrypted dictionary",
                     "This dictionary tests encryption using the DeviceID method, with key supplied in dictionary header",
                     encoding="utf8",
                     version="2.0",
                     encrypt_key=b"abc",
                     register_by="device_id",
                     user_device_id="")
writer.write(outfile)
outfile.close()


### Example 13: Basic dictionary, with no compression. 
outfile = open("example_output/no_compression.mdx", "wb")
writer = MDictWriter(d,
                     "Uncompressed dictionary",
                     "This is a test of the basic dictionary, with compression type 0 (no compression).",
                     compression_type=0)
writer.write(outfile)
outfile.close()

### Example 14: Basic dictionary, with LZO compression:
#               Only works if python-lzo is installed.
outfile = open("example_output/lzo_compression.mdx", "wb")
try:
	writer = MDictWriter(d, "LZO compressed dictionary", "This tests the LZO compression type.", compression_type=1)
	writer.write(outfile)
except NotImplementedError:
	print("python-lzo not installed. Skipping LZO test.")
outfile.close()

### Example 15: MDD file.
outfile_mdx = open("example_output/mdd_file.mdx", "wb")
d3 = {"red": """Like this: <img src="file:///red.png" />"""}
writer = MDictWriter(d3, "Dictionary with MDD file", "This dictionary tests MDD file handling.")
writer.write(outfile_mdx)
outfile_mdx.close()

# A raw PNG file, with size 10x10, all red.
raw_image = (b"\x89PNG\r\n\x1a\n"
             b"\0\0\0\x0dIHDR"
             b"\0\0\0\x0a\0\0\0\x0a\x08\x02\x00\x00\x00"
             b"\x02\x50\x58\xea"
             b"\x00\x00\x00\x12IDAT"
             b"\x18\xd3\x63\xfc\xcf\x80\x0f\x30\x31\x8c\x4a\x63\x01\x00\x41\x2c\x01\x13"
             b"\x65\x62\x10\x33"
             b"\0\0\0\0IEND"
             b"\xae\x42\x60\x82")

outfile_mdd = open("example_output/mdd_file.mdd", "wb")
d_mdd = {"\\red.png": raw_image}
writer = MDictWriter(d_mdd, "Dictionary with MDD file", "This dictionary tests MDD file handling.", is_mdd=True)
writer.write(outfile_mdd)
outfile_mdd.close()
	



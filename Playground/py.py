# from struct import pack
# nseh = pack("<L", 0x06eb9090) 
# seh = pack("<L", 0x1001ae86) 
# print(nseh, seh)


# import os
# import hashlib
# from pyDes import des, CBC, PAD_PKCS5

# def restore(dest_dir):
#     for filename in os.listdir(dest_dir):
#         filepath = os.path.join(dest_dir, filename)
#         with open(filepath, 'rb') as src:
#             data = src.read()
#             k = des(b"87629ae8", CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
#             try:
#                 plaintext = k.decrypt(data)
#             except:
#                 continue  # skip this file if decryption fails
#         restored_filename = hashlib.sha224(plaintext).hexdigest()
#         restored_filepath = os.path.join(dest_dir, restored_filename)
#         with open(restored_filepath, 'wb') as dest:
#             dest.write(plaintext)
#         print(f"Restored {filepath} to {restored_filepath}")

# if __name__ == '__main__':
#     dest_dir = "E:\OSCP\data"
#     restore(dest_dir)

import base64

def encode_file(file_name, new_file_name):
    with open(file_name, 'rb') as file:
        encoded_file = base64.b64encode(file.read())
        with open(new_file_name, 'w') as new_file:
            new_file.write('<?php eval(base64_decode({}));?>'.format(encoded_file))

encode_file('file.php', 'file_encoded.php')

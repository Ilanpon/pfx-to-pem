from OpenSSL import crypto
import argparse
from os import path

parser = argparse.ArgumentParser(prog='PFXtoPEM', description='Converts MS stuff to the superior format')
parser.add_argument('-password', type=str, nargs='?', default='', required=False, help='The password used for the cert')
parser.add_argument('-file', type=str, nargs='?', default='', required=True, help='The path to pfx file')
args = parser.parse_args()

pfx_password = args.password
pfx_file = args.file


def convertpfx(password, file):
    # open the input file and extract data
    with open(file, 'rb') as pfx:
        pem_converter = crypto.load_pkcs12(pfx.read(), password)
        pem_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, pem_converter.get_privatekey())
        pem_cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pem_converter.get_certificate())

    # write key
    pem_file = path.splitext(file)[0]
    with open(pem_file + '-key.pem', 'wb') as file:
        file.write(pem_key)

    # write cert
    with open(pem_file + '-cert.pem', 'wb') as file:
        file.write(pem_cert)

    # write ca, if any
    with open(pem_file + '-ca.pem', 'wb') as file:
        ca = pem_converter.get_ca_certificates()
        if ca is not None:
            for cert in ca:
                file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

if __name__ == "__main__":
    print(f'Converting {pfx_file} to PEM')
    convertpfx(pfx_password, pfx_file)
    




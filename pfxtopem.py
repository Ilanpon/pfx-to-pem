from OpenSSL import crypto
import argparse
from os import path


parser = argparse.ArgumentParser(
    prog='PFXtoPEM',
    description='Converts MS stuff to the superior format and uploads it to Vault, if you specify the URL'
)

parser.add_argument('-password', type=str, nargs='?', default='',
                    help='The password used for the cert')

parser.add_argument('-file', type=str, nargs='?', default='', required=True,
                    help='The path to pfx file')


args = parser.parse_args()

pfx_password = args.password
pfx_file = args.file


class PemFormat:
    def convertpfx(self, password, file):
        # open the input file and extract data
        print(f'Converting {file} to PEM \n')

        with open(file, 'rb') as pfx:
            pem_converter = crypto.load_pkcs12(pfx.read(), password)
            self.pem_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, pem_converter.get_privatekey())
            self.pem_cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pem_converter.get_certificate())

        # write key
        pem_file = path.splitext(file)[0]
        with open(pem_file + '-key.pem', 'wb') as file:
            print(f'Writing key to {file.name}')
            file.write(self.pem_key)

        # write cert
        with open(pem_file + '-cert.pem', 'wb') as file:
            print(f'Writing cert to {file.name}')
            file.write(self.pem_cert)

        # write ca, if any
        with open(pem_file + '-ca.pem', 'wb') as file:
            ca = pem_converter.get_ca_certificates()
            if ca is not None:
                print(f'Writing ca data to {file.name} \n')
                for cert in ca:
                    self.pem_ca = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)
                    file.write(self.pem_ca)


if __name__ == "__main__":
    converter = PemFormat()
    converter.convertpfx(pfx_password, pfx_file)







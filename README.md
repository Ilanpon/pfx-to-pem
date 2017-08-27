# Usage
pfxtopem.py -password PASSWORD -file "full/path/to/file.pfx"

This will extract the key, cert, and ca from the pfx. I wrote this when I set up an Active Directory CA and had to transfer a lot of certs to linux systems quickly
Check out Vault-PEMfx if you want a tool like this that also uploads the secrets to Vault

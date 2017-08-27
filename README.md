# Usage
pfxtopem.py -password PASSWORD -file "full/path/to/file.pfx"

This will extract the key, cert, and ca from the pfx. I wrote this when I set up an Active Directory CA and had to transfer a lot of certs to linux systems quickly

Based on this script, I wrote [Vault-PEMfx](https://github.com/Ilanpon/Vault-PEMfx) to use in production which does all this and integrates with Vault i.e. convert pfx -> PEM, upload to Vault

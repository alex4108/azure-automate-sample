from azure.storage.blob import ContainerClient

storageCred['username'] = 'my-storage-account-name'
storageCred['password'] = 'my-access-key'
containerName = 'my-container-name'

if __name__ == "__main__":
    ContainerClient("https://" + storageCred['username'] + ".blob.core.windows.net/", containerName, credential=storageCred['password'])
    main()


'''
This is my (heavily) stripped down attempt to use azure.storage.blob.ContainerClient in a python3 runbook.
The code is functional locally in Ubuntu 18 w/ Python 3.8

Result:

Failed
C:\WPy64-3800\python-3.8.0.amd64\lib\site-packages\azure\storage\blob\_upload_chunking.py:403: SyntaxWarning: "is" with a literal. Did you mean "=="?  if n is 0 or self._buffer.closed:
C:\WPy64-3800\python-3.8.0.amd64\lib\site-packages\azure\storage\blob\baseblobservice.py:1009: SyntaxWarning: "is not" with a literal. Did you mean "!="?  if lease_duration is not -1 and \
C:\WPy64-3800\python-3.8.0.amd64\lib\site-packages\azure\storage\blob\baseblobservice.py:2660: SyntaxWarning: "is not" with a literal. Did you mean "!="?  if lease_duration is not -1 and \
C:\WPy64-3800\python-3.8.0.amd64\lib\site-packages\azure\storage\common\_connection.py:82: SyntaxWarning: "is" with a literal. Did you mean "=="?  self.protocol = self.protocol if parsed_url.scheme is '' else parsed_url.schemeTraceback (most recent call last):  File "C:\Temp\peilpacs.wgz\a27abd70-d0a9-46c8-9476-cdeb0d4f8d5c", line 1, in <module>    from azure.storage.blob import ContainerClient
ImportError: cannot import name 'ContainerClient' from 'azure.storage.blob' (C:\WPy64-3800\python-3.8.0.amd64\lib\site-packages\azure\storage\blob\__init__.py)
'''


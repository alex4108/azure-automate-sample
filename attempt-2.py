import azure.core
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

This sample includes the suggestion mentioned here: https://docs.microsoft.com/answers/answers/234760/view.html

Result:

Failed
Traceback (most recent call last):  File "C:\Temp\50yfoh15.idn\a27abd70-d0a9-46c8-9476-cdeb0d4f8d5c", line 1, in <module>    import azure.core
ModuleNotFoundError: No module named 'azure.core'
'''




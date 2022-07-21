from zipfile import ZipFile

zip = ZipFile('resources/hello.zip')
print(zip.namelist())
zip.extractall(path='resources/zip')
zip.close()

with ZipFile('resources/hello.zip') as myzip:
    myzip.extractall(path='resources/zip')



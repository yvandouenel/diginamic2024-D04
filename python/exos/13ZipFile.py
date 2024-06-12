from zipfile import ZipFile

source = ZipFile("./annexe/sources.zip", "r")
source.extractall("./extraits/")

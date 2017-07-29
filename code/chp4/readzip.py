import zipfile

z = zipfile.ZipFile("top-1m.csv.zip", "r")

for filename in z.namelist(  ):
    print 'File:', filename,
    bytes = z.read(filename)
    print 'has',len(bytes),'bytes'
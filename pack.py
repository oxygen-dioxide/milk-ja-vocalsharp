import sys
import py7zr

class Callback():#尚未使用，先写在这里，参考：https://github.com/miurahr/py7zr/issues/74
    def init():
        pass
    def report_start(self, processing_file_path, processing_bytes):
        print("report_start",processing_file_path, processing_bytes)

    def report_end(self, processing_file_path, wrote_bytes):
        print("report_end",processing_file_path, wrote_bytes)

def makearchive(filelist,outfilename):
    print(outfilename)
    with py7zr.SevenZipFile(outfilename,"w") as archive:
        for file in filelist:
            print("\t",file)
            archive.write(file)

version=sys.argv[1]
filelist=[
    "Milk JPN {}.srdx".format(version),
    "A3.vsdx",
    "A3.vsdxindex",
    "D4.vsdx",
    "D4.vsdxindex",
    "F3.vsdx",
    "F3.vsdxindex",
    "G4.vsdx",
    "G4.vsdxindex",
    "main.lsd",
    "license.md",
    "readme.md",
    "readme_zh.md",
]
outfilename=r"bin\Milk JPN {}.7z".format(version)
makearchive(filelist,outfilename)

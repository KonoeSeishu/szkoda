class FileUtils():
    @staticmethod
    def file_extension(filename):
        if "." in filename:
            return(filename.split(".")[1])
        else:
            return("")
        
print(FileUtils.file_extension("file.txt"))
print(FileUtils.file_extension("image.png"))
print(FileUtils.file_extension("no_extension"))
print(FileUtils.file_extension("file.py"))
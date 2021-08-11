from file_save_load import FileSaveLoad
from make_file_schema import MakeFileSchemaFromLootDir
from tags import Tags

a = FileSaveLoad()
tt = a.load()
ff = MakeFileSchemaFromLootDir('C:\\Users\\rlaxo\\Documents\\hitomi\\hitomi_downloaded', tt)
a.save(tt)
tt = a.load()
for i in tt.files:
    if 'C:\\Users\\rlaxo\\Documents\\hitomi\\hitomi_downloaded' == tt.files[i].parent:
        print(i)


'''\\\\RASPBERRYPI\\altairBackup\\test'''
'''C:\\Users\\rlaxo\\Documents\\hitomi\\hitomi_downloaded'''
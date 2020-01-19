# from PIL import Image
# from PIL.ExifTags import TAGS
#
# def get_meta(filename):
#   image = Image.open(filename)
#   image.verify()
#   return image._getexif()
#
# def get_labels(meta):
#     labeled = {}
#     for (key, val) in meta.items():
#         labeled[TAGS.get(key)] = val
#     return labeled
#
# meta = get_meta('100-days-in-space.jpg')
# labeled = get_labels(meta)
# print(labeled)

import dropbox
client = dropbox.Dropbox('Ci8e3duLF4AAAAAAAAAAFoK1urCLRrEKR-1CCbyHzBbPEOVXrh1Voj2Zl17jCH_5')
# print(client.users_get_current_account())
metadata = client.files_list_folder('/All onboard images').entries
print(metadata)

flist = []
# if metadata.has_more == True:
    # m1 = metadata.entries
    # cur = metadata.cursor
    # for i in m1:
    #     if isinstance(i, dropbox.files.FileMetadata):
    #         flist.append([i.name, i.size])
    #     # flist now has 2000 items
    # m2 = client.files_list_folder_continue(cur)
    # while m2.has_more == True:
    #     for i in m2.entries:
    #         if isinstance(i, dropbox.files.FileMetadata):
    #             flist.append([i.name, i.size])
    #     cur = m2.cursor
    #     m2 = client.files_list_folder_continue(cur).entries
    # else:
    #     m_final = client.files_list_folder_continue(cur)
    #     for i in m_final.entries:
    #         if isinstance(i, dropbox.files.FileMetadata):
    #             flist.append([i.name, i.size])

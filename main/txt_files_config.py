def remove_txt_from_filenames (list_filenames_with_txt_local):
    new_filenames = []
    for name in list_filenames_with_txt_local:
        first = name.split('.')[0]
        new_filenames += [first]
    return new_filenames

def add_txt_to_filenames (list_filenames_without_txt):
    filenames_txt = []
    for name in list_filenames_without_txt:
        first = name + '.txt'
        filenames_txt += [first]
    return filenames_txt
def string_to_list(contents, spliting=' - '):
    if not (spliting in contents):
        return None

    content_list = contents.split(spliting)

    list_content = []

    for content in content_list:
        list_content.append(content.strip())

    return list_content

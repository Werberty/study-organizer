def string_to_list(contents, spliting=' - '):
    if not (spliting in contents):
        return None

    content_list = contents.split(spliting)

    list_content = [content.strip() for content in content_list]

    return list_content

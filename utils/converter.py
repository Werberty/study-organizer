def string_to_list(contents, spliting=' - '):
    if spliting not in contents:
        return None

    content_list = contents.split(spliting)

    list_content = [content.strip() for content in content_list]

    return list_content

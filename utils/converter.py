def string_to_list(content_list, spliting=' - '):
    content_list = content_list.split(spliting)
    list_content = []
    for content in content_list:
        list_content.append(content.strip())

    return list_content

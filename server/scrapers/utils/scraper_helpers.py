from re import sub

def remove_html(string):
    return sub(r'<[^>]*>', "", string, 0).strip()
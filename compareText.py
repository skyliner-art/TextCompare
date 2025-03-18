import difflib

def compare_texts(standard_text:str,test_text:str):
    diff = difflib.context_diff(standard_text.splitlines(), test_text.splitlines())
    result= '\n'.join(diff)
    print(result)
    return result
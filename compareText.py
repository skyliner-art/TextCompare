import difflib
def compare_texts(standard_text:str,test_text:str):
    # standard_lines = len(standard_text.splitlines())
    # test_lines = len(test_text.splitlines())
    diff = difflib.context_diff(standard_text.splitlines(), test_text.splitlines())
    diff_list = list(diff)
    split_index = 0
    standard_lines = 1
    test_lines = 1
    is_standard = False
    is_test = False
    is_text = False
    for line in diff_list:
        if not is_text and line == f"***************\n":
            split_index+=1
            is_text = True
        elif not is_text:
            split_index+=1
        elif is_text and line[0:3] == "***":
            is_standard = True
        elif is_standard and line[0:3] == "---":
            is_test = True
            is_standard = False
        elif is_standard:
            standard_lines+=1
        elif is_test:
            test_lines+=1
        else:
            pass
    print('\n'.join(diff_list))
    print("---")
    print(split_index)
    print("---")
    standard_result = diff_list[split_index:split_index+standard_lines]
    test_result = diff_list[standard_lines+split_index:standard_lines+split_index+test_lines]
    standard_result = '\n'.join(standard_result)
    test_result = '\n'.join(test_result)
    print(standard_result)
    print("---")
    print(test_result)
    return (standard_result,test_result)
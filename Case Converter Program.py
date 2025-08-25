def case_convert(camel_or_pascal_case_text):
    snake_case_char_list = ['_' + char.lower() if char.isupper() else char for char in camel_or_pascal_case_text]
    snake_case_text = ''.join(snake_case_char_list).strip('_')
    
    return snake_case_text

def main():
    camel_or_pascal_case_text = input('Enter camel or pascal case text: ')
    snake_case_text = case_convert(camel_or_pascal_case_text)
    print(snake_case_text)

main()


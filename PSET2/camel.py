def main():
    camel_case = input("camelCase: ")
    snake_case(camel_case)

def snake_case(text):
    add_ele = ''
    for ele in text:
        if ele.isupper():
            add_ele = add_ele + '_' + ele.lower()
        else:
            add_ele += ele
    print(add_ele)

main()

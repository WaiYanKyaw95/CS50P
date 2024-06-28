input_text = input("Input: ")
output_text = input_text

for c in output_text:
    if c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u':
        output_text = output_text.replace(c, "")
print(f"Output: {output_text}")

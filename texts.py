text = "Hello World"
print(text)
print(type(text))
text2 = text.upper()
print(text)
print(text.upper())
print(text2)

print(len(text))

encoded_s = text.encode("utf-8")
print(encoded_s)
print(type(encoded_s))

decoded_s = encoded_s.decode("utf-8")
print(decoded_s)
print(type(decoded_s))

name = "Natalia"
print("Name: " + name)
text_format = f"My name is {name} and I like Python"
print(text_format)

multiline = """Hello
       World
       
       Natalia"""
print(multiline)



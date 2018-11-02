from system import handler
text = input('what program to test load?:')
print(len(text))
if len(text) == 0:
    text = 'example_ENT_SPC_SPC_SPC2'
print('loading:')
print(text)
handler.load(text)
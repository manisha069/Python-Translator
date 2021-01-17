from translate import Translator


lang=input("Enter a language you want to translate to ")
t=Translator(to_lang=lang)

text=input("Enter text you want to translate ")
ans=t.translate(text)

print(ans)
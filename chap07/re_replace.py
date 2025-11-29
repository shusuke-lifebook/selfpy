import re

msg = "サポートサイトはhttps://www.wing.msn.to/です。"
ptn = re.compile(r"http(s)?://([\w-]+\.)+[\w-]+(/[\w./?%&=_]*)?", re.IGNORECASE)
print(ptn.sub(r'<a href="\g<0>">\g<0></a>', msg))

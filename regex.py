import re

print(re.sub(r"\b([0-9]+)\b", (lambda m: str(int(m.group(1)) * 2)), "Dnes je 52 stupnu a 45 dni"))
print(re.sub(r"\b([0-9]+)\b", (lambda m: "X{0}X".format(m.group(1))), "Dnes je 52 stupnu a 45 dni"))


colors = {"b": 34, "h": 31, "a": 32, "div": 33, "p": 35}
re_pattern = re.compile(r"<(?P<start>[^>]+)\b[^>]*>((?:.(?!<\/(?P=start)>))*.)<\/(?P=start)>")
text = "Dnes je <h>To jsou veci: <a href='t'> ale ale!</a> - nebo: <p class='x'>52 a jeste <div>test</div> ha ha ha <div>zase neco</div></p> stupnu a <a>45 a bold: <b>BOLD</b></a></h> dni"
while re_pattern.search(text) is not None:
    text = re_pattern.sub(
        (lambda m: "\033[{0}m{1}\033[0m".format(
            colors.get(m.group(1), 37), m.group(2))), text)

print(text)

re_pattern = re.compile(r"(\w+)([, .;:-]+)(\w+)([, .;:-]+)(\w+)")
print(re_pattern.sub(
    lambda m : "{0}{1}{2}{3}{4}".format(
        m.group(1).upper(),
        "...{0}...".format(m.group(2)),
        m.group(3).lower(),
        "...{0}...".format(m.group(4)),
        m.group(5)), "hola ahoj---diVOKO---velke hej"))
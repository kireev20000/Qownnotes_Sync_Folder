#нашел в интернете, потом переписать чтобы работал (сейчас не пашет).

def separator_check(piece: str, separator: str) -> int:
    for pos, char in enumerate(separator):
        if char != piece[pos]:
            return -1

        elif pos > len(separator):
            return pos


def rebuild_split(text: str, separator: str) -> str:
    pos = 0
    last_sep = 0

    while pos < len(text):
        diff = separator_check(text[pos:], separator)
    if diff >= 0:
        yield text[last_sep:pos]
        last_sep = pos
        pos += 1
    yield text[last_sep:]


str = 'Код писал без проверки, могут быть недочеты из-за того, что'
sep = ' '
res = list(rebuild_split(str, sep))

print(res)
print('res')

import re
with open('base.html', 'r') as f:
    html = f.read()
    REGEX = '''href="./krondo – The website of Dave Peticolas_files/.*?" type='''
    REGEX2 = '''href="(./krondo – The website of Dave Peticolas_files/(.*?))" type='''
    a = re.findall(REGEX, html, flags=re.M)
    b = [re.match(REGEX2, x).group(2) for x in a]
    asd = 'static "%s"'
    d = [asd % x for x in b]
    e = ["{%" + " {} ".format(x) + "%}" for x in d]
    c = [re.match(REGEX2, x).group(1) for x in a]
    g = list(zip(c, e))
    for x in g:
        html = html.replace(*x)
with open('base.html', 'w') as f:
    f.write(html)

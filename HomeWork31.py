import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    while '<' in html and '>' in html:
        start = html.find('<')
        end = html.find('>', start)
        html = html[:start] + html[end + 1:]

    with  codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(html)

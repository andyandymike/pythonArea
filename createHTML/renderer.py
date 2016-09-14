from handlers import *

class HTMLRenderer(Handler):

    def start_html(self):
        print('<html><head><title>Andy</title></head><body>')

    def end_html(self):
        print('</body></html>')

    def start_p(self):
        print('<p style="color: #444;">')

    def end_p(self):
        print('</p>')

    def start_h1(self):
        print('<h1 style="color: #1ABC9C;">')

    def end_h1(self):
        print('</h1>')

    def start_h2(self):
        print('<h2 style="color: #68BE5D;">')

    def end_h2(self):
        print('</h2>')

    def start_ul(self):
        print('<ul style="color: #363736;">')

    def end_ul(self):
        print('</ul>')

    def start_li(self):
        print('<li>')

    def end_li(self):
        print('</li>')

    def feed(self, data):
        print(data)

    def sub_em(self, match):
        print('<em>%s</em>' % match.group(1))

    def sub_url(self, match):
        return '<a target="_blank" style="text-decoration: none;color: #BC1A4B;" href="%s">%s</a>' % (match.group(1), match.group(1))

    def sub_mail(self, match):
        return '<a style="text-decoration: none;color: #BC1A4B;" href="mailto:%s">%s</a>' % (match.group(1), match.group(1))

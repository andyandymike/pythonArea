from handlers import *
from util import *
from rules import *
from renderer import *
import re

class Parser:

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('html')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('html')

class BasicTextParser(Parser):

    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ulRule())
        self.addRule(liRule())
        self.addRule(h1Rule())
        self.addRule(h2Rule())
        self.addRule(pRule())


        self.addFilter(r'\*(.+?)\*', 'em')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

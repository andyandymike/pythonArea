class Rule:

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

class h2Rule(Rule):
    type = 'h2'

    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class h1Rule(Rule):
    type = 'h1'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return h2Rule.condition(self, block)

class liRule(Rule):
    type = 'li'

    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True

class ulRule(Rule):
    type = 'ul'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and liRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not liRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False

class pRule(Rule):
    type = 'p'

    def condition(self, block):
        return True


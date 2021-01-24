
print ("learning class with a cardgame")
print ("------------------------------")


class Card(object):
    def __init__(self, suit, val, provider):
        self.suit = suit
        self.value = val
        self.provider = provider

    def show(self):
        # print "{} of {} in {}".format(self.value, self.suit, self.provider)
        pass

    def report(self):
        # print "{} of {}".format(self.value, self.suit)
        # if self.provider == '1001':
        #     print "{} of {}".format(self.value, self.suit)
        if self.provider == '1001':
            print self.suit, self.value

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        with open("/home/ernie/cdr/class/cdr2.log",'r') as f:
            line_file1 = f.readlines()
            for line in line_file1:
            #     #print line
                list = []
                list = " ".join(line.split())
                st = list.split(',')
                # print st
                # print st[0], st[1]
                try:
                    if len(st) == 19:
                        if st[11] != 'success_esme':
                            self.cards.append(Card(st[11], st[8], st[3]))
                except:
                    pass

                # print st
                # self.cards.append(Card(st[1], st[0]))
                

    def show(self):
        for c in self.cards:
            c.show()
            c.report()

class Player(object):
    pass



card = Card("Clubs", 7, 'tata')
# card.report()


deck = Deck()
deck.show()
# deck.report()
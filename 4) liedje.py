#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

# import


class Liedje:

    def __init__(self, lijst):
        self.lijst = lijst

    def zingen(self):
        lijn1 = self.lijst[0] + " " + self.lijst[1] + " " + self.lijst[2] + " " + self.lijst[3]
        lijn2 = self.lijst[0] + " " + self.lijst[1] + " " + self.lijst[4] + " " + self.lijst[5]
        print(lijn1 + "\n" + lijn1 + "\n" + lijn2 + "\n" + lijn1)


verjaardagslied = Liedje(["Happy", "birthday", "to", "you", "dear", "Jakob"])
verjaardagslied.zingen()
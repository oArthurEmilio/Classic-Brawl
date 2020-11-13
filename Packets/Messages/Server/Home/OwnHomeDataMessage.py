from Utils.Writer import Writer
from Database.DataBase import DataBase


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        DataBase.loadAccount(self)

        self.writeVint(2020007)
        self.writeVint(75158) # timestamp

        self.writeVint(self.player.trophies) # trophies
        self.writeVint(self.player.trophies) # max reached trophies

        self.writeVint(122)
        self.writeVint(99)  # reward for trophy road

        self.writeVint(1262469)  # starting level (exp points)

        self.writeVint(28) # csv id
        self.writeVint(self.player.profileIcon)  # player icon ID

        self.writeVint(43) # csv id
        self.writeVint(self.player.namecolor)  # player name color ID

        self.writeVint(9)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(7)
        self.writeVint(8)
        self.writeVint(9)
        self.writeVint(10)

        self.writeVint(3)
        self.writeVint(29)

        self.writeVint(14)
        self.writeVint(29)

        self.writeVint(self.player.skinID) # skinID
        self.writeVint(29)

        self.writeVint(0)


        self.writeVint(self.player.skins_count) # unlocked skins array

        for i in range(0, self.player.skins_count):
            self.writeScId(29, i)


        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeBoolean(False)  # "token limit reached message" if true

        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)

        self.writeVint(248791) # season ends timer

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(200)
        self.writeVint(200)

        self.writeVint(5)
        self.writeVint(93)
        self.writeVint(206)
        self.writeVint(456)
        self.writeVint(1001)
        self.writeVint(2264)
        self.writeVint(8)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)

        for i in range(0,4):
            self.writeVint(0)

        self.writeVint(100) # available tokens
        self.writeVint(99999) # time till bonus tokens (seconds)

        self.writeBoolean(True)  # tickets enabled
        self.writeVint(0)
        self.writeVint(self.player.tickets)  # tickets number
        self.writeVint(-21)
        self.writeVint(16)

        self.writeVint(self.player.brawlerID) # selected brawler

        self.writeString("RO")  # location
        self.writeString("26.165") # supported content creator

        self.writeVint(-133169153)

        for i in range(0,4):
            self.writeVint(0)

        self.writeVint(2019053)
        self.writeVint(100)

        self.writeVint(10)
        self.writeVint(30)  # shop big box price

        self.writeVint(3)
        self.writeVint(80)  # shop mega box price

        self.writeVint(10)
        self.writeVint(50)  # shop token doubler price
        self.writeVint(1000)  # shop token doubler amount

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)


        self.writeVint(6)
        self.writeVint(0)
        self.writeVint(30)
        self.writeVint(80)
        self.writeVint(170)
        self.writeVint(350)
        self.writeVint(0)
        self.writeVint(15)

        for i in range(0,10):
            self.writeVint(i)

        for i in range(20, 25):
            self.writeVint(i)

        totalSlots = 10
        mapsList = [7, 32, 17, 0,  24, 202, 97, 167, 174]
        self.writeVint(totalSlots -1 )  # map slots count

        for i in range(1, totalSlots):

            self.writeVint(-133000102)  # map slot starts here
            self.writeVint(i)
            self.writeVint(0)
            self.writeVint(75992) # timer
            self.writeVint(10)
            self.writeVint(15)

            self.writeVint(int(mapsList[i - 1]))  # game mode slot map id

            self.writeVint(2) # [3 = nothing, 2 = star token, 1 = new event]
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)  # map slot ends here

        # shop
        self.writeVint(0)

        self.writeVint(8)
        for i in [20, 35, 75, 140, 290, 480, 800, 1250]:
            self.writeVint(i)

        self.writeVint(8)
        for i in [1, 2, 3, 4, 5, 10, 15, 20]:
            self.writeVint(i)

        self.writeVint(3)
        for i in [10, 30, 80]: # Tickets price
            self.writeVint(i)

        self.writeVint(3)
        for i in [6, 20, 60]: # Tickets amount
            self.writeVint(i)

        self.writeVint(4)
        for i in [20, 50, 140, 280]: # Gold price
            self.writeVint(i)

        self.writeVint(4)
        for i in [150, 400, 1200, 2600]: # Gold amount
            self.writeVint(i)


        self.writeVint(2)

        self.writeVint(999) # max tokens
        self.writeVint(20) # plus tokens

        self.writeVint(8640)
        self.writeVint(10)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(50)
        self.writeVint(604800)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(14)
        self.writeVint(0)
        self.writeVint(3193)

        self.writeVint(-8)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)  # High Id
        self.writeVint(1)  # Low Id

        for i in range(0, 4):
            self.writeVint(0)

        if self.player.name is None:

            self.writeString("Guest")  # player name
            self.writeVint(0)
            DataBase.createAccount(self)  # create new account

        else:
            self.writeString(self.player.name)  # player name
            self.writeVint(1)

        self.writeVint(1207959551)

        self.writeVint(39) # array


        i = 0

        for x in range(0,19):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i += 4

        i = 95

        for x in range(0,8):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i += 5

        i = 177

        for x in range(0,2):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i += 5

        i = 188

        for x in range(0,4):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i += 6

        i = 218

        for x in range(0,2):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i += 18


        resources = {
            'brawlbox': {'id': 1, 'amount': self.player.brawlBoxes},
            'gold': {'id': 8, 'amount': self.player.gold},
            'bigbox': {'id': 9, 'amount': self.player.bigBoxes},
            'starpoints': {'id': 10, 'amount': self.player.starPoints}
        }

        for resource in resources:
            self.writeVint(5) # csv id
            self.writeVint(resources[resource]['id']) # resource id
            self.writeVint(resources[resource]['amount']) # resource amount


        # brawlers trophies
        self.writeVint(35)  # brawlers count

        for i in range(0, 33):
            self.writeScId(16, i)
            self.writeVint(self.player.brawler_trophies)
        # exceptions
        self.writeScId(16, 34)
        self.writeVint(self.player.brawler_trophies)  # jacky trophies
        self.writeScId(16, 37)
        self.writeVint(self.player.brawler_trophies)  # sprout trophies


        # brawlers trophies for rank
        self.writeVint(35)  # brawlers count

        for i in range(0,33):
            self.writeScId(16, i)
            self.writeVint(self.player.brawler_trophies_for_rank)
        # exceptions
        self.writeScId(16, 34)
        self.writeVint(self.player.brawler_trophies_for_rank)  # jacky trophies for rank
        self.writeScId(16, 37)
        self.writeVint(self.player.brawler_trophies_for_rank)  # sprout trophies for rank


        self.writeVint(0)


       # upgrade poitns
        self.writeVint(35)  # brawlers count

        for i in range(0,33):
            self.writeScId(16, i)
            self.writeVint(self.player.brawler_upgrade_points)  # Upgrade poitns
        # exceptions
        self.writeScId(16, 34)
        self.writeVint(self.player.brawler_upgrade_points)
        self.writeScId(16, 37)
        self.writeVint(self.player.brawler_upgrade_points)


        # brawlers power level
        self.writeVint(35)  # brawlers count

        for i in range(0,33):
            self.writeScId(16, i)
            self.writeVint(self.player.brawler_power_level)
        # exceptions
        self.writeScId(16, 34)
        self.writeVint(self.player.brawler_power_level)  # jacky power level
        self.writeScId(16, 37)
        self.writeVint(self.player.brawler_power_level)  # sprout power level


        self.writeVint(119)  # gadgets and star powers


        for i in range(76, 95):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)

        self.writeVint(23)
        self.writeVint(99)
        self.writeVint(1)

        self.writeVint(23)
        self.writeVint(104)
        self.writeVint(1)

        i = 109

        for x in range(0, 5):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i+=5

        for i in range(134, 172):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)


        self.writeVint(23)
        self.writeVint(172)
        self.writeVint(1)


        for i in range(174, 176):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)


        self.writeVint(23)
        self.writeVint(181)
        self.writeVint(1)
        self.writeVint(23)

        self.writeVint(186)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(187)
        self.writeVint(1)

        self.writeVint(23)
        self.writeVint(192)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(193)
        self.writeVint(1)
        self.writeVint(23)

        self.writeVint(198)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(199)
        self.writeVint(1)
        self.writeVint(23)

        self.writeVint(204)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(205)
        self.writeVint(1)
        self.writeVint(23)

        self.writeVint(210)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(211)
        self.writeVint(1)

        self.writeVint(23)
        self.writeVint(216)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(217)
        self.writeVint(1)


        for i in range(222, 224):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)

        for i in range(240, 277):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)


        # "new" brawler tag
        self.writeVint(35)  # brawlers count

        for i in range(0, 33):
            self.writeScId(16, i)
            self.writeVint(2)  # mr p  "new" tag
        # exceptions
        self.writeScId(16, 34)
        self.writeVint(2)  # jacky "new" tag
        self.writeScId(16, 37)
        self.writeVint(2) # sprout "new" tag


        self.writeVint(self.player.gems) # gems
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(100)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(0)




class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there\n"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets pull of shells\n"])

fish = Song(["Lonely is as lonely does.",
             "Lonely is an eyesore.",
             "The feeling describes itself.\n"])

love_cats = ["We move like cagey tigers",
             "We couldn't get closer than this.\n"]

# Module style
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
fish.sing_me_a_song()

# Pass variable to Class
cure = Song(love_cats)
cure.sing_me_a_song()

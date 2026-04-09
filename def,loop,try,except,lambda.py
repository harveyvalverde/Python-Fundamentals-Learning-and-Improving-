def videogames(num):
        games = []
        for game in range(num):
            gamename = input("Enter one videogame name: ")
            while True:
                try:
                    punctuation = int(input("Enter a punctuation for that game from 0 to 10: "))
                    if 0 <= punctuation <= 10:
                        gamedata = (gamename,punctuation)
                        games.append(gamedata)
                        break
                    else:
                         print("I said from 0 to 10!")
                except ValueError:
                    print("Please enter a number")
        games.sort(key=lambda x:x[1])
        gamelow = games[0][0]
        gamescorelow = games[0][1]
        print(f"The game {gamelow} has a punctuation of {gamescorelow}, is the lowest score!")

videogames(3)

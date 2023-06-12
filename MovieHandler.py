import random

class MovieHandler:
    
    def __init__(self, movieListFile, watchedMovieListFile):
        
        self.movieListFile = movieListFile
        
        self.watchedMovieListFile = watchedMovieListFile
        
        self.movieList = []
        
        self.watchedMovieList = []


    def chooseRandomMovie(self):
        
        while(True):
            randomNum = random.randint(0,len(self.movieList))
            print("++++++ Choosing a random film ++++++\n")
            print(f"Random film :: {randomNum}) {self.movieList[randomNum]}\n")
            
            while(True):

                print(f'Confirming you want to watch {randomNum}) {self.movieList[randomNum]}\n')
                yn = input("y/n :: ")

                if(yn == 'y'):
                    
                    self.addMovieToWatchedTextFile(self.movieList[randomNum])
                    self.removeMovieFromListTextFile(self.movieList[randomNum])
                    self.addMovieToWatchedList(self.movieList[randomNum])
                    self.removeMovieFromList(self.movieList[randomNum])
                    
                    
                    break
                
                elif(yn == 'n'):
                    print("Exiting, no film chosen\n")
                    break

                else:
                    continue

            return None
    
    
    def chooseMovieToWatch(self):
        self.displayMovieList()
        print("\n")
        
        while(True):


            movieToWatch = int(input(f"Please enter number between 0 and {len(self.movieList)-1} :: "))
            
            if movieToWatch >= 0 and movieToWatch < len(self.movieList):
                print(f'Confirming you want to watch {movieToWatch}) {self.movieList[movieToWatch]}\n')
                yn = input("y/n :: ")

                if(yn == 'y'):
                    
                    self.addMovieToWatchedTextFile(self.movieList[movieToWatch])
                    self.removeMovieFromListTextFile(self.movieList[movieToWatch])
                    self.addMovieToWatchedList(self.movieList[movieToWatch])
                    self.removeMovieFromList(self.movieList[movieToWatch])
                    
                    
                    break
                elif(yn == 'n'):
                    print("Exiting, no film chosen\n")
                    break

                else:
                    continue

            else:
                print("!!!!!!!!!!!! Invalid movie!!!!!!!!!!!!\n")


    def addMovieToList(self, movieName):
        self.movieList.append(movieName)
        
        return None
    
    def addMovieToWatchedList(self,movieName):
        self.watchedMovieList.append(movieName)
        return None

    def removeMovieFromList(self,movieName):
        self.movieList.remove(movieName)
        return None
    

    def removeMovieFromListTextFile(self, movieName):
        
        with open(self.movieListFile, 'r') as file:
            lines = file.readlines()
        file.close()
        
        with open(self.movieListFile, 'w') as file:
            for line in lines:
                if line.strip("\n") != movieName.strip("\n"):
                    file.write(line)
        file.close()
        return None
    
    def addMovieToWatchedTextFile(self,movieName):
        
        file = open(self.watchedMovieListFile, 'a')
        file.write(f"{movieName}\n")
        file.close()
        
        self.createMovieList()

        print(f"{movieName} added to file, movie list is updated")

        return None
    
    def addMovieToMovieListTextFile(self, movieName):
        file = open(self.movieListFile, 'a')
        file.write(f"{movieName}\n")
        file.close()
        self.createMovieList()

    def createMovieList(self):
        file = open(self.movieListFile, 'r')
        
        lines = file.readlines()

        file.close()
        self.movieList.clear()
        for movieName in lines:
            self.movieList.append(movieName.replace('\n',''))
        return None
    
    def createWatchedMovieList(self):
        
        file = open(self.watchedMovieListFile, 'r')

        lines = file.readlines()
        file.close()
        for movieName in lines:
            self.watchedMovieList.append(movieName)

        return None
    
    def displayWatchedMovies(self):
        print("--------Watched Movies--------\n")
        for i in range(0, len(self.watchedMovieList)):
            print(f'{i}) {self.watchedMovieList[i]}\n')
        return None
    
    def displayMovieList(self):
        print("--------Unwatched Movies--------\n")
        for i in range(0,len(self.movieList)):
            print(f'{i}) {self.movieList[i]}\n')
        return None
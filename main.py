import MovieHandler
import Gui


def main():
    
    #initial setup for MovieHandler
    movieHandler = MovieHandler.MovieHandler('movieList.txt', 'watchedMovies.txt')
    movieHandler.createMovieList()
    movieHandler.createWatchedMovieList()


    
    while(True):
        
        choice = int(input("Welcome to MovieChooser, please choose what you would like to do\n1 :: Choose a random movie\n2 :: Choose a movie manualy\n3 :: Add film to movie list\n4 :: View movie list\n5 :: View Watched Movie List\n6 :: Exit\n     Choice :: "))
        
        if(choice == 1):
            movieHandler.chooseRandomMovie()
        
        elif(choice == 2):
            movieHandler.chooseMovieToWatch()
        
        elif(choice == 3):
            movieHandler.addMovieToMovieListTextFile(input("\nEnter the film to be added :: "))
        
        elif(choice == 4):
            movieHandler.displayMovieList()
        
        elif(choice == 5):
            movieHandler.displayWatchedMovies()
        
        elif(choice == 6):
            print("\nEnjoy the film!\n >>>>>> Exiting <<<<<<")
            break
        
    return None


if __name__ == '__main__':
    main()
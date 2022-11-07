# The below code is importing the spacy and numpy libraries.
import spacy
import numpy as np

def suggest_movie(description):
    """
    1. Load the spacy model
    2. Create a dictionary of movie titles and descriptions
    3. Create a list of similarity scores
    4. Return the movie title with the highest similarity score
    
    :param description: The description of the movie you want to watch
    :return: The movie title
    """
    

    # Loading the spacy model.
    nlp = spacy.load("en_core_web_md")

    # Creating an empty dictionary.
    dictionary ={}


    # The above code is opening the movies.txt file and reading it. Then it is splitting the file by
    # the new line character and then popping the last item off the list.
    my_movie = open("./movies.txt").read()
    my_movie = my_movie.split("\n")
    my_movie.pop()

   # This is creating a dictionary with the movie title as the key and the description as the value.
    for movie in my_movie:
        dictionary[movie.split(":")[0]] = movie.split(":")[1]
        
    # Creating an empty list.
    list_1 = []

    # Comparing the similarity of the description with the values of the dictionary.
    for i in dictionary.values():
    
        model_description = nlp(description)
        similarity = nlp(i).similarity(model_description)
        print(i + "--" + str(similarity))
        
    
   # Creating an empty list and then appending the movie title to the list.
    movie_title = []
    for name in movie_title:
        movie_title.append(name)

    
    return movie_title[list_1.index(max(list_1))] 

 
if __name__ == '__main__':
    
     description = '''
    Will he save
    their world or destroy it? When the Hulk becomes too dangerous for the
    Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
    planet where the Hulk can live in peace. Unfortunately, Hulk land on the
    planet Sakaar where he is sold into slavery and trained as a gladiator.
    '''
# This is calling the function and printing the movie title.
moive_seen = suggest_movie(description)
print(moive_seen)

    
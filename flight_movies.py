from collections import Counter

def movies_to_watch(flight, movies):

    movie_counts = Counter(movies)

    for first in movies:
        second = flight - first
        if second == first:
            return movie_counts[first] > 1
        if second in movie_counts:
            return True

    return False

flight = 120
movies = [40, 60, 100, 10, 50]

print movies_to_watch(flight, movies)

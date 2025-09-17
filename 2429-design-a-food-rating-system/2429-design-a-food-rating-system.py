import heapq
class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}   #food -> cuisine
        self.food_to_rating = {}    #food -> rating
        self.cuisine_heaps = {}     #cuisine -> heap [(-rating, food)]

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.cuisine_heaps:
                self.cuisine_heaps[c] = []
            heapq.heappush(self.cuisine_heaps[c], (-r, f))

    def changeRating(self, food, newRating):
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_heaps[cuisine]
        # Usuwamy nieaktualne elementy z wierzchu
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)  # stary wpis – wyrzucamy
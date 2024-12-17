import networkx as nx  # for graphs
import matplotlib.pyplot as plt  # visualization

class ResourceAllocationGraph:
  def __init__(self, readers, booksread):
    # Initialize an empty graph
    self.graph = nx.DiGraph()
    self.readers = readers
    self.booksread = booksread

  def add_edge(self, reader, book, weight=None):
    # Add an edge between a reader and a book
    self.graph.add_edge(reader, book, weight=weight)

  def visualize(self):
    # Set up the figure size
    plt.figure(figsize=(16, 12))

    # Manually set the positions of the nodes
    position = {}
    # Place readers on the left
    for i, reader in enumerate(self.readers):
        position[reader] = (-1, i)
    # Place books on the right
    for j, book in enumerate(self.booksread):
        position[book] = (2, j * (len(self.readers) / len(self.booksread)))

    # Draw the nodes
    nx.draw(
      self.graph,
      pos=position,
      node_size=3000,
      node_color='skyblue',
      font_size=12,
      font_weight='bold',
      with_labels=True
    )

    # Draw edges with weights
    edge_labels = nx.get_edge_attributes(self.graph, 'weight')
    nx.draw_networkx_edges(self.graph, position, width=2, alpha=0.5, edge_color='gray')
    nx.draw_networkx_edge_labels(self.graph, position, edge_labels=edge_labels, font_size=10)

    plt.title('What Books Have They Read?')
    plt.show()

  def get_similar_users(self, target_reader):
    similarities = []
    for reader in self.readers:
      if reader == target_reader:
          continue
      common_books = set(self.graph.successors(reader)) & set(self.graph.successors(target_reader))
      if common_books:
          similarity = sum(abs(self.graph[reader][book]['weight'] - self.graph[target_reader][book]['weight'])
                            for book in common_books) / len(common_books)
          similarities.append((similarity, reader))
    similarities.sort()  # Sort by similarity
    return [reader for _, reader in similarities]

  def recommend_book(self, reader):
    similar_readers = self.get_similar_users(reader)
    books_read_by_reader = set(self.graph.successors(reader))

    for similar_reader in similar_readers:
      for book in self.graph.successors(similar_reader):
          weight = self.graph[similar_reader][book].get('weight', 0)  # Use 0 if weight not set
          if book not in books_read_by_reader and weight >= 4:
            return book
    return None  # No recommendation found

  def get_recommendation(self, reader):

    recommendations_made = [] #store all recs
    relevant_recommendations = [] #store relevant rec

    if reader not in self.readers:
      print("User not found. Please check the name.")
      return

    while True:
      recommended_book = self.recommend_book(reader)

      if recommended_book is None:
        print("Sorry, we have no recommendations for you right now.")
        precision = len(relevant_recommendations) / len(recommendations_made) if recommendations_made else 1.0
        print(f"Precision for {reader}: {precision:.2f}")
        return

      recommendations_made.append(recommended_book)

      print(f"We recommend you read '{recommended_book}'")
      feedback = input("Did you like this recommendation? (y/n): ")


      if feedback.lower() == 'y':
        relevant_recommendations.append(recommended_book)
        print("Happy reading!")
        precision = len(relevant_recommendations) / len(recommendations_made) if recommendations_made else 1.0
        print(f"Precision for {reader}: {precision:.2f}")
        return
      else:
        print("We'll try another recommendation.")
        # Mark the book as disliked to avoid recommending it again
        self.graph.add_edge(reader, recommended_book, weight=1)

readers = ['Cat', 'Amei', 'Jihyun', 'Shannon', 'James', 'Rick', 'J', 'Annie',
           'Jess', 'Jessica', 'Matthew', 'Miranda', 'Whitney']

Booksread = ['Twilight', 'Divine Rivals', 'Fated Blades', 'Scorpion', 'Icebreaker', 'Before I Left Go',
             'A Song to Drown Rivers', 'On the Way to the Wedding', 'Big Summer', 'Muscles & Monsters',
             'The Stone and the Star', 'An Offer From a Gentleman', 'The Viscount Who Loved Me',
             'Harry Potter and the Sorcerers Stone', 'Harry Potter and the Chamber of Secrets',
             'Harry Potter and the Prisoner of Azkaban', 'Harry Potter and the Goblet of Fire', 'Fourth Wing',
             'A Witch\'s Guide to Magical Innkeeping', 'Darker by Four', 'Powerless', 'The Sword of Kaigen',
             'The Jasad Heir', 'All This & More', 'Son of the Drowned Empire', 'Charlie and the Chocolate Factory',
             'Charlie and the Great Glass Elevator', 'Kindred', 'Parable of the Sower', 'Leviathan Wakes',
             'Battle Royale', 'Uglies', 'Brave New World', 'Slaughterhouse-Five', 'City of Bones']

rag = ResourceAllocationGraph(readers, Booksread)

# Adding some edges with weights as user ratings (1-5 scale)

#twilight
rag.add_edge('Cat', 'Twilight', weight = 3)
rag.add_edge('Jihyun', 'Twilight', weight = 4)
rag.add_edge('Shannon', 'Twilight', weight = 5)
rag.add_edge('James', 'Twilight', weight = 1)
rag.add_edge('Jessica', 'Twilight', weight = 5)
rag.add_edge('Miranda', 'Twilight', weight = 5)

#HPSS
rag.add_edge('Cat', 'Harry Potter and the Sorcerers Stone', weight = 3)
rag.add_edge('Jihyun', 'Harry Potter and the Sorcerers Stone', weight = 5)
rag.add_edge('Amei', 'Harry Potter and the Sorcerers Stone', weight = 4)
rag.add_edge('Shannon', 'Harry Potter and the Sorcerers Stone', weight = 5)
rag.add_edge('James', 'Harry Potter and the Sorcerers Stone', weight = 4)
rag.add_edge('Matthew', 'Harry Potter and the Sorcerers Stone', weight = 5)

#Kindred
rag.add_edge('Cat', 'Kindred', weight = 5)
rag.add_edge('James', 'Kindred', weight = 5)
rag.add_edge('Rick', 'Kindred', weight = 5)

#Parable of the sower
rag.add_edge('Cat', 'Parable of the Sower', weight = 5)
rag.add_edge('James', 'Parable of the Sower', weight = 5)
rag.add_edge('Rick', 'Parable of the Sower', weight = 5)

#Divine Rivals
rag.add_edge('Cat', 'Divine Rivals', weight = 4)
rag.add_edge('Amei', 'Divine Rivals', weight = 5)
rag.add_edge('Jess', 'Divine Rivals', weight = 5)

#Leviathan Wakes
rag.add_edge('Amei', 'Leviathan Wakes', weight = 4)
rag.add_edge('Rick', 'Leviathan Wakes', weight = 5)
rag.add_edge('J', 'Leviathan Wakes', weight = 4)

#Harry Potter and the Chamber of Secrets
rag.add_edge('Jihyun', 'Harry Potter and the Chamber of Secrets', weight = 5)

#Harry Potter and the Chamber of Secrets
rag.add_edge('Jihyun', 'Harry Potter and the Prisoner of Azkaban', weight = 4)

#Harry Potter and the Goblet of Fire
rag.add_edge('Jihyun', 'Harry Potter and the Goblet of Fire', weight = 5)

#Fourth Wing
rag.add_edge('Amei', 'Fourth Wing', weight = 5)
rag.add_edge('Annie', 'Fourth Wing', weight = 4)
rag.add_edge('Matthew', 'Fourth Wing', weight = 5)

#Battle Royale
rag.add_edge('Shannon', 'Battle Royale', weight = 5)

#Uglies
rag.add_edge('Shannon', 'Uglies', weight = 5)
rag.add_edge('Rick', 'Uglies', weight = 4)

#Brave New World
rag.add_edge('James', 'Brave New World', weight = 5)
rag.add_edge('Rick', 'Brave New World', weight = 3)

#Slaughterhouse-Five
rag.add_edge('Rick', 'Slaughterhouse-Five', weight = 4)

#City of Bones
rag.add_edge('Rick', 'City of Bones', weight = 4)

#Fated Blades
rag.add_edge('Jessica', 'Fated Blades', weight = 4)

#A Witch's Guide to Magical Innkeeping
rag.add_edge('Jessica', 'A Witch\'s Guide to Magical Innkeeping', weight = 4)

#Scorpion
rag.add_edge('Annie', 'Scorpion', weight = 4)

#Icebreaker
rag.add_edge('Annie', 'Icebreaker', weight = 2)

#Darker by Four
rag.add_edge('Jess', 'Darker by Four', weight = 4)

#Powerless
rag.add_edge('Jess', 'Powerless', weight = 1)
rag.add_edge('Miranda', 'Powerless', weight = 3)

#The Sword of Kaigen
rag.add_edge('Jess', 'The Sword of Kaigen', weight = 4)
rag.add_edge('Matthew', 'The Sword of Kaigen', weight = 4)

#The Jasad Heir
rag.add_edge('Jess', 'The Jasad Heir', weight = 3)

#Before I Left Go
rag.add_edge('Jess', 'Before I Left Go', weight = 1)

#A Song to Drown Rivers
rag.add_edge('Jessica', 'A Song to Drown Rivers', weight = 4)

#All This & More
rag.add_edge('Jessica', 'All This & More', weight = 4)

#Son of the Drowned Empire
rag.add_edge('Jessica', 'Son of the Drowned Empire', weight = 4)

#Charlie and the Chocolate Factory
rag.add_edge('Matthew', 'Charlie and the Chocolate Factory', weight = 5)
rag.add_edge('Whitney', 'Charlie and the Chocolate Factory', weight = 4)

#Charlie and the Great Glass Elevator
rag.add_edge('Matthew', 'Charlie and the Great Glass Elevator', weight = 2)

#On the Way to the Wedding
rag.add_edge('Miranda', 'On the Way to the Wedding', weight = 4)

#Big Summer
rag.add_edge('Miranda', 'Big Summer', weight = 5)

#Muscles & Monsters
rag.add_edge('Whitney', 'Muscles & Monsters', weight = 4)

#The Stone and the Star
rag.add_edge('Whitney', 'The Stone and the Star', weight = 3)

#An Offer From a Gentleman
rag.add_edge('Whitney', 'An Offer From a Gentleman', weight = 5)

#The Viscount Who Loved Me
rag.add_edge('Whitney', 'The Viscount Who Loved Me', weight = 4)

rag.visualize()

####

user_name = input("Enter your name to get book recommendations: ")
rag.get_recommendation(user_name)
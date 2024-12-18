import networkx as nx  # for graphs
import matplotlib.pyplot as plt  # visualization

# Class defined in Amei's classroom
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
# Book Recommendation

The goal of Book Club is to provide efficient, tailored book recommendations by analyzing users' reading histories to identify similarities and differences. 

This project was created with two classmates Amei & Jihyun in October & November 2024. Though originally created in google colab, I moved the program to github using pycharm.


**Data Collection:**
User book data from Goodreads was compiled into the “CS291 Library User Data” spreadsheet, including usernames, reading histories, genres, and ratings. Data was prioritized for users with at least one shared book to enhance the recommendation algorithm.


[CS291 Library User Data - Sheet1.pdf](https://github.com/user-attachments/files/18186247/CS291.Library.User.Data.-.Sheet1.pdf)


**Program Creation:**
The program was developed orgiginally in Google Colab using Python, NetworkX for graph modeling, and Matplotlib for visualization. Reader history data from the spreadsheet was imported into a bipartite graph based on code from Introduction to Operating Systems. ChatGPT and Gemini refined the recommendation methods within the existing ResourceAllocationGraph class.


**Overview of Book Club:**
Book Club identifies user similarities based on book ratings in their reading history. Higher similarity is assigned when two users rate a book similarly (e.g., both give 5 stars) compared to dissimilar ratings or no shared history.

The system recommends the highest-similarity book not already in the user's history. If the user dislikes the recommendation, a low-weight edge is added to reduce the likelihood of recommending that book again. Recommendations continue until either:
1. The user likes a book, or
2. No more qualifying books remain.

**Example 1**


<img width="739" alt="Screen Shot 2024-12-18 at 10 36 06 AM" src="https://github.com/user-attachments/assets/4ccbf6fe-550d-4c52-8168-fc6fd40f30b3" />

**Example 2**


<img width="790" alt="Screen Shot 2024-12-18 at 10 37 19 AM" src="https://github.com/user-attachments/assets/5d50bba3-cd71-4843-be90-8517625c1414" />


**References**
www.goodreads.com 

**Bipartite Graph Visualization**


<img width="816" alt="Screen Shot 2024-12-18 at 10 38 49 AM" src="https://github.com/user-attachments/assets/0a13a392-1b48-42e5-95ba-9dec578d18cd" />

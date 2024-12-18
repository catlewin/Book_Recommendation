from Library_Data import rag

user_name = input("Enter your name to get book recommendations: ")
rag.get_recommendation(user_name)
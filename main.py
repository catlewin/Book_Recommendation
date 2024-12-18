from Library_Data import rag

def main():
    rag.visualize()
    user_name = input("Enter your name to get book recommendations: ")
    rag.get_recommendation(user_name)

if __name__ == "__main__":
    main()
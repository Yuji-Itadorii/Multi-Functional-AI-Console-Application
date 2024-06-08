# main.py
import asyncio
import helper as hf

async def main():
    check = True
    while check:
        print("Select a task:")
        print("1. Summarize text")
        print("2. Translate text")
        print("3. Expand text")
        print("4. Fact-check text")
        print("5. Exit")

        print("\n")
        
        choice = input("Enter your choice: ")

        try: 
            if choice == "1":
                number_of_paragraphs = int(input("Enter the number of paragraphs to summarize: "))
                list_of_paragraphs = []

                for i in range(number_of_paragraphs):
                    text = input(f"Enter the paragraph number {i+1} :")
                    print("\n")
                    list_of_paragraphs.append(text)
                
                print("\n Generating Response . . . \n")

                summaerized_paragraphs = []

                for i in range(len(list_of_paragraphs)):
                    response = await hf.summarize_text(list_of_paragraphs[i])
                    print(f"Paragraph {i+1}:", response)
                    print("\n")
                    summaerized_paragraphs.append(response)

                print("\n")

                whole_text = ""
                for para in summaerized_paragraphs:
                    whole_text += para + "\n"

                hf.save_to_file(whole_text, "summarized_text.txt")



            elif choice == "2":
                text = input("Enter the text to translate: ")
                target_language = input("Enter the target language code (e.g., es for Spanish): ")
                print("\n Generating Response . . . \n")
                response = await hf.translate_text(text, target_language)
                print("Translation:", response)
                print("\n")
                hf.save_to_file(response , "text_translation.txt")
            elif choice == "3":
                text = input("Enter the text to expand: ")
                print("\n Generating Response . . . \n")
                response = await hf.expand_text(text)
                print("Expanded text:", response)
                print("\n")
                hf.save_to_file(response , "expand_text.txt")
            elif choice == "4":
                text = input("Enter the statement to fact-check: ")
                print("\n Generating Response . . . \n")
                response = await hf.fact_check_text(text)
                print("Fact-check result:", response)
                print("\n")
                hf.save_to_file(response , "fact_check_result.txt")
            elif choice == "5":
                print("Thank You!! Exiting the program. . .")
                check = False
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred. Please try again!  Error : {e}")

        print("\n")

if __name__ == "__main__":
    asyncio.run(main())

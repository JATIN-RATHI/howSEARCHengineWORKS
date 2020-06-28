def counter(string1, string2):
    #here words1 = search and words2 = doc . Both are split word by word and compared word by word using nested for loop and counts the matches found.
    words1 = string1.split(" ")
    words2 = string2.split(" ")
    count = 0
    for word1 in words1:
        for word2 in words2:
            #the words in both search and doc are converted into lower case to compare
            if word1.lower() == word2.lower():
                count += 1
    return count

if __name__ == '__main__':
    print("\nWelcome to the program\tcreated by \x1b[6;30;42m'Jatin Rathi'\x1b[0m")
    doc = ["Python language", "Examples of Python work", "Python is best", "Work in python console in pycharm", "C is also a language", "C console", "Java docs", "javascript for websites"]
    search = input("\nEnter what you want to search : ")
    counts = [counter(search, word) for word in doc]
    #zip binds counts and doc in a list form, this found list is sorted in order of counts ...decending order - reverse
    found = [find for find in sorted(zip(counts, doc), reverse=True)]
    count = len(found)
    print(f"\t{count} results found")
    sno = 1
    for count, item in found:
        print(f"{sno} : \"{item}\"    - matches {count} word ")
        sno += 1

import urllib

def read_file():
    open_file = open(r"C:\Users\Ajay Sharma\Desktop\deckofcards.txt")
    read_file = open_file.read()
    print(read_file)
    open_file.close()
    check_profanity(read_file)
    

def check_profanity(text_to_search):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_search)
    profanity_read = connection.read()
    connection.close()
    if "true" in profanity_read:
        print("Profanity Alert!")
    elif "false" in profanity_read:
        print("Profanity not found!")
    
read_file()
 

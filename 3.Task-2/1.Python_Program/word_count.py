def wordy(init_text):
    # All the character of the text is converted into lower case letter
    lower_text=init_text.lower()

    # All the punctuation and special symbol is being removed from the text
    # Except space and alphabetic character
    filter_text = []
    for char in lower_text:
        if (char.isalpha() or char==' '):
            filter_text.append(char)
    join_text=''.join(filter_text)
    #print(join_text)

    # Each word of the text is splited and stored in a list
    split_words=join_text.split()
    #print(split_words)

    # Every word occurance is counted and stored in a dictionary
    word_counts = {}
    for word in split_words:
        if word in word_counts:
            word_counts[word]+=1
        else:
            word_counts[word]=1


    # The word are sorted and printed in alphabetic order
    sort_keys=sorted(word_counts.keys())
    #print(sort_keys)

    organized_dict={}
    for key in sort_keys:
        organized_dict[key]=word_counts[key]
    #print(organized_dict)

    print("****Word Frequency****")
    for word,count in organized_dict.items():
        print(f"{word} : {count}")

if __name__ == '__main__':

    # Through this input can be taken several times
    # but when enter 0 the process will be finished
    while(1):
        init_text = input("Enter Sentence: ")
        if init_text=='0':
            break
        else:
            wordy(init_text)
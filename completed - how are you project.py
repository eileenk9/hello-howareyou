name = "Noah"
good_words = ['good', 'great', 'wonderful', 'awesome']
reply_words = ['what?', 'what', 'what!']
bad_words = ['bad', 'okay', 'terrible']
print("HOWDY!")
var = input ("How are you feeling today?").replace(" ","")
if var in good_words:
    print('I am so glad to hear that! I hope it continues to your weekend', name)
else:
    print("Sorry to hear that. I think you're great.")
var = input ("But as a bonus, guess what?!").replace(" ","")
if var in reply_words:
    print ("It's Friday!")
else:
    print ("Type 'what'")
    var = input ("But as a bonus, guess what?").replace (" ","")
    if var in reply_words:
            print ("It's Friday! " +name)
    else:
        print: ("Bye", name)

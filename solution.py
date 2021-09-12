### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question, answer=None):
    if question == "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?":
       answer = "mTLS"
    elif question == "Are encoding and encryption the same? - Yes/No":
       answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
       answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
       answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
       answer = "Yes"
    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking":
       answer = "Yes"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
       answer = "Yes"
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
       answer = "7"
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
       answer = "Yes"
    else:
        return (answer)


# Complete all the questions.


#if __name__ == "__main__":
   # use this space to debug and verify that the program works
   #debug_question = "Are encoding and encryption the same? - Yes/No"
   #print(welcome_assignment_answers(debug_question))


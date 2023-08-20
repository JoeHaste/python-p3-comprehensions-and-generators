#!/usr/bin/env python3

def return_evens(num_list):
    even_no = [num for num in num_list if num % 2 == 0]
    return even_no
return_evens([10, 21, 4, 45, 66, 93])

def make_exclamation(sentence_list):
    new_sent = [x + "!" for x in sentence_list]
    return new_sent
make_exclamation(["Hello", "I'm doing great", "Python is fun"])

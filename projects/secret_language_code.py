import re
import random

def get_random_number(start, end):
    rand = random.randint(start, end)
    return rand

st1 = 'he is a good bo.y. but harry is 54 344 also a good boy.'
st2 = ''
st3 = ''
new_word_List = []
    # print(word)
# print(st2.strip("."))

def encode(st1):
    new_word_List = []
    word_list = st1.split(' ')
    # word_list = re.findall(r'[a-zA-Z0-9]+', st1)
    for i in word_list:
        st2 = ''
        st3 = ''
        # print(i)
        # symbol_index = i.find('.')
        # print(symbol_index)
        dot = '.' if i[-1] == '.' else ''
        word = i.strip('.')
        if len(word) == 1:
            st2 += word + dot
        elif len(word) == 2:
            st2 += word[1] + word[0] + dot
        elif len(word) > 2:
            if word.isnumeric():
                st2 += str(get_random_number(0, 9)) + str(get_random_number(0, 9)) + word + str(get_random_number(0, 9)) + str(get_random_number(0, 9)) + dot
            else:
                first_letter = word[0]
                st3 = word[1:] + first_letter
                st2 += chr(get_random_number(65, 90)) + chr(get_random_number(97, 122)) + chr(get_random_number(65, 90) )  + st3 + chr(get_random_number(97, 122)) + chr(get_random_number(97, 122)) + chr(get_random_number(65, 90 ) ) + dot
        new_word_List.append(st2)
    st4 = " ".join(new_word_List)
    return st4



def decode(st1):
    decode_List = []
    new_word_List = []
    new_word_List = st1.split(' ')
    # word_list = re.findall(r'[a-zA-Z0-9]+', st1)
    for i in new_word_List:
        st2 = ''
        st3 = ''
        # print(i)
        # symbol_index = i.find('.')
        # print(symbol_index)
        dot = '.' if i[-1] == '.' else ''
        word = i.strip('.')
        if len(word) == 1:
            st2 += word + dot
        elif len(word) == 2:
            st2 += word[1] + word[0] + dot
        elif len(word) > 2:
            if word.isnumeric():
                st2 +=  word[2:-2] + dot
            else:
                last_letter = word[len(word)-4]
                s = word[3:-4]
                st2 = last_letter + s + dot
        decode_List.append(st2)
    st4 = " ".join(decode_List)
    return st4


encode_st = encode(st1)
print(encode_st)# Output

decode_st = decode(encode_st)
print(decode_st)# Output



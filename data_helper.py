import pandas as pd 
import os 

def get_data(poet_list = ['taufik ismail', 'chairil anwar', 'ws rendra', 'sapardi djoko damono']): 

    poetry_data = []

    poet = poet_list[0]
    poetry_list = sorted(os.listdir('./dataset/' + poet))

    for poet in poet_list: 
        poetry_list = sorted(os.listdir('./dataset/' + poet))
        print('~~~~~~~' + poet)
        i = 1
        for poetry_title in poetry_list:
            print(str(i) + '/' + str(len(poetry_list)) + " :" + poetry_title)
            file = open('./dataset/' + poet + '/' + poetry_title , 'r', encoding= 'cp850')
            poetry_data.append(file.readlines())
            i += 1

    poetry_data = [''.join(poetry) for poetry in poetry_data]

    poetry_data = [poetry.lower() for poetry in poetry_data]

    text = ' '.join(sorted(poetry_data))

    # remove unused character
    for s_char in ['%', '*', '+', '[', ']', '^', '"', '~', 'à', 'æ', 'ô', 'ö', 'ù', 'ú', 'û', '╔']:
        text = text.replace(s_char, ' ')
    
    # remove white space
    text = text.strip()
    pattern = re.compile(r'\s{2,}')
    text = re.sub(pattern, ' ', text)
    
    print('corpus length:', len(text))

    chars = sorted(list(set(text)))
    print('total chars:', len(chars))
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))


    
    return text, chars, char_indices, indices_char


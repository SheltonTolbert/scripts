import random
import time

def print_graph(graph):
    
    for key in graph:
        if key:
            print(key)

def add_to_graph(key, last_character, graph):

    if last_character in graph: 
        if key in graph[last_character]:
            graph[last_character][key] += 1
        else: 
            graph[last_character][key] = 1
        graph[last_character]['total'] += 1
    else: 
        graph[last_character] = {'total': 0}

    return graph

def build_graph():
    graph = {}
    last_character = False
    file =  open('./words.txt', 'r')

    for word in file:
        
        for char in word:
            if last_character: 
                if ('\n' == char):
                    graph = add_to_graph(' ', last_character, graph)
                else: 
                    graph = add_to_graph(char, last_character, graph)
            last_character = ' ' if char == '\n' else char

    return graph
        
def calculate_most_likely(character, graph):
    char_map = graph[character]
    total = char_map['total']

    percentages = []
    percentages_map = {}

    for map in char_map.items():
        if map[0] == 'total': 
            continue
        else:
            percentage = map[1] / total
            percentages.append(percentage)
            percentages_map[percentage] = map[0]

    percentages.sort()
    for p in percentages:
        print(percentages_map[p], p)


def main():
    file = open('./trash.txt', 'w')
    num_letters = 9

    for i in range(2000000): 
        if num_letters >= random.randrange(12):
            file.write(' ')
            num_letters = 0
        else:
            file.write(chr(random.randrange(97, 122, 1)))
            num_letters +=  1
    print('done')

    file.close()

t = time.perf_counter()
#main()
calculate_most_likely('a', build_graph())
print(time.perf_counter() - t)

#-*- coding : utf-8 -*-
import sys
import random

### Const
file_dir = "/home/takashi/dev/banabo/scripts/python/comments/"

### Sub Function
def get_comment_list(file):
    comment_list = []
    for line in open(file, 'r'):
        comment_list.append(line)
    return comment_list


### Main Function
if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2:
        print "Usage : %s comment_list" % argv[0]
        quit()
    file_name = argv[1]
    file = file_dir + file_name
    comment_list = get_comment_list(file)
    
    print random.choice(comment_list)

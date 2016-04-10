# -*- coding : utf-8 -*-
import sys
import shutil
import os

#### Const
python_dir = "/home/takashi/dev/banabo/scripts/python/"
memo_dir = python_dir + "memo/"

### Sub Functions
def get_memo_file(user):
    memo_file = memo_dir + user
    return memo_file

def show_comments(user,memo_file):
    count = 0
    for line in open(memo_file, 'r'):
        print "[%s] : %s" % (str(count), line),
        count = count + 1

def backup_file(memo_file):
    back_file = memo_file + ".bak"
    shutil.copyfile(memo_file, back_file)

def revert_file(memo_file):
    back_file = memo_file + ".bak"
    back2_file = memo_file + ".bak2"
    
    # swap main and backup file
    shutil.copyfile(memo_file, back2_file)
    shutil.copyfile(back_file, memo_file)
    shutil.copyfile(back2_file, back_file)
    os.remove(back2_file)
    
def add_comments(comment_list,memo_file):
    backup_file(memo_file)

    comment=""
    fa = open(memo_file, 'a')
    for item in comment_list:
        comment="%s%s " % (comment,item)
    fa.write("%s\n" % comment)

def del_comments(index_list,memo_file):
    backup_file(memo_file)
    index_list.reverse()
    comment_list = []
    for line in open(memo_file, 'r'):
        comment_list.append(line)
    
    for index in index_list:
        comment_list.pop(int(index))
    fw = open(memo_file, 'w')
    for comment in comment_list:
        fw.write("%s" % comment)

def show_usage():
    print "Usage"
    print "%s help : show usage" % argv[0]
    print "%s user_name add [comment] : add comments" % argv[0]
    print "%s user_name del [index *] : delete comments by indicate indexes" % argv[0]
    print "%s user_name show : show commens" % argv[0]
    print "%s user_name revert : revert memo file from backkup" % argv[0]

### Main Function
if __name__ == '__main__':
    # Validate argvs
    argv = sys.argv
    argc = len(argv)

    if argc < 3:
        show_usage()
        quit()

    # Setting
    user = argv[1]
    option = argv[2]
    memo_file = get_memo_file(user)

    if not os.path.exists(memo_file):
        open(memo_file, 'w')

    # Processing 
    if option == "help":
        show_usage()

    elif option == "show":
        show_comments(user, memo_file)

    elif option == "add":
        comment_list = argv[3:argc]
        add_comments(comment_list, memo_file)
        show_comments(user, memo_file)
        
    elif option == "del":
        index_list = argv[3:argc]
        del_comments(index_list, memo_file)
        show_comments(user, memo_file)

    elif option == "revert":
        revert_file(memo_file)
        show_comments(user, memo_file)

    else:
       show_usage()

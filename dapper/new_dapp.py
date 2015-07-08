import os
import json
import dapper.utils as u

def help():
    print '''\
Usage: dapper new-dapp <option>

Options:
  <name>           The name of the dapp folder to set up.
  help           Prints this message.
'''
################################################################################
#        1         2         3         4         5         6         7         8
def main(option):
    if option == 'help':
        return help()
    try:
        u.find_project_root()
    except AssertionError:
        os.mkdir(name)
        os.mkdir(os.path.join(name, '.dapper'))
        json.dump({}, open(os.path.join(name, '.dapper', 'build.json'), 'w'))
        open(os.path.join(name, '.dapper', 'README'), 'w').write('''\
This folder is used to hold important files for dapper operation.
DO NOT MODIY ANYTHING IN HERE!
''')
    else:
        print 'You can\'t make a dapper project in a dapper project!'

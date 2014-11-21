#!/usr/bin/env python
import sys, logging, getopt
sys.path.append('..')
from pygame_client import PygameClient
from config import *

#
# Main controlling program.  You should not change anything here.
#

def usage():
    print "usage: %s [-l|--localhost] [-s|--server host] [-L|--logging level] [-n|--name name] [-t|--title title] [-h|--help]" % (sys.argv[0])
    print "-l|--localhost   : use localhost for the server"
    print "-s|--server host : identify the host of the server"
    print "-L|--logging info|debug|warning|error: logging level"
    print "-n|--name name   : display name in game"
    print "-t|--title title : game name to display in title bar"
    print "-h|--help        : show this message and exit"
    return

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:lL:n:t:", ["help", "server=", "localhost", "logging=", "name=", "title="])
    except getopt.GetoptError as e:
        print str(e)
        usage()
        sys.exit(1)

    show_help = False
    server = "rookie.cs.dixie.edu"
    name = DEFAULT_TEAM_NAME
    title = DEFAULT_GAME_TITLE
    logging_level = "error"
    for o, a in opts:
        if o in ("-h", "--help"):
            show_help = True
        elif o in ("-s", "--server"):
            server = a
        elif o in ("-l", "--localhost"):
            server = "127.0.0.1"
        elif o in ("-L", "--logging"):
            logging_level = a
        elif o in ("-n", "--name"):
            name = a
        elif o in ("-t", "--title"):
            title = a
        else:
            print "Unexpected option: %s" % (o)
            usage()
            sys.exit(1)
    if show_help:
        usage()
        sys.exit(1)

    if logging_level == "info":
        logging.basicConfig(level=logging.INFO)
    elif logging_level == "debug":
        logging.basicConfig(level=logging.DEBUG)
    elif logging_level == "warning":
        logging.basicConfig(level=logging.WARNING)
    elif logging_level == "error":
        logging.basicConfig(level=logging.ERROR)
    else:
        logging.basicConfig(level=logging.ERROR)
    
    g = PygameClient(WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND, name, title, server)
    g.main_loop()
    return

if __name__ == "__main__":
    main()

#!/usr/bin/env python2
# coding=utf-8
"""
research/simplewebserver2
-

Active8 (12-05-15)
author: erik@a8.nl
license: GNU-GPL2
"""
import os
import SimpleHTTPServer
import SocketServer
import random
import webbrowser

from threading import Timer


def startbrowser(*port):
    """
    startbrowser
    """
    webbrowser.open("http://0.0.0.0:" + str(port[0]))


def main():
    """
    main
    """
    port = random.randint(7000, 8000)
    t = Timer(1.5, startbrowser, [port])
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", port    ), Handler)
    print "\033[93m" + "serving " + os.getcwd() + "\non port", str(port) + "\033[0m"
    print "\033[90m"

    t.start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt as e:
        print "ctrl-c exit"
    finally:
        print "\033[0m"


if __name__ == "__main__":
    main()

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Sean Kirmani <sean@kirmani.io>
#
# Distributed under terms of the MIT license.
"""TODO(Sean Kirmani): DO NOT SUBMIT without one-line documentation for test

TODO(Sean Kirmani): DO NOT SUBMIT without a detailed description of test.
"""
import argparse
import os
import re
import sys
import time
import traceback

def main():
  global args
  # TODO(Sean Kirmani): Do something more interesting here...
  print IsUrl('http://www.google.com/')
  print IsUrl('Hello world!')

def IsUrl(string):
  regex = re.compile(
      r'^(?:http|ftp)s?://' # http:// or https://
      r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
      r'localhost|' #localhost...
      r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
      r'(?::\d+)?' # optional port
      r'(?:/?|[/?]\S+)$', re.IGNORECASE)
  return regex.match(string) != None

if __name__ == '__main__':
  try:
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--verbose', action='store_true', default=False, \
        help='verbose output')
    parser.add_argument('-d','--debug', action='store_true', default=False, \
        help='debug output')
    args = parser.parse_args()
    # if len(args) < 1:
    #   parser.error('missing argument')
    if args.verbose: print(time.asctime())
    main()
    if args.verbose: print(time.asctime())
    if args.verbose: print('TOTAL TIME IN MINUTES:')
    if args.verbose: print(time.time() - start_time) / 60.0
    sys.exit(0)
  except KeyboardInterrupt, e: # Ctrl-C
    raise e
  except SystemExit, e: # sys.exit()
    raise e
  except Exception, e:
    print('ERROR, UNEXPECTED EXCEPTION')
    print(str(e))
    traceback.print_exc()
    os._exit(1)

"""
Spur, a cool tool for converting Scratch games to Spyral games!
"""

__version__ = '0.1'
__license__ = 'MIT'
__author__ = 'Austin Cory Bart'

from converter import convert_to_spyral
import sys
from optparse import OptionParser

def format_columns(message, data):
    first_width = max([len(x[0]) for x in data])
    second_width = max([len(x[1]) for x in data])
    total_width = first_width + second_width + 8

    # calculate a format string for the output lines
    format_str = "%%-%ds        %%-%ds" % (first_width, second_width)

    print message
    print "=" * max(total_width, len(message))
    for x in data:
        print format_str % x

if len(sys.argv) > 1:
    convert_to_spyral(sys.argv[1])
else:
    print "Error: Need at least one Scratch file"
    #parser = OptionParser()
    #parser.add_option("-c", "--fullscreen", action="store_true", dest="fullscreen", default=False, help="Run in fullscreen mode. Default is windowed mode.")
    #(options, args) = parser.parse_args()
    
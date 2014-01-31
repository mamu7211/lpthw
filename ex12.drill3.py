import os
import sys
print "os.linesep = %r" % os.linesep
print "os.reduce -> reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) = %r" % reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
print "sys.path[0] = %r" %sys.path[0]
print "sys.floatinfo = %r" %sys.floatinfo
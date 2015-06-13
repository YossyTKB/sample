#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      yoshitaka
#
# Created:     27/05/2014
# Copyright:   (c) yoshitaka 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import platform

def main():
    print 'hello'
    print 'Version      :', platform.python_version()
    print 'Version tuple:', platform.python_version_tuple()
    print 'Compiler     :', platform.python_compiler()
    print 'Build        :', platform.python_build()

if __name__ == '__main__':
    main()
    print 'test'








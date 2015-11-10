#!/usr/bin/python
import getopt, sys
 
def main():

    in_filename = 'fin'
    out_filename = 'fout'

    print('argv  : %s' %(sys.argv[1:]))

    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'i:o:', ['input=', 'output='])
    except getopt.GetoptError:
        sys.exit()

    print('options  : %s' %(options))

    for opt, arg in options:
        if opt in ('-i', '--input'):
            in_filename = arg
        elif opt in ('-o', '--output'):
            out_filename = arg

    print('remainder : %s' %(remainder))

    print('input file = %s' %(in_filename))
    print('output file = %s' %(out_filename))

    return 0

if __name__ == "__main__":
    sys.exit(main())

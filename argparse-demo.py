import argparse
import sys

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Script to learn basic argparse')
    parser.add_argument('-c', '--command',
                        help='Command to run',
                        required='True',
                        default='ping')
    
    parser.add_argument('-p', '--placeholder',
                        help='place holder of the command',
                        required='True',
                        default='10.10.30.38'
                        )
    
    parser.add_argument('-a', '--arguments',
                        help='extra arguments'
                       )

    results = parser.parse_args(args)
        
    return (results.command,
            results.placeholder,
            results.arguments)
 
 
if __name__ == '__main__':
    check_arg(sys.argv[1:])

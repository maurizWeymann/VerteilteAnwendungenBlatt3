# Stand: 13.10.21
# Beispiel für Kommandozeilenparameter

import sys, argparse

# aufruf python.exe test.py --number1=34 --number2 4

def main(argv):
    #a = b = 0
    print(f'Parameter: {argv=}')
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.1')
    parser.add_argument('--number1', '-n1', dest='a', type=int, help='Zahl 1')
    parser.add_argument('--number2', '-n2', dest='b', type=int, help='Zahl 2')
    args = parser.parse_args()

    print(f'Das Ergebnis ist: {args.a + args.b}')


if __name__ == '__main__':
    main(sys.argv)
    sys.exit(1)
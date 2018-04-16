from token_list import token_list
from token_parser import parse


def main():
    t = 'test.json'
    ts = token_list(t)
    o = parse(ts)
    for k, v in o.items():
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()

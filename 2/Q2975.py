import re

def main():
    r = re.compile('(-?\d+) (W|D) (\d+)')

    while True:
        m = r.search(input())

        if m.group() == '0 W 0': break

        start, action, amount = int(m.group(1)), m.group(2), int(m.group(3))

        if action == 'W':
            after = start - amount

            print(after if after >= -200 else 'Not allowed')
        else:
            print(start + amount)

if __name__ == '__main__':
    main()

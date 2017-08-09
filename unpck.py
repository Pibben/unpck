import sys


def main():
    filename = sys.argv[1]

    with open(filename, "rb") as f:
        f.read(4)

        f.readline()

        entries = []

        while True:
            line = f.readline().decode('utf-8').strip()
            if line == '':
                break

            entries.append(line.split('?'))

        print(entries)

if __name__ == '__main__':
    main()

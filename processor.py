import os

def write_integers(filename):
    with open(filename, 'w') as f:
        for i in range(101):
            f.write(f'{i}\n')

def get_integers(filename):
    if not os.path.exists(filename):
        raise IOError('File does not exist')
    if not os.path.isfile(filename):
        raise IOError('Given filename is not a file')
    with open(filename, 'r') as f:
        if f.read(2) != '0\n':
            raise Exception('File is malformed')
    with open(filename, 'r') as f:
        integers = []
        for i in range(50):
            integers.append(int(f.readline().strip()))
    return integers

if __name__ == '__main__':
    write_integers('file')
    print(*get_integers('file'), sep='\n')

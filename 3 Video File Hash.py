__author__ = 'Siyao'


def read_in_chunks(filename, chunk_size=1024):
    blocks = []
    with open(filename, 'rb') as f:
        data = None
        while data != '':
            data = f.read(chunk_size)
            if data != '':
                blocks.insert(0, data)
    return blocks


if __name__ == '__main__':
    file_blocks = read_in_chunks('test.mp4')

    from Crypto.Hash import SHA256
    previous_sha = ''
    for i in file_blocks:
        # Get sha of current block augmented with previous sha
        sha = SHA256.new()
        sha.update(i + previous_sha)
        previous_sha = sha.digest()
        hex_sha = sha.hexdigest()
    print hex_sha

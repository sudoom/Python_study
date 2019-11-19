import hashlib

# -------------TO-DO------------
# we have 5 files
# read each file
# calculate hashsum for each file
# create manifest file
# write to manifest ["file name": "hashsum"]
# write classes
# write "check" read manifest
# do global manifest


class files:
    manifest = '/home/worker/Python_study/IT-Academy/Lesson 14/Manifest.txt'

    def __init__(self, path):
        self.path = path

    def hashsum(self):
        with open(self.path, 'r') as fn:
            b = hashlib.md5(str(fn.read()).encode())
            z = b.hexdigest()
        with open(manifest, 'w') as wr:
            wr.write(self.path+" : "+z+"\n")

    def read(self):
        blank_list = []

        manifest = '/home/worker/Python_study/IT-Academy/Lesson 14/Manifest.txt'
        blank_list.append(self.path)
        with open(manifest, 'w') as rd:
            rd.write(str(blank_list))



x1 = files('/home/worker/Python_study/IT-Academy/Lesson 14/hash_files/Hash_file_1.txt')
q1 = x1.read()
x2 = files('/home/worker/Python_study/IT-Academy/Lesson 14/hash_files/Hash_file_2.txt')
x3 = files('/home/worker/Python_study/IT-Academy/Lesson 14/hash_files/Hash_file_3.txt')
q2 = x2.read()
q3 = x3.read()
#x4 = files('/home/worker/Python_study/IT-Academy/Lesson 14/hash_files/Hash_file_4.txt')
#x5 = files('/home/worker/Python_study/IT-Academy/Lesson 14/hash_files/Hash_file_5.txt')
#o1 = x1.hashsum()
#o2 = x2.hashsum()
#o3 = x3.hashsum()
#o4 = x4.hashsum()
#o5 = x5.hashsum()



'''

path = '/home/worker/Python_study/IT-Academy/Lesson 14/hash_files/Hash_file_1.txt'
with open(path,'r') as fn:
    a = hashlib.md5(str(fn.read()).encode())
    z = a.hexdigest()
with open('/home/worker/Python_study/IT-Academy/Lesson 14/hash_files/Hash_file_1.txt', 'w') as mn:
    mn.write(path+' : '+z)

  1 import argparse
  2
  3
  4 if __name__ == '__main__':
  5         parser = argparse.ArgumentParser()
  6         parser.add_argument('--calc', nargs='+', dest='files')
  7
  8         pars = parser.parse_args()
  9         print(pars.files)
   '''


# m = hashlib.md5()
# z = "lksdlfksldf"
# x = hashlib.md5()
# m.update(z.encode())
# x.update(" the spammish repetition".encode())
# print(m.digest())
# print(x.digest())


# import hashlib
# def chunks(filename, chunksize):
#     f = open(filename, mode='rb')
#     buf = "Let's go"
#     while len(buf):
#        buf = f.read(chunksize)
#        yield buf
# def md5sum(filename):
#     d = hashlib.md5()
#     for buf in chunks(filename, 128):
#         d.update(buf)
#         return d.hexdigest()

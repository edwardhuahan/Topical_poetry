import os
import struct

topic = sys.argv[1]
data = ''
path = os.path.join(os.getcwd(), '../example/4line/')

while True:
    data = str(struct.unpack('I', os.urandom(4))[0])
    if not os.path.isdir(os.path.join(path, str(data))):
        break;

os.mkdir(os.path.join(path,data))

random_dir = os.path.join('../',path, data)
rhyme_dir = os.getcwd()
rhyme_cmd = 'sudo sh '+rhyme_dir+'/run-different-line-numbers.sh '
rhyme_cmd += topic + ' '
rhyme_cmd += random_dir+'/poem.fsa '
rhyme_cmd += random_dir+'/source.txt '
rhyme_cmd += random_dir+'/rhyme.txt '
rhyme_cmd += random_dir+'/encourage.txt '
rhyme_cmd += '4'

os.system(rhyme_cmd)


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
current_dir = os.getcwd()
rhyme_cmd = 'sudo sh '+rhyme_dir+'/run-different-line-numbers.sh '
rhyme_cmd += topic + ' '
rhyme_cmd += random_dir+'/poem.fsa '
rhyme_cmd += random_dir+'/source.txt '
rhyme_cmd += random_dir+'/rhyme.txt '
rhyme_cmd += random_dir+'/encourage.txt '
rhyme_cmd += '4'

os.system(rhyme_cmd)

root_dir = os.path.join(current_dir, '../')
poem_cmd = 'python '
poem_cmd += os.path.join(root_dir, '/py/run_standalone.py ')
poem_cmd += os.path.join(root_dir, '/models/lyrics.tl.nn ')
poem_cmd += os.path.join(random_dir, '/source.txt ')
poem_cmd += os.path.join(random_dir, '/poem.fsa ')
poem_cmd += os.path.join(random_dir, '/encourage.txt ')
poem_cmd += os.path.join(random_dir, '/output.txt ')
poem_cmd += '50 1 '
poem_cmd += random_dir

print(poem_cmd)

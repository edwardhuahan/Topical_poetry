import os
import struct
import sys
import shutil
sys.path.insert(1, os.getcwd()+'/../py/')
import run_standalone

def generate(topic):
    topic = topic
    data = ''
    path = os.path.join(os.getcwd(), '../example/4line/')

    while True:
        data = str(struct.unpack('I', os.urandom(4))[0])
        if not os.path.isdir(os.path.join(path, str(data))):
            break;

    os.mkdir(os.path.join(path,data))

    random_dir = os.path.join('../',path, data)
    current_dir = os.getcwd()
    rhyme_cmd = 'sudo sh '+current_dir+'/run-different-line-numbers.sh '
    rhyme_cmd += topic + ' '
    rhyme_cmd += random_dir+'/poem.fsa '
    rhyme_cmd += random_dir+'/source.txt '
    rhyme_cmd += random_dir+'/rhyme.txt '
    rhyme_cmd += random_dir+'/encourage.txt '
    rhyme_cmd += '4'

    os.system(rhyme_cmd)
    open(random_dir+'/output.txt', 'a').close()

    root_dir = os.getcwd() + '/..'
    poem_cmd = 'python '
    poem_cmd += root_dir+'/py/run_standalone.py '
    poem_cmd += root_dir+'/models/lyrics.tl.nn '
    poem_cmd += random_dir+'/source.txt '
    poem_cmd += random_dir+'/poem.fsa '
    poem_cmd += random_dir+'/encourage.txt '
    poem_cmd += random_dir+'/output.txt '
    poem_cmd += '50 1 '
    poem_cmd += random_dir

    os.system(poem_cmd)

    result = run_standalone.process_results(random_dir+'/output.txt')
    # Deletes folder
    shutil.rmtree(random_dir)
    return result

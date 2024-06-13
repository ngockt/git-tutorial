import json
import os
from collections import defaultdict


def make_md_py_files(qname, FOLDER):
    mdtext = open('src/data/qa_md_template.txt').read()
    pytext = open('src/data/answer_py_code_template.txt').read()
    folder = os.path.join(FOLDER, f'qa{qname}')
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f'a{qname}.py')
    with open(path, 'w') as f:
        f.write(pytext.format(q=qname))

    path = os.path.join(folder, f'qa{qname}.md')
    
    with open(path, 'w') as f:
        f.write(mdtext.format(q=qname, q_ref=''))


def rename_question_images(qnum, FOLDER):
        qname = os.path.join(FOLDER, f'qa{qnum}/image.png')
        if os.path.exists(qname):
            newname = qname.replace('image.png', f'q{qnum}.png')
            os.rename(qname, newname)


def rename_solution_images(qnum, FOLDER):
        qname = os.path.join(FOLDER, f'qa{qnum}/image.png')
        if os.path.exists(qname):
            newname = qname.replace('image.png', f's{qnum}.png')
            os.rename(qname, newname)


if __name__ == '__main__':
    psinfo = json.load(open('static/documents/1-maths/2-calculus/2-problem-sets/mit18.01/ps-info.json'))
    for ps in psinfo['new']:
        FOLDER = ps['folder']
        ps_number = ps['ps_index']
        for sindex in ps['sub_index']:
            c, n = sindex.split('-')
            for i in range(1, int(n) + 1):
                qname = f'{ps_number}{c}-{i}'
                # make_md_py_files(qname, FOLDER)
                rename_question_images(qname, FOLDER)

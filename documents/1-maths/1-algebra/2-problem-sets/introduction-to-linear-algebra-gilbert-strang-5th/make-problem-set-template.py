import json
import os
from collections import defaultdict


def make_ques_ref(qref_map):
    q_refs = defaultdict(lambda: '')
    for text in qref_map:
        s, e = map(int, text.split('-'))
        q_ref = open('src/data/ques_ref_template.txt').read().format(s=s, e=e)
        for i in range(s, e + 1):
            q_refs[i] = q_ref
    return q_refs


def make_md_py_files(qmax, we_max, q_refs, FOLDER):
    mdtext = open('src/data/qa_md_template.txt').read()
    pytext = open('src/data/answer_py_code_template.txt').read()
    labels = ['0' + c for c in we_max] + list(range(1, qmax + 1))
    for qnumber in labels:
        folder = os.path.join(FOLDER, f'qa{qnumber}')
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, f'a{qnumber}.py')
        with open(path, 'w') as f:
            f.write(pytext.format(q=qnumber))

        path = os.path.join(folder, f'qa{qnumber}.md')
        q_ref = q_refs[qnumber]
        with open(path, 'w') as f:
            f.write(mdtext.format(q=qnumber, q_ref=q_ref))


def rename_question_images(qmax, we_max, FOLDER):
    labels = ['0' + c for c in we_max] + list(range(1, qmax + 1))
    for q in labels:
        qname = os.path.join(FOLDER, f'qa{q}/image.png')
        if os.path.exists(qname):
            newname = qname.replace('image.png', f'q{q}.png')
            os.rename(qname, newname)


def rename_solution_images(qmax, we_max, FOLDER):
    labels = ['0' + c for c in we_max] + list(range(1, qmax + 1))
    for q in labels:
        qname = os.path.join(FOLDER, f'qa{q}/image.png')
        if os.path.exists(qname):
            newname = qname.replace('image.png', f's{q}.png')
            os.rename(qname, newname)


if __name__ == '__main__':
    psinfo = json.load(open('static/documents/1-maths/1-algebra/3-problem-sets/problem-sets-introduction-to-linear-algebra-gilbert-strang-5th/ps-info.json'))
    for ps in psinfo['new']:
        FOLDER = ps['folder']
        qmax = ps['qmax']
        we_max = ps['we_max']
        qref_map = ps['qref_map']
        # q_refs = make_ques_ref(qref_map)
        # make_md_py_files(qmax, we_max, q_refs, FOLDER)
        rename_question_images(qmax, we_max, FOLDER)
        # rename_solution_images(qmax, we_max, FOLDER)

#!/bin/env python
from __future__ import with_statement

import os
import sys

import xml.etree.ElementTree as ET
from datetime import datetime


def sum(root, fn):
    fi = os.path.join(root, fn)
    with open(fi, 'r') as f:
        dic = {'PASS': 'Passed', 'FAIL': 'Analysis'}
        passed = 0
        failed = 0
        st = []
        st.append('Testcase                                               Status      Elapsed Time')
        st.append('---------------------------------------------------------------------------------')
        tree = ET.parse(f)
        for node in tree.findall('.//test'):
            skip = False
            s = node.find('status')
            tags = node.find('tags')
            for tag in tags:
                if tag.text == 'InTestingSetup':
                    skip = True
            if s is not None and not skip:
                caseStartTime = datetime.strptime(s.attrib['starttime'], '%Y%m%d %H:%M:%S.%f')
                caseEndTime = datetime.strptime(s.attrib['endtime'], '%Y%m%d %H:%M:%S.%f')
                print(caseEndTime - caseStartTime)
                st.append("%-55s%-12s%-12s" % (node.attrib['name'], dic[s.attrib['status']], caseEndTime - caseStartTime))
                if s.attrib['status'] == 'FAIL':
                    failed += 1
                else:
                    passed += 1

        st.append('')
        st.append('Number of testcase run:                %d' % (passed + failed))
        st.append('Number of testcase passed:             %d' % passed)
        st.append('Number of testcase failed:             %d' % failed)
        fp = fn[:fn.rfind('_')]
        fo = os.path.join(root, "%s.sum" % fp)
        with open(fo, 'w') as f2:
            f2.write("\n".join(st))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: %s <OUTPUT_XML> ..." % sys.argv[0])
        sys.exit(1)

    for a in sys.argv[1:]:
        if os.path.isfile(a):
            path = os.path.abspath(a)
            (d, f) = os.path.split(path)
            sum(d, f)

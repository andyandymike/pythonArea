#!/bin/env python
from __future__ import with_statement

import os
import sys
import re

import xml.etree.ElementTree as ET
from datetime import datetime


def sum(root, fn):
    fi = os.path.join(root, fn)
    with open(fi, 'r') as f:
        dic = {'PASS': 'Passed', 'FAIL': 'Analysis'}
        passed = 0
        failed = 0
        st = []
        st.append('ENVIRONMENT')
        re_build_num = re.compile(r'.*\s(\d+\.\d+.\d+.\d+)')
        ds_build = os.environ.get('DS_BUILD')
        if ds_build:
            m = re_build_num.match(os.environ.get('DS_BUILD'))
            ds_build = (m.group(1) if m else '?')
        else:
            ds_build = '?'
        st.append('BUILD: %s' % ds_build)
        st.append('\n')
        st.append('Date : %s' % datetime.strftime(datetime.now(), '%a %b %d %H:%M:%S %Y'))
        st.append('')
        st.append('Testcase                                               Status      Elapsed Time      SP')
        st.append('---------------------------------------------------------------------------------------')
        tree = ET.parse(f)
        for node in tree.findall('.//test'):
            skip = False
            s = node.find('status')
            tags = node.find('tags')
            doc = node.find('doc')
            if tags is not None:
                for tag in tags:
                    if tag.text == 'InTestingSetup':
                        skip = True
            if s is not None and not skip:
                caseStartTime = datetime.strptime(s.attrib['starttime'], '%Y%m%d %H:%M:%S.%f')
                caseEndTime = datetime.strptime(s.attrib['endtime'], '%Y%m%d %H:%M:%S.%f')
                elapsedTime = str(caseEndTime - caseStartTime)[:7]
                document = (doc.text if doc is not None else '')
                st.append("%-55.54s%-12s%-18s%-12s" % (node.attrib['name'] + ' ' + document, dic[s.attrib['status']], elapsedTime, 'NA'))
                if s.attrib['status'] == 'FAIL':
                    failed += 1
                else:
                    passed += 1

        st.append('')
        st.append('Number of testcase planed:             0')
        st.append('Number of testcase run:                %d' % (passed + failed))
        st.append('Number of testcase passed:             %d' % passed)
        st.append('Number of testcase failed:             %d' % failed)
        fp = fn[:fn.rfind('_')]
        fo = os.path.join(root, "%s.sum" % fp)
        with open(fo, 'w') as f2:
            os.chmod(fo, 0777)
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

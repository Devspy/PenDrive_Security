#!/usr/bin/python36

import subprocess
import os

subprocess.getoutput(" python36 /root/Desktop/project/camera.py")
subprocess.getoutput("sudo ansible-playbook /root/Desktop/project/tar.yml")
subprocess.getoutput("sudo ansible-playbook /root/Desktop/project/mail.yml")
subprocess.getoutput(" rm -rf /root/Desktop/project/photo/* ")
subprocess.getoutput(" rm -rf /root/Desktop/project/photo.tar.gz ")

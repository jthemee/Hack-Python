from distutils.core import setup
import py2exe,socket,sys,subprocess

sys.argv.append("py2exe")
setup(console=[{'script':'payload.py'}],options={'py2exe':{'bundle_files':1}},zipfile=None,)

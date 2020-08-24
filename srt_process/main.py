import re
from tkinter import filedialog

fType = [('字幕文件', '*.srt')]
initDir = 'D:\\Videos'
try:
    srtPath = filedialog.askopenfilename(filetypes = fType, initialdir = initDir)
except:
    exit()

srtName = re.findall(r"[0-9a-zA-Z]+\.srt$", srtPath)[0]
#print(srtName)

srtIn = open(srtPath, 'r', encoding = 'utf-8')
srtOut = open(r"D:/out_" + srtName, 'w', encoding = 'utf-8')

subNo = 1
ch = re.compile(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}")
for line in srtIn:
    if ch.search(line):
        srtOut.write('%s\n' % (subNo) + line)
        subNo += 1
    else:
        srtOut.write(line)

srtIn.close()
srtOut.close()
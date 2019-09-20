#递归遍历指定目录文件输出文件夹名+文件名，可指定过滤关键词及后缀名
#https://roceys.cn
#2019-09-20 17:28:04

import os
import time

def containsStr(str,filters):
    return True if any(s in str for s in filters) else False

def loopPath(dir):
    videoExts = ['mp4','mkv','avi','qtm','mpeg','mpg','rmvb','mov','wmv','asf','dat','mpa','mpe','wvx','asx','swf','rm']
    imageExts = ['jpg','jpeg','png','gif','ico','webp','raw','psd','cdr','dxf','pcx','bmp','tiff','tga','exif','svg','fpx','cr2','nef','dng']
    audioExts = ['wav','mp3','ogg','flac','ape','aif','aiff','au','svx','snd','mid','voc','wma','cdda','wv','aac','m4a','m4p']
    textExts = ['pdf', 'doc', 'docx','rtf','epub', 'txt','xls', 'xlsx','csv', 'wps','odf','djvu', 'chm', 'ppt', 'pptx']
    nameFilters = ['xxx','巨乳','大奶','露出','番号','无码','做爱','性爱','爱爱','性交','颜射','后入']
    dirFilters = ['xml']
    whiteLists = []
    xxxLists = []
    audioLists = []
    videoLists = []
    imageLists = []
    textLists  = []
    allLists = []
    i = 0

    for rootDir, subDir, fileNameLists in os.walk(dir):
        for fileName in fileNameLists:
            fullName = os.path.join(rootDir, fileName)
            if containsStr(rootDir,dirFilters) and i == 1: #过滤一级目录名
                xxxLists.append(fullName)
            else:
                if containsStr(fileName,nameFilters):
                    xxxLists.append(fullName)
                else:
                    whiteLists.append(fullName)

                if fileName.split('.')[-1] in videoExts:
                    videoLists.append(fullName)

                if fileName.split('.')[-1] in audioExts:
                    audioLists.append(fullName)

                if fileName.split('.')[-1] in imageExts:
                    imageLists.append(fullName)

                if fileName.split('.')[-1] in textExts:
                    textLists.append(fullName)
        i += 1

    # 0为白名单文件 1为敏感文件 2为音频文件 3为视频文件 4为图片文件 5为文本文件
    allLists.append(whiteLists)
    allLists.append(xxxLists)
    allLists.append(audioLists)
    allLists.append(videoLists)
    allLists.append(imageLists)
    allLists.append(textLists)
    return allLists

def writeFiles(fname,data):
    today = time.strftime('%Y-%m-%d-', time.localtime())
    with open(today + fname, 'wt', encoding='utf8') as sfile:
        for v in data:
            print(v, file=sfile)
    return

if __name__ == '__main__':
    start = time.time()
    if not os.path.exists('X:\\'):
        os.system(r'net use X: \\XIAOMI_7CA8\XiaoMi-usb0')

    dir = "X:\\"
    # dir = "X:\新建文件夹"

    all = loopPath(dir)

    writeFiles('whiteFiles.txt',all[0])

    writeFiles('xxxfiles.txt',all[1])

    writeFiles('audioFiles.txt',all[2])

    writeFiles('videoFiles.txt',all[3])

    writeFiles('imageFiles.txt',all[4])

    writeFiles('textFiles.txt',all[5])

    print('耗时：'+ str(time.time()-start) + '秒')
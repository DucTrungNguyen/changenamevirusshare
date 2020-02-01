import os


def compare():
    pathFolderVirusTotal = '/home/nguyentrung/apk/abc'
    pathFolderApk = '/home/nguyentrung/apk/samples'

    arrVT = []
    for filenameVT in os.listdir(pathFolderVirusTotal):
        a = filenameVT.split('.')
        filenameVT = a[0]
        arrVT.append(filenameVT)


    for filenameApk in os.listdir(pathFolderApk):
        b = filenameApk.split('.')
        filenameApk = b[0]
        if filenameApk in arrVT:
            os.remove(pathFolderApk + '/'+filenameApk + '.apk')


if __name__ == "__main__":
    compare()
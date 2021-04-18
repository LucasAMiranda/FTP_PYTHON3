'''código responsável por baixar uma arquivo binário, como uma imagem, pdf, vídeo ou qualquer outro formato que não seja
ASCII. '''

from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
ftp.cwd('/pub/linux/logos/pictures')
with open('pai_do_linux.jpg', 'wb') as arq:
    ftp.retrbinary('RETR linus-father-of-linux.jpg', arq.write)
ftp.quit()
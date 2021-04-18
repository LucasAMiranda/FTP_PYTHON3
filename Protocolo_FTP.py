from ftplib import *
ftp_ativo = False
ftp = FTP('ftp.ibge.gov.br')
print(ftp.getwelcome())
usuario = input("Digite o usuário:")
senha = input("Digite a senha: ")
ftp.login(usuario, senha)
print("O diretório atual de trabalho ", ftp.pwd())
ftp.cwd('pub')
print("O diretório corrente ", ftp.pwd())
print(ftp.retrlines('LIST'))
ftp.quit()

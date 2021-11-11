from ftp_setup import process_file_ftp

ftpserv = "ftp.vandereyken.be"
ftpuser = "vandereyken.be"
ftppwd = "4uYtQCRJkuobZt"
outPath = "/"
# ftpfile = "ftptest.txt"
inPath = "ftpget/"
ftpfile = "upload.txt"
upload = False

process_file_ftp(ftpserv, "21", 1, ftpuser, ftppwd, outPath, inPath, "ftptest2.txt", upload)

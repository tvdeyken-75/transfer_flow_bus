import ftplib as flib

# define variables for server and login:
# host = "ftp.vandereyken.be"
# port = "21"
# timeout = 10
# user = "vandereyken.be"
# pswd = "4uYtQCRJkuobZt"
# # pswd = "wrongpassword"
#
# outbound = "upload.txt"
# inbound = "download.txt"
# outPath = "/"
# inPath = "ftpget/"
# isUpload = False


def check_connection_ftp(host, port, timeout, user, pswd):
    if host is None or port is None or user is None or pswd is None or timeout < 1:
        msg = "One or more variables are empty or missing"
        status = False
        if timeout < 1:
            msg = "Timeout should be higher then 0"
            status = False
    else:
        try:
            ftp = flib.FTP(host)
        except flib.all_errors as err:
            msg = err
            status = False
        else:
            try:
                ftp.login(user, pswd)
            except flib.all_errors as err:
                msg = err
                status = False
            else:
                msg = "Connection check to " + host + " is valid"
                status = True
    if status is True:
        message = "Success: ", msg
    else:
        message = "Failure", msg
    return message, status


def process_file_ftp(host, port, timeout, user, pswd, outPath, inPath, filename, isUpload):
    check = check_connection_ftp(host, port, timeout, user, pswd)
    if check[1] is True:
        if isUpload is False:
            try:
                ftp = flib.FTP(host)
                ftp.login(user, pswd)
                ftp.cwd(outPath)
                if inPath == "":
                    ftp.retrbinary("RETR " + filename, open("/" + filename, 'wb').write)
                else:
                    ftp.retrbinary("RETR " + filename, open(inPath + filename, 'wb').write)
                ftp.retrbinary("RETR " + filename, open("tmp/" + filename, 'wb').write)
                with open('tmp/' + filename) as f:
                    body = f.read()
                status = filename + " is stored on ftp server " + host
            except flib.all_errors as e:
                body = None
                status = "Error: ", e
        else:
            try:
                ftp = flib.FTP(host)
                ftp.login(user, pswd)
                ftp.cwd(outPath)
                file = open(filename, 'rb')
                ftp.storbinary('STOR ' + filename, file)
                file.close()
                ftp.quit()
                body = None
                status = filename + " was downloaded and can be found in " + inPath
            except flib.all_errors as e:
                body = None
                status = "Error: ", e
        return body, status
    else:
        print("Dit ging fout: ", check[0])


def remove_file_ftp(host, port, timeout, user, pswd, outPath, filename):
    ftp = flib.FTP(host)
    ftp.login(user, pswd)
    ftp.cwd(outPath)
    file = ftp.nlst()
    if file is None or len(file) == 0:
        msg = filename + " doesn't exist in " + outPath + " on " + host
    else:
        ftp.delete(filename)
        msg = filename + " is deleted from "  + outPath + " on " + host

#! /usr/bin/python
#apod-dybg-py
#by boot1110001

### IMPORTS ####################################################################
import socket
import ssl
import base64
import datetime #to get the time

import log

### NON EDITABLE VARIABLES #####################################################


### EDITABLE VARIABLES #########################################################
verbose = 3

### FUNCTIONS ##################################################################
def by_b64(by):
    b64 = base64.b64encode(by)
    return b64

def mysend(sock, sdata, expected, verbose):
    if verbose >= 3: log.p.cout(repr(sdata))
    sock.sendall(sdata)
    rdata = sock.recv(1024)
    if verbose >= 3: log.p.cin(repr(rdata))
    if rdata.decode("utf-8")[:3] != expected:
        log.p.fail(expected+' reply not received from server')

def mysslsend(sslsock, sdata, expected, verbose):
    if verbose >= 3: log.p.sslcout(repr(sdata))
    sslsock.sendall(sdata)
    rdata = sslsock.recv(1024)
    if verbose >= 3: log.p.sslcin(repr(rdata))
    if rdata.decode("utf-8")[:3] == '535':
        log.p.fail("the credentials of the mailfrom are incorrect")
    elif rdata.decode("utf-8")[:3] != expected:
        log.p.fail(expected+' reply not received from server')

def mysslonlysend(sslsock, sdata, verbose):
    if verbose >= 3: log.p.sslcout(repr(sdata))
    sslsock.sendall(sdata)

def https_end_and_recive(sslsock, expected, verbose):
    if verbose >= 3: log.p.sslcout(repr(b'\r\n'))
    sslsock.sendall(b'\r\n')

    rdata = b''
    rdatal = 0
    while True:
        # print(rdatal)
        rdata += sslsock.recv(1024)
        if (len(rdata) == rdatal):
            break
        rdatal = len(rdata)

    if verbose >= 3: log.p.sslcin(repr(rdata))
    if rdata.decode("ISO-8859-1")[:15] != expected:
        log.p.fail(expected+' reply not received from server')

### MAIN #######################################################################
def main():
    host = 'apod.nasa.gov'
    bhost = host.encode('utf-8')
    webpage = '/apod/astropix.html'
    bwebpage = webpage.encode('utf-8')
    port = 443

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    sslsock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_SSLv23)

    mysslonlysend(sslsock, b'GET ' + bwebpage + b' HTTP/1.1\r\n', verbose)
    mysslonlysend(sslsock, b'User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)\r\n', verbose)
    mysslonlysend(sslsock, b'Host: apod.nasa.gov\r\n', verbose)
    mysslonlysend(sslsock, b'Accept-Language: en-us\r\n', verbose)
    mysslonlysend(sslsock, b'Connection: Keep-Alive\r\n', verbose)
    https_end_and_recive(sslsock, 'HTTP/1.1 200 OK', verbose)

    pass

### EXEC #######################################################################
main()

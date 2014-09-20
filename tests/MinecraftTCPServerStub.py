import SocketServer
import random

class MinecraftTCPServerStub(SocketServer.StreamRequestHandler):
    """
        The RequestHandler class for our server.

        It is instantiated once per connection to the server, and must
        override the handle() method to implement communication to the
        client.
        """


    PLAYER_SETTING_KEYS = ("autojump")

    WORLD_SETTING_KEYS = ("world_immutable", "nametags_visible")


    def genCommands():
        BASE_COMMANDS = ("world", "chat", "player", "events", "camera" )

        WORLD_COMMANDS = ("getBlock", \
                          "getBlockWithData", \
                          "getBlocks", \
                          "setBlock", \
                          "setBlocks", \
                          "getHeight", \
                          "getPlayerIds", \
                          ("checkpoint",("save", "restore")), \
                           "setting", \
                          )

        CHAT_COMMANDS = ("post",)

        PLAYER_COMMANDS = ("getPos", \
                           "setPos", \
                           "getTile", \
                           "setTile", \
                           "setting", )

        EVENTS_COMMANDS = ( "clear", \
                           ("block", ("hits",)), )

        CAMERA_COMMANDS = ( ("mode",("setNormal", "setFixed", "setFollow")), \
                           "setPos")



        for cmd in BASE_COMMANDS:
            # have to use a mutable object in Python 2
            # in Python 3 could use non-local for changing variable in parent scope
            cmdsToUse = []
            if cmd == "world":
                cmdsToUse.append(WORLD_COMMANDS)
            elif cmd == "player":
                cmdsToUse.append(PLAYER_COMMANDS)
            elif cmd == "events":
                cmdsToUse.append(EVENTS_COMMANDS)
            elif cmd == "camera":
                cmdsToUse.append(CAMERA_COMMANDS)
            elif cmd == "chat":
                cmdsToUse.append(CHAT_COMMANDS)

            for cmd1 in cmdsToUse[0]:
                if isinstance(cmd1, tuple):
                    for cmd2 in cmd1[1]:
                        yield cmd+"."+cmd1[0]+"."+cmd2
                else:
                    yield cmd+"."+cmd1

    COMMANDS = list(genCommands())

    BLOCK_IDS =(0 , \
            1 , \
            2 , \
            3 , \
            4 , \
            5 , \
            6 , \
            7 , \
            8 , \
            9 , \
            10 , \
            11 , \
            12 , \
            13 , \
            14 , \
            15 , \
            16 , \
            17 , \
            18 , \
            20 , \
            21 , \
            22 , \
            24 , \
            26 , \
            30 , \
            31 , \
            35 , \
            37 , \
            38 , \
            39 , \
            40 , \
            41 , \
            42 , \
            43 , \
            44 , \
            45 , \
            46 , \
            47 , \
            48 , \
            49 , \
            50 , \
            51 , \
            53 , \
            54 , \
            56 , \
            57 , \
            58 , \
            60 , \
            61 , \
            62 , \
            64 , \
            65 , \
            67 , \
            71 , \
            73 , \
            78 , \
            79 , \
            80 , \
            81 , \
            82 , \
            83 , \
            85 , \
            89 , \
            95 , \
            98 , \
            102 , \
            103 , \
            107 , \
            246 , \
            247 , \
)


# World bounds (space that exists)
    MAX_X = 127
    MIN_X = -127

    MAX_Y = 127
    MIN_Y = -127

    MAX_Z = 127
    MIN_Z = -127

    # data value limits
    MIN_DATA = 0
    MAX_DATA = 15


    TERRAIN = list(random.randint(-127, 127) for x in xrange(-127, 127))

    def randomIntCoord(self, min, max):
        return random.randint(min, max)

    def randomFloatCoord(self, min, max):
        return random.uniform(min, max)

    def worldRequest(self, cmd, data):

        if cmd[1] == "getHeight":
            if len(data) != 2:
                self.failedRequest(".".join(cmd.extend(data)))
            self.wfile.write("%d\n\n" % self.TERRAIN[int(data[0])])
        elif cmd[1] == "getBlock":
            self.wfile.write("%d\n\n" % self.BLOCK_IDS[random.randint(0, len(self.BLOCK_IDS))])

        elif cmd[1] == "getBlockWithData":
            self.wfile.write("%d,%d\n\n" % (self.BLOCK_IDS[random.randint(0, len(self.BLOCK_IDS))], random.randint(0,15)))
        elif cmd[1] == "getBlocks":
            self.wfile.write("BUGGED\n\n")
        elif cmd[1] == "setBlock":
            pass
        elif cmd[1] == "setBlocks":
            pass
        elif cmd[1] == "getPlayerIds":
            self.wfile.write("%d|%d|%d\n\n" % (1, 20, 57))
        elif cmd[1] == "checkpoint":
            pass
        elif cmd[1] == "setting":
            if dataLen == 2:
                if data[0] in self.WORLD_SETTING_KEYS:
                    if data[1] in [0,1]:
                        pass
                    else:
                        self.failedRequest(".".join(cmd.extend(data)))
                else:
                    self.failedRequest(".".join(cmd.extend(data)))
            else:
                self.failedRequest(".".join(cmd.extend(data)))
        else:
            self.failedRequest(".".join(cmd.extend(data)))

    def cameraRequest(self, cmd,  data):
        print cmd
        print data
        pass

    def playerRequest(self, cmd,  data):
        #TODO validate data and command for each possible action
        dataLen = len(data)
        if cmd[1] == "getTile":
            if dataLen == 0:
                self.wfile.write("%d,%d,%d\n\n" % (self.randomIntCoord(self.MIN_X, self.MAX_X),self.randomIntCoord(self.MIN_Y, self.MAX_Y),self.randomIntCoord(self.MIN_Z, self.MAX_Z)) )
            else:
                self.failedRequest(".".join(cmd.extend(data)))

        elif cmd[1] == "setTile":
            if dataLen == 3:
                pass
            else:
                self.failedRequest(".".join(cmd.extend(data)))

        elif cmd[1] == "getPos":
            if dataLen == 0:
                self.wfile.write("%f,%f,%f\n\n"% (self.randomFloatCoord(self.MIN_X, self.MAX_X),self.randomFloatCoord(self.MIN_Y, self.MAX_Y),self.randomFloatCoord(self.MIN_Z, self.MAX_Z)) )
            else:
                self.failedRequest(".".join(cmd.extend(data)))

        elif cmd[1] == "setPos":
            if dataLen == 3:
                pass
            else:
                self.failedRequest(".".join(cmd.extend(data)))

        elif cmd[1] == "setting":
            if dataLen == 2:
                if data[0] in self.PLAYER_SETTING_KEYS:
                    if data[1] in [0,1]:
                        pass
                    else:
                        self.failedRequest(".".join(cmd.extend(data)))
                else:
                    self.failedRequest(".".join(cmd.extend(data)))
            else:
                self.failedRequest(".".join(cmd.extend(data)))

        else:
            self.failedRequest(".".join(cmd.extend(data)))
            print cmd
            print data
            pass

    def eventsRequest(self, cmd, data):
        print cmd
        print data
        if cmd[1] == "block":
            if cmd[2] == "hits":
                self.wfile.write("%d,%d,%d,%d,%d,%d|%d,%d,%d,%d,%d,%d|%d,%d,%d,%d,%d,%d\n\n" % (0, 20, 57, -65, 3, 1,    0, -10, 78, -75, 4, 1,    0, -2, 7, 5, 2, 1))

    def chatRequest(self, cmd, data):
        print cmd
        print data
        pass

    def failedRequest(self, data):
        print "Failed Request for command %s " % (data)
        self.wfile.write("Fail")
        pass


    def handle(self):
        while 1:
            # self.rfile is a file-like object created by the handler;
            # we can now use e.g. readline() instead of raw recv() calls
            self.data = self.rfile.readline().strip()
            if not self.data:
                break

            print "handle called"

            print "{} wrote:".format(self.client_address[0])
            print self.data
            commandSent = self.data.partition("(")
            command = commandSent[0]
            commandData = commandSent[2].rstrip(")")
            print "command is |"+command+"|"

            if command in MinecraftTCPServerStub.COMMANDS:
                print "command allowed"
                # Now split into appropriate handling function
                commandSections = command.split(".")
                comData = filter(None, commandData.split(","))
                print commandSections
                print comData

                if commandSections[0] == "world":
                    self.worldRequest(commandSections, comData)
                elif commandSections[0] == "player":
                    self.playerRequest(commandSections, comData)
                elif commandSections[0] == "camera":
                    self.cameraRequest(commandSections, comData)
                elif commandSections[0] == "events":
                    self.eventsRequest(commandSections, comData)
                elif commandSections[0] == "chat":
                    self.chatRequest(commandSections, comData)
                else :
                     self.failedRequest(self.data)
            else:
            # Likewise, self.wfile is a file-like object used to write back
            # to the client
                self.failedRequest(self.data)



if __name__ == "__main__":
    HOST, PORT = "localhost", 4711

    # Create the server, binding to localhost on port 4711
    server = SocketServer.TCPServer((HOST, PORT), MinecraftTCPServerStub)
    print server.allow_reuse_address
    #server.allow_reuse_address = True
    print server.server_address
    print server.socket

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
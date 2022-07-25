import sys, getopt

class Arguments:

    def getArguments(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],"f:d:p:",["faze=","data=", "port="])
        except getopt.GetoptError:
            sys.exit(2)

        for opt, arg in opts:
            if opt in ("-f", "--faze"):
                self.faze = int(arg)
            elif opt in ("-d", "--data"):
                self.data = (arg)
            elif opt in ("-p", "--port"):
                self.port = int(arg)
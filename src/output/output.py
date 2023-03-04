class Output:
    @staticmethod
    def cli(object):
        print(object, "\n")

    @staticmethod
    def redis(key, object):
        r=Redis(host="host.local")
        if r.rpush(key, object):
            return True

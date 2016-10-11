import pickle
class Tools():
    def __init__(self):
        pass
    @staticmethod
    def pickle_file(dest, contents):
        f = open(dest, 'wb')
        pickle.dump(contents, f)
        f.close()
    @staticmethod
    def retive_file(source):
        f = open(source, 'rb')
        d = pickle.load(f)
        f.close()
        return d
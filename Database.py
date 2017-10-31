import pickle

class database:
    def __init__(self):
        try:
            self.data = pickle.load(open('database.p', 'rb'))
        except:
            self.data = {}
            self.data['config'] = {
                'pid_current': 100,
                'fid_current': 200,
                'initMe': True
            }

            self.data['producers'] = []
            self.data['films'] = []

            pickle.dump(self.data, open('database.p', 'wb'))
    def __del__(self):
        pickle.dump(self.data, open('database.p', 'wb'))
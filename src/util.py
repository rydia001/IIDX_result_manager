clearflg_dict={
    "clflg7": 7,
    "clflg6": 6,
    "clflg5": 5,
    "clflg4": 4,
    "clflg3": 3,
    "clflg2": 2,
    "clflg1": 1,
    "clflg0": 0
    }

djlevel_dict={
    "AAA": 8,
    "AA": 7,
    "A": 6,
    "B": 5,
    "C": 4,
    "D": 3,
    "E": 2,
    "F": 1,
    "---": 0
    }

difficulty_dict={
    "ANOTHER": 3,
    "HYPER": 2,
    "NORMAL": 1,
    "BEGINNER": 0
    }

spdp_dict={
    "DP": 1,
    "SP": 0
    }

clearflgs = ["---", "F", "A", "E", "N", "H", "EXH", "FC"]
djlevels = {djlevel_dict[k]: k for k in djlevel_dict}
difficulties = {difficulty_dict[k]: k for k in difficulty_dict}
spdps = {spdp_dict[k]: k for k in spdp_dict}

class Music_data:
    def __init__(self, spdp, level, name, difficulty, djl, score, clf):
        self.__data = {"Music": name,
                        "SPDP": spdp_dict[spdp],
                        "Difficulty": difficulty_dict[difficulty],
                        "LEVEL": int(level),
                        "DJLEVEL": djlevel_dict[djl],
                        "SCORE": int(score),
                        "CLEAR": clearflg_dict[clf]
                       }


    def get_data(self):
        return self.__data


    def get_data_readable(self):
        data_readable = {"Music": self.__data["Music"],
                        "SPDP": spdps[self.__data["SPDP"]],
                        "Difficulty": difficulties[self.__data["Difficulty"]],
                        "LEVEL": self.__data["LEVEL"],
                        "DJLEVEL": djlevels[self.__data["DJLEVEL"]],
                        "SCORE": self.__data["SCORE"],
                        "CLEAR": clearflgs[self.__data["CLEAR"]]
                       }
        return data_readable

    def __repr__(self):
        return str(self.get_data_readable())

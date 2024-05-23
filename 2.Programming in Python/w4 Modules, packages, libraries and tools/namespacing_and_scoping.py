# LGBE

# Global
trm = "lilo"
print("Global var: {}".format(trm))


class scopes:
    pass

    def f1(self):
        # local
        v = 2 + 2
        k = trm
        print(v, k)

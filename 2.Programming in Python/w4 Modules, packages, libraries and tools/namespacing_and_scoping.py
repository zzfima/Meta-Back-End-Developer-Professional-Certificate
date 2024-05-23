# LGBE

# Global
var_g = "var global"
var_nl = "var nl"


def fn_out():
    var_nl1 = "fsd1"

    def fnc_local():
        # Local
        var_l = "vr local"
        print("Local var: {}".format(var_l))
        nonlocal var_nl1
        var_nl1 = "fsd2"

    print("fn_out var: {}".format(var_nl1))
    fnc_local()
    print("fn_out var: {}".format(var_nl1))


def fnc_enclosed():
    # Enclosed
    var_g = "var enclosed"
    print("Enclosed var: {}".format(var_g))


print("Global var nl: {}".format(var_nl))
print("Global var: {}".format(var_g))
fn_out()
fnc_enclosed()
print("Global var: {}".format(var_g))
print("Global var nl: {}".format(var_nl))

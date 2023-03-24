def checkScope():
    def do_local():
        test="local test"
    def do_non_local():
        nonlocal test
        test="non local test"
    def do_global():
        global test
        test="global test"

    test="default"
    do_local()
    print("Test value after do local: "+test)
    do_non_local()
    print("Test value after do non local: " + test)
    do_global()

checkScope()
print("Test value after do global: " + test)
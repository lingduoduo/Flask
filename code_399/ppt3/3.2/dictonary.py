# -*- coding: utf-8 -*-
if __name__ == "__main__":
    dict = {}
    dict["one"] = "1 - google.com"
    dict[2] = "2 - gmail.com"

    tinydict = { "name":"gmail", "code":1 , "site":"www.google.com" }
    print( dict )
    print( dict[ "one" ] )
    print( dict[ 2 ] )
    print( tinydict )
    print( tinydict.keys() )
    print( tinydict.values() )

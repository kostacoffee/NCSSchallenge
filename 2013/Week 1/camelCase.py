def to_camel(ident):
    ident = str(ident)
    while ("_" in ident):
        underscoreIndex = ident.find("_")
        ident = ident[:underscoreIndex+1] + ident[underscoreIndex+1].upper() + ident[underscoreIndex+2:]
        ident = ident.replace("_","",1)
    return ident

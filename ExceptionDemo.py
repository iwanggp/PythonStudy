def safe_float(obj):
    try:
        retval=float(obj)
    except (ValueError,TypeError) as diag:
        retval=str(diag)
    return retval
print(safe_float(111))
print(safe_float("sssss"))
assert 1==1,'one does not equal zero silly'
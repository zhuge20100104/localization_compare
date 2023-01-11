

def test_str():
    src = '''Recorded since:
%1$s at %2$s'''
    dst = '''Recorded since:\\n%1$s at %2$s'''
    src = src.replace("\n", "\\n")
    print(src)
    print(dst)
    assert src == dst, "Source and dest string are not equal"
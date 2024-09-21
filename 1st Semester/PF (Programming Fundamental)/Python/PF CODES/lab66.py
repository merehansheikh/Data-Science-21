def GPA(pf, pfl, pst, iict, iictl, ecc, qt):
    if pf == "A":
        pf = (3*5)
        return pf
    elif pfl == "A":
        pfl = (1*5)
        return pfl
    elif pst == "A":
        pst = (2*5)
        return pst
    elif iict == "A":
        iict = (2*5)
        return iict
    elif iictl == "A":
        iictl = (1*5)
        return iictl
    elif ecc == "A":
        ecc = (3*5)
        return ecc
    elif qt == "A":
        qt = (3*5)
        return qt
    elif qt == "B":
        qt = (3*4)
        return qt
    add = (pf + pfl + pst + iict + iictl + ecc + qt) / 12.5
    gpa = add / 12.5
    return add
def main():
    pf = str(input())
    pfl = str(input())
    pst = str(input())
    iict = str(input())
    iictl = str(input())
    ecc = str(input())
    qt = str(input())
    print(GPA(pf, pfl, pst, iict, iictl, ecc, qt))

main()

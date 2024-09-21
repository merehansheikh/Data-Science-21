def GPA(pf, pfl, pst, iict, iictl, ecc, qt):
    GPA = (pf*3 + pfl*1 + pst*2 + iict*2 + iictl*1 + ecc*3 + qt*0.5)/12.5
    return GPA
def main():
    pf_g = input('Enter your grade in PF: ')
    pflab_g = input('Enter your grade in PF Lab: ')
    pst_g = input('Enter your grade in PST: ')
    iict_g = input('Enter your grade in IICT: ')
    iictlab_g = input('Enter your grade in IICT Lab: ')
    ecc_g = input('Enter your grade in ECC: ')
    qt_g = input('Enter your grade in QT: ')
    #for calculating gpa in pf
    if pf_g == "A":
        pf_gpa = 5
    elif pf_g == "B":
        pf_gpa = 4
    elif pf_g == "C":
        pf_gpa = 3
    elif pf_g == "D":
        pf_gpa = 2
    elif pf_g == "E":
        pf_gpa = 1
    elif pf_g == "F":
        pf_gpa = 0
    #for calculating gpa in pflab
    if pflab_g == "A":
        pflab_gpa = 5
    elif pflab_g == "B":
        pflab_gpa = 4
    elif pflab_g == "C":
        pflab_gpa = 3
    elif pflab_g == "D":
        pflab_gpa = 2
    elif pflab_g == "E":
        pflab_gpa = 1
    elif pflab_g == "F":
        pflab_gpa = 0
    #for calculating gpa in pst
    if pst_g == "A":
        pst_gpa = 5
    elif pst_g == "B":
        pst_gpa = 4
    elif pst_g == "C":
        pst_gpa = 3
    elif pst_g == "D":
        pst_gpa = 2
    elif pst_g == "E":
        pst_gpa = 1
    elif pst_g == "F":
        pst_gpa = 0
    #for calculating gpa in iict
    if iict_g == "A":
        iict_gpa = 5
    elif iict_g == "B":
        iict_gpa = 4
    elif iict_g == "C":
        iict_gpa = 3
    elif iict_g == "D":
        iict_gpa = 2
    elif iict_g == "E":
        iict_gpa = 1
    elif iict_g == "F":
        iict_gpa = 0
    #for calculating gpa in iict lab
    if iictlab_g == "A":
        iictlab_gpa = 5
    elif iictlab_g == "B":
        iictlab_gpa = 4
    elif iictlab_g == "C":
        iictlab_gpa = 3
    elif iictlab_g == "D":
        iictlab_gpa = 2
    elif iictlab_g == "E":
        iictlab_gpa = 1
    elif iictlab_g == "F":
        iictlab_gpa = 0
    #for calculating gpa in ecc
    if ecc_g == "A":
        ecc_gpa = 5
    elif ecc_g == "B":
        ecc_gpa = 4
    elif ecc_g == "C":
        ecc_gpa = 3
    elif ecc_g == "D":
        ecc_gpa = 2
    elif ecc_g == "E":
        ecc_gpa = 1
    elif ecc_g == "F":
        ecc_gpa = 0
    #for calculating gpa in qt
    if qt_g == "A":
        qt_gpa = 5
    elif qt_g == "B":
        qt_gpa = 4
    elif qt_g == "C":
        qt_gpa = 3
    elif qt_g == "D":
        qt_gpa = 2
    elif qt_g == "E":
        qt_gpa = 1
    elif qt_g == "F":
        qt_gpa = 0
    #for calculatig total gpa
    gpa = GPA(pf_gpa, pflab_gpa, pst_gpa, iict_gpa, iictlab_gpa, ecc_gpa, qt_gpa)
    print('Your GPA is ', gpa)

main()

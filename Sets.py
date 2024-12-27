foods= {"burger","fries","pizza","salad","rice","dumplings","apple",}
print(foods)

print(type(foods))


foods.add("Lopado_temacho_selacho_galeo_kranio_leipsano_drim_hyp_trimmato_silphio_karabo_melit_katakechy_meno_kichl_epi_kossypho_phatto_periste_alektryo_opte_kephallio_kigklo_peleio_lagoio_siraio_baphe_tragano_pterygon")
print(foods)

foods.remove("apple")
print(foods)

foods.pop
print(foods)

A = {"HA","Y"}
B = {"PP","Y"}

print(A.union(B))
print(A.difference(B))
print(B.difference(A))
print(A.intersection(B))
print(A.symmetric_difference(B))
#Game


print("Choose on of the folowing options:")
print("1.Create a Union")
print("2.Create a difference")
print("3.Create a intersection")
print("4.Create a symetric difference")

while True:
    UserChoice = input("Choose on of the folowing numbers:")
    if UserChoice == "1":
        print(A.union(B))
    elif UserChoice =="2":
        print(A.difference(B))
    elif UserChoice =="3":
        print(A.intersection(B))
    elif UserChoice == "4":
        print(A.symmetric_difference(B))
    else:
        print("???(type 1,2,3 or 4)")



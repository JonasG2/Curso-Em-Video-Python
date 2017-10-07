# ------------- VERIFICANDO SE TEM "SANTO" NO NOME DA CIDADE ----------- #

city = str(input("Em qual cidade vocẽ nasceu? ")).strip()

print (city[:5].upper() == 'SANTO')
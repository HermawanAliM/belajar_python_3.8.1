# Belajar Bahasa Pemrograman Python

"""
#? Apa itu tipe data..?
- Mengutip dari wikipedia
Tipe data atau kadang disingkat dengan ‘tipe’ saja adalah sebuah pengelompokan data untuk memberitahu compiler 
atau interpreter bagaimana programmer ingin mengolah data tersebut

- Sedangkan secara sederhana, tipe data adalah cara kita memberitahu komputer untuk mengelompokkan data berdasarkan apa yang dipahami oleh komputer.

#! Tipe data pada Python menurut W3S :
- teks : str
- angka : int, float, complex
- urut : list, tuple, range
- pemetaan : dict
- boolean : bool
- binary : bytes, bytesarray,memoryview
- set : set, frozenset

#! Bila ingin mengetahui sebuah tipe data pada variable gunakan fungsi yang namanya type()
- type(nama_variable)

"""

# untuk str -> string yang merupakan teks
# penulisan string boleh menggunakan ' ', " ", ''' ''', """" """"
tanya = '\tSiapa namamu..?'
jawab = "\tNamaku Eich"
tanyaJawab = """ 
  Kamu  : "Kamu lagi apa..?"
  Aku   : "Lagi ngoding nih"
  Kamu  : "Ohh gitu"
  Aku   : "Iya gitu" 
"""
print(tanya) # Menampilkan atau mencetak isi dari variable
print(jawab)
print(tanyaJawab) 
print(type(tanyaJawab)) # Untuk mengetahui tipe data apa yang kita digunakan


# untuk int -> integer yang meruapakan angka yang bulat
# int tidak perlu menggunakan tanda ' ', " ", ''' ''', """" """" pada penulisannya
# untuk penulisan angka tidak boleh diawali dengan angka "0"
tanggalLahir = 18
bulanLahir = 8

print("\n", tanggalLahir)
print(bulanLahir)
print(type(tanggalLahir))

# untuk float itu bilangan pecahan atau bilangan real
# untuk penulisan sama dengan int
phi = 3.14
ipk = 2.5

print("\n", phi)
print(ipk)
print(type(phi))

# untuk complex itu bilangan yang menyatakan pasangan angka real & imajiner
# untuk complex penulisan sama dengan int
comp = 1 + 5j
comp2 = 17j + 1
print("\n",comp)
print(comp2)
print(type(comp2))

# untuk list itu tipe data yang bisa menampung lebih 2 nilai
# untuk penulisan menggunakan tanda []
myList = ["Hermawan", 18]
print("\n", myList)
print(type(myList))

# untuk range itu mengembalikan deret integer secara berurutan
numSort = range(10)
print("\n", numSort)
print(type(numSort))

# untuk tuple itu sama seperti list, cuman tuple ini bersifat immutable 
# untuk penulisan menggunakan tanda ()
myTuple = (18, 8, "Ali")
print("\n", myTuple)
print(type(myTuple))

# untuk dict atau dictionary ini berbeda dengan list & tuple
# untuk penulisan menggunakan tanda {}
myDict = {'name':"Hermawan", 'date':18}
print("\n", myDict)
print(type(myDict))

# untuk bool atau boolean ini hanya memiliki dua nilai yaitu : True & False
letItGo = True
dontDie = False

print("\n", letItGo)
print(dontDie)
print(type(letItGo))

# untuk set ini adalah tipe data yang tidak berurut
# untuk penulisan sama seperti dict
mySet = {"Hermawan", "Ali", "M"}
print("\n", mySet)
print(type(mySet))

# untuk frozenset ini berfungsi mengubah iterable menjadi obj yang immutable
myF_set = frozenset([myTuple])
print("\n", myF_set)
print(type(myF_set))

# untuk bytes ini mengembalikan obj byte yang bersifat immutable
myBytes = b"Hermawan"
print("\n", myBytes)
print(type(myBytes))

# untuk bytearray ini mengembalikan obj bytearray dari suatu obj
myObjArr = bytearray(5)
print("\n", myObjArr)
print(type(myObjArr))

# untuk memory view ini mengembalikan obj memory view dari argumennya
myObjMemoV = memoryview(bytes(5))
print("\n", myObjMemoV)
print(type(myObjMemoV))

















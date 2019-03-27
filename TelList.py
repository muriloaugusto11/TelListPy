class TelList():

    def __init__(self):
        self.contact_list = [] #constructor

    def imp(self):
      name = input("\n NAME TO REMOVE: ").upper()
      num = input("\n NUMBER TO REMOVE: ")

    def menu(self):
        return int(input('\n TYPE:' +
                           '\n [1]- TO ADD: ' +
                           '\n [2]- TO SHOW: ' +
                           '\n [3]- TO REMOVE: ' +
                           '\n [4]- TO EXIT: \n :'))

    def show(self):
        print("\n--FONE-LIST--\n")
        for i in self.contact_list:
            print("NAME: ", i.name)
            print("NUMBER: ", i.num)
            print("")

    def execute(self):
        option = self.menu()
        while option != 4:

            if option == 1:
                print("--ADD-LIST--")
                print("")
                name = input('\n TYPE A NAME TO ADD: ').upper()
                num = input('\n TYPE A NUMBER TO ADD: ')
                contato = Contact(name, num)
                self.contact_list.append(contato)
                print("NAME", "(",name,")", "NUMBER", "(",num,")", "ADD WITH SUCCESS")

            elif option == 2:
                self.show()

            elif option == 3:
                self.show()
                self.imp()
                #contato = Contact(name, num)
                for x in self.contact_list:
                    if name == x.name and num == x.num:
                        self.contact_list.remove(x)
                        print("NAME","(",name,")","AND NUMBER","(",num,")","REMOVED WITH SUCCESS!")
                        self.show()

            elif option > 4 or option < 1:
              print("\n ERROR! SELECT A VALID NUMBER!")

            option = self.menu()

class Contact():
    def __init__(self, name, num): #constructor
        self.name = name
        self.num = num

TelList().execute()




#while True:
#    try:
#        num = int(input("Digite seu número: "))
#        if not 900000000 <= num <= 999999999:
#            raise ValueError("Não é permitido número maior ou menor que 9 caracteres")
#    except ValueError as e:
#        print("Número de telefone só pode conter numeros.", e)
#    else:
#        break
#
#print(num)##

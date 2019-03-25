class TelList():

    def __init__(self):
        self.contact_list = [] #constructor

    def menu(self):
        return int(input('\n TYPE:' +
                           '\n [1]- TO ADD: ' +
                           '\n [2]- TO SHOW: ' +
                           '\n [3]- TO REMOVE: ' +
                           '\n [4]- TO EXIT: \n :'))

    def show(self):
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
                name = input('\n TYPE A NAME TO ADD: ')
                num = input('\n TYPE A NUMBER TO ADD: ')
                contato = Contact(name, num)
                self.contact_list.append(contato)
                print("NAME ", name, "NUMBER ", num, " ADD WITH SUCCESS")

            elif option == 2:
                print("--FONE-LIST--")
                self.show()

            elif option == 3:
                self.show()
                name1 = input("\n NAME TO REMOVE: ")
                num1 = input("\n NUMBER TO REMOVE: ")
                contato = Contact(name, num)
                for x in self.contact_list:
                    if name1 == x.name and num1 == x.num:
                        self.contact_list.remove(x)
                        print("NAME","(",name1,")","AND NUMBER","(", num1,")","REMOVED WITH SUCCESS!")

            if option > 4 or option < 1:
                print("\n ERROR! SELECT A VALID NUMBER!")
                self.show()

            option = self.menu()

class Contact():
    def __init__(self, name, num): #constructor
        self.name = name
        self.num = num

TelList().execute()

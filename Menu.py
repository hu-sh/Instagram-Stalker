class Menu:
    def __init__(self, title, options):
        self.__options = options
        self.__title = title
        self.__esc = False 
        self.__choice = len(options)

    def show(self):
        i=1
        print("="* (len(self.__title)*2) )
        print("\t"+self.__title)
        print("="* (len(self.__title)*2) )
        for option in self.__options: 
            print("\t" + str(i)+ ") " + option) 
            i+=1

    def setChoice(self):
        self.__choice = int(input("Choice: "))

        if self.__choice == len(self.__options):
            self.__esc = True

        return self.__choice     

    def getChoice(self):
        return self.__choice

    def esc(self):
        return self.__esc
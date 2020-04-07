#Znajdź i popraw błędy w podanych fragmentach kodu

class menuConfig:
    """A configuration for the Menu.

    Attributes:
        title: The title of the Menu.
        body: The body of the Menu.
        button_text: The text for the button label.
        flag: Can it be cancelled?
    """
    title: str
    body: str
    button_text: str
    flag: bool = False

    def getItems(self):
        return self.body

    def checkIfMenuIsCancellable(self):             #checks if menu is cancellable
        return self.flag

    def retrieveMenuTitle(self):
        return self.title
        #print(self.title)


def Create_Menu(config: menuConfig):
    title = config.Title
    body = config.Body
    # ...


config = menuConfig()
config.title = "My delicious menu"
config.body = "A description of the various items on the menu"
config.button_text = "Order now!"
config.flag = True

Create_Menu(config)

##############################################################################################

def email_clients(clients: List[Client]):
    """Filter active clients and send them an email.
    """
    for client in clients:
        if client.active:
            email(client)
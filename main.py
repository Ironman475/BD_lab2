import model
import view
import Menu
import Controller


def main():
    Gamer = Controller.ControllerGamer(model.ModelGamer, view.View)
    Character = Controller.ControllerCharacter(model.ModelCharacter, view.View)
    Location = Controller.ControllerLocation(model.ModelLocation, view.View)
    Boss = Controller.ControllerBoss(model.ModelBoss, view.View)
    Item = Controller.ControllerItem(model.ModelItem, view.View)
    Menu.menu(Gamer, Character, Location, Boss, Item)
    Gamer.disconnect()
    Character.disconnect()
    Location.disconnect()
    Boss.disconnect()
    Item.disconnect()


if __name__ == '__main__':
    main()

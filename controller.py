from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model=Model()
        self.view=View(self)

    def on_button_click(self, caption):
        print(f'button {caption} clicked')
        if caption == "fileSelected":
            self.model.filePath=self.view.filePath
            print("Inside the controller",self.model.filePath)
        if caption == "comSelected":
            self.model.currentCom=self.view.serialSelected
        if caption == "flash":
            self.model.flash()

    def main(self):
        print("In main of controler")
        self.view.main()

    def grabValues(self):
        return self.model.serial_ports()


if __name__ == '__main__':
    flasher = Controller()
    flasher.main()
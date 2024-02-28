import modules.menus as menu
import modules.import as imp
data = {}

if __name__ == "__main__":
    data = imp.readJson('data')
    menu.menuprincipal()

import shutil
import os
import getpass
import time
from tqdm import tqdm as pb


class module_uninstaller:
    def uninstall():
        print("Telegram Bot Library Module Uninstaller")
        print("***************************************")
        print()

        try:

            pathforpackages = sys.prefix + "/Lib/site-packages/"

            print("Do you really want to uninstall this module?")
            ok = input("(y/n): ")

            if ok == "y":
                progressbar = pb(range(2), desc="Uninstalling Module")
                progressbar.update(1)

                shutil.rmtree(pathforpackages + "py_telegram")
                progressbar.update(1)
                progressbar.close()
                print("Sucessfully Uninstalled.")
                time.sleep(5)
            else:
                quit()
        except:
            print("There was an error. This could be because you don't operate Windows (10). This installer was only tested on Windows and it could raise errors in other operating systems. Please try it again or create an issue on GitHub.")

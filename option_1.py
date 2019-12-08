#open atom and terminal
def open_app():
    import subprocess
    import os
    subprocess.call('/Applications/Atom.app');
    subprocess.call('/Applications/Utilities/Terminal.app');
    os.system("python3");
    print("OPTION 1 COMPLETE");
    
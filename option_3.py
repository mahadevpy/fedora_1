def github_wid():
    import webbrowser
    f =open("github_address.txt", 'r')
    site = f.read()
    webbrowser.open(site)
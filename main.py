#### Fonction secondaire
"""f"""
def ispalindrome(p):
    """Test"""
    p=p.lower()
    mytable=p.maketrans("éèêôçëà","eeeocea","-_ /?', !:")
    p=p.translate(mytable)
    if p == p[::-1]:
        return True
    return False

#### Fonction principale
def main():
    """test"""
    # vos appels à la fonction secondaire ici
    for s in ["raDaR", "kayak"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()

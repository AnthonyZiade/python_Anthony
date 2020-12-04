# Je decide de faire un questionnaire pour voir les technologies préferés des personnes pour les comparés a les miennes et pour just voir generalement ce que les autres aime. 
# Dans le questionnaire, je vais demandé le media social le plus utilisé de l'utilisateur, combien d'heures ils/elles l'utilise et qu'elle console ils/elles utilise le plus. 

print("Quel est votre nom?")
nomUtilisateur = input()
print("Bonjour " + nomUtilisateur + ", ceci est un petit questionaire sur les technologies de nos jours. Ca prendra seulement une minute a répondre, quand tu est prêt, répond Oui")
ready = input().lower() # J'utilise .lower() pour que n'importe quoi l'utilisateur repond, ca va etre lut dans python come un mot non majuscule pour assurer que les codes son pareilles. 
if ready=="oui":
    print("Quelle medias socials utilise tu le plus entre ; Instragram, Snapchat, Twitter, Tiktok et Autre?") # J'ai ajouter un ; pour demontré les options
Q1 = input().lower()
if Q1=="instagram": # Q1 represente que c'est la premiere question du questionnaire
    print("J'utilise Instagram beaucoup aussi, mais plutot pour les memes que pour voir les photos des autres.")

elif Q1=="snapchat":
    print("Ahh Snapchat, j'aime plus voir mes amies en personne mais, durant cette pandemie, Snapchat est une bonne facon d'avoir du plaisir avec tes amies.")
    
elif Q1=="twitter":
    print("Oooh Twitter, Twitter est probablement le media que j'utilise le plus aussi, bonne choix.")

elif Q1=="tiktok":
    print("Tiktok est interessant, beaucoup de videos très droles.")

elif Q1=="autre":
    print("Ahhh interessant.")

print("Combien d'heures par jours utilisé vous les medias sociaux entre ; 0-2, 2-4, 4-6 et 6+ ?")
Q2 = input()
if Q2=="0-2":
    print("Wow, très bon, tu n'est pas attaché a ton telephone!")

elif Q2=="2-4":
    print("Ahh, 2-4 heures est un bon montant.")

elif Q2=="4-6":
    print("4-6 est assez normal de nos jours.")

elif Q2=="6+":
    print("Wow c'est beaucoup mais, durant la pandémie c'est correcte.")

print("Est-ce que vous avez accès a une console comme une PC, Playstation ou Xbox ou Non? Si Oui, quel utilise tu le plus?")
Q3 = input().lower()
if Q3=="pc":
    print("Moi aussi j'utilise un PC, c'est un outil très outil et il y a plusieurs jeux videos très bonnes et amusantes.")

elif Q3=="playstation":
    print("J'utilisais un Playstation il y a longtemps, c'est définitivement une bonne console avec des jeux très bonnes et amusantes.")

elif Q3=="xbox":
    print("Je n'ai jamais utilisé une Xbox mais, je sais que c'est une bonne console avec des jeux très bonnes et amusantes.")

elif Q3=="non":
    print("Wow, si tu peut un jour en avoir un, il est définitivement une bonne idée, personellement je recomande un PC mais son coût est plus élevé.")

print("Combien d'heures par jours utilisé vous un console entre ; 0-2, 2-4, 4-6, 6+ et Aucun Console?")
Q4 = input().lower()
if Q4=="0-2":
    print("Wow, très bon, tu n'est pas attaché a ton console!")

elif Q4=="2-4":
    print("Ahh, 2-4 heures est un bon montant.")

elif Q4=="4-6":
    print("4-6 est assez normale de nos jours.")

elif Q4=="6+":
    print("Wow c'est beaucoup mais, durant la pandémie c'est totalement normale.")

elif Q4=="aucun console":
    print("Ah oui...")

print("Merci pour avoir répondu au questionnaire, je l'apprecie.")
# Ceci est la fin du questionnaire, ceci ma donné plus d'info sur la technologie les personnes aime utilisé et combien de temps ils passent a les utilisés. 
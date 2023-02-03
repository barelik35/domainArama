import whois
domainList=[line.strip() for line in open('domainList.txt')]
bosDomainList = []
uzanti = ".net" # Domain uzantısı
basinaYazi = "" # Başına yazılacak kelime # Boş bırakabilirsiniz
sonunaYazi = "" # Sonuna yazılacak kelime # Boş bırakabilirsiniz
for domain in domainList:
    try:
        r10 = whois.whois(str(basinaYazi+domain+sonunaYazi+uzanti))
        print("Domain dolu, " + domain)
    except:
        print("Domain boş, " + domain)
        bosDomainList.insert(1,domain)
with open('bosDomainList.txt', 'w') as f:
    for i in bosDomainList:
        f.write(f"{i}\n")
      

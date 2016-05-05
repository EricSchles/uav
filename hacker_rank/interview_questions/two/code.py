def get_domains(line):
    not_all_found = True
    domains = []
    while not_all_found:
        domain = line.split("http://")[1].split("/")[0].split("?")[0].split("\\")[0].split('"')[0].split(" ")[0]
        domain = domain.replace("www.","")
        domain = domain.replace("ww2.","")
        domain = domain.replace("web.","")
        domain = domain.replace('") + "','')
        domains.append(domain)
        new_start_index = line.index(domain)
        try:
            line = line[new_start_index+len(domains[-1]):]
        except:
            not_all_found = False
    return domains

def  printDomains( arr):
    domains = []
    #doesn't account for multiple links per line, yet
    for line in arr:
        if "http://" in line: 
            domain = line.split("http://")[1].split("/")[0].split("?")[0].split("\\")[0].split('"')[0].split(" ")[0]
            
            
            domains.append(domain)
        elif "https://" in line:
            domain = line.split("https://")[1].split("/")[0].split("?")[0].split("\\")[0].split('"')[0].split(" ")[0]
            domain = domain.replace("www.","")
            domain = domain.replace("ww2.","")
            domain = domain.replace("web.","")
            domain = domain.replace('") + "','')
            domains.append(domain)
    domains = [elem for elem in list(set(domains)) if elem !='']
    domains.sort()
    #print ";".join(domains)

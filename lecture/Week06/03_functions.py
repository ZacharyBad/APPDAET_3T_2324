stations ={
    "lrt1"
    "lrt2"
    "mrt3": ["Taft", "Magallanes", "Ayala", "Buendia"]
}

def find_railway_network(destination: str):
    railway_networks = []
    for line in stations:
        if destination in stations[line]:
            railway_networks.append(line)


#unfinished code

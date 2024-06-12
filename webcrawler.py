def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        tags = soup.find("tbody").text
        tag = tags.split()
        male_total = 0
        female_total = 0
        for i in range(200):
            if i % 5 == 2:
                n = "".join(tag[i].split(","))
                male_total += int(n)
            if i % 5 == 4:
                n = "".join(tag[i].split(","))
                male_total += int(n)
                female_total += int(n)
        print(f"Male Number: {male_total}")
        print(f"Female Number: {female_total}")
      

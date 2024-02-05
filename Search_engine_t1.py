from os import system
def Find_match(text)->str:
    '''Function docstring here'''
    categories = ["Women's Closing",
                  "Women's Shoes",
                  "Women's Accessories",
                  "Women's Bag",
                  "Women's under wear",
                  "Man's Closing",
                  "Man's Shoes",
                  "Man's Bag",
                  "Man's Beach Shopping",
                  "Man's Watch & Accessory",
                  "Man's Underwear",
                  "Home & Kitchen",
                  "Bathroom",
                  "Home Decor",
                  "Baby",
                  "Girl's Child",
                  "Boy's Child",
                  "Baby Care",
                  "Baby toy",
                  "Baby Nutrition",
                  "Baby Transportation",
                  "Makeup",
                  "Skin Care",
                  "Hair Care",
                  "Personal Care",
                  "Perfume",
                  "Hair Styling Product",
                  "Makeup Accessories"]
    for category in categories :
        if category.lower() == text.lower():
            yield text
            return
    percents = []
    if ' ' in text :
        text = text.split()[0]
    for category in categories :
        c = 0
        if ' ' in category :
            for word in category.split():
                for j in range(len(word)):
                    try :
                        if word[j].lower() == text[j].lower():
                             c += 1
                    except :
                        continue
                prcnt = (c*100)/len(word)
                percents.append((prcnt,category))
                c = 0
        else :
            for i in range(len(category)) :
                try :
                    if category[i].lower() == text[i].lower():
                           c += 1
                except :
                    continue
            prcnt = (c*100)/len(category)
            percents.append((prcnt,category))
    percents = sorted(percents,reverse=True)
    full_match = [i[1] for i in percents if i[0]==100]
    if len(full_match)>0:
        for result in list(set(full_match)) :
            yield result
    else :
        non_zero = []
        for i in percents:
            if i[0]!=0 and i[1] not in non_zero:
                non_zero.append(i[1])
                yield i[1]
while ask:=input('Search something:'):
    system('cls')
    print(f'Result for {ask}\n-----------------------')
    for i in list(Find_match(ask)):
        print(i)
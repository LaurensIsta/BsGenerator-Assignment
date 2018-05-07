from random import randint


part1 = ["Het proces ","De factor mens ","De communicatie", "Het management ","De kerncompetentie ","Human capital ","De organisatie-ontwikkeling ","De missie ","Kennismanagement ","De eerste aanzet "]
part2 = ["moet meerwaarde leveren bij  ","stelt eisen aan ","dient te faciliteren bij ","is uitgangspunt bij ","Is onlosmakelijk verbonden met ","schept voorwaarden voor  ","dient te focussen op ","stuurt ","hangt nauw samen met ","moet een opstap bieden voor "]
part3 = ["de implementatie van ","de terugkoppeling van ","het aftimmeren van ","het aansturen van ","het aansturen van ","de ontwikkeling van ","de flexibilisering van ","de intergratie van ","de inventarisatie van ","de definitie van ","de insteek van "]
part4 = ["complexe ","optimale ","in elkaar grijpende","eenduidige ","onderling afhankelijke ","structurele ","pro-actieve ","resultaatgerichte ","efficiente ","consistente"]
part5 = ["supply chain processen ","business architecture ","mijlpalen ","targets ","business units ","organisatie-onderdelen ","scenario's ","best practices ","business models ","conceptplannen "]
part6 = ["waarbij het belang van ","waarbij de feedback van ","waarbij het kader voor ","waarbij afstemming met ","waarbij de structuur van ","waarbij de synergie met ","waarbij de interface met ","waarbij input van ","waarbij commitment van "," waarbij klankborden met "]
part7 = ["strategisch beleid ","de taskforce ","de communicatie ","de werkgroepen ","new business development ","de systeemintegratie ","de markt ","de stakeholders ","het management ","de projectorganisatie "]
part8 = ["moet uitkristalleren.","voorop staat.","wordt aangestuurd.","leading is.","toegevoegde waarde levert.","win-win situaties kan veroorzaken.","moet worden gemanaged.","voldoende draagvlak heeft.","doorslaggevend is.","cruciaal is."]
resultArray = ["","","","","","","",""]
loopPosition = 0

def PickRandInt():
    return randint(0,9)

## Dictionary approach may work better(?)

while loopPosition <9:
    pickedInt = PickRandInt()

    if loopPosition == 1:
        resultArray[0] = part1[pickedInt]
    if loopPosition == 2:
        resultArray[1] = part2[pickedInt]
    if loopPosition == 3:
        resultArray[2] = part3[pickedInt]    
    if loopPosition == 4:
        resultArray[3] = part4[pickedInt]
    if loopPosition == 5:
        resultArray[4] = part5[pickedInt]
    if loopPosition == 6:
        resultArray[5] = part6[pickedInt]
    if loopPosition == 7:
        resultArray[6] = part7[pickedInt]
    if loopPosition == 8:
        resultArray[7] = part8[pickedInt]

    loopPosition = loopPosition + 1

for x in resultArray:
    print (x)
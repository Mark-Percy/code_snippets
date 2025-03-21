binsover = {
    'red':{
        'everyWeeks': 2,
        'nextBinWeek': 1,
        'lastWeek': null,
        'weeks' : []
    },
    'blue': {
        'everyWeeks': 3,
        'nextBinWeek': 12,
        'lastWeek': 48,
        'weeks' : []
    },
    'Grey': {
        'everyWeeks': 2,
        'nextBinWeek': 2,
        'lastWeek': null,
        'weeks' : []
    }
}

binWeeks(binsover)

colDay = 3

startDate = getFirstGivenDay(colDay)
currWeek = 1
while(startDate.getFullYear() == new Date().getFullYear()) {
    
    binsForWeek = getBinsForCurrWeek(currWeek, binsover)
    console.log(`${startDate.getDate()}/${startDate.getMonth()} bins: ${binsForWeek}`)

    startDate.setDate(startDate.getDate()+7)
    currWeek ++
    
}

function getFirstGivenDay(givenDay) {
    currDate = new Date()
    firstDateOfYear = new Date(`${currDate.getFullYear()}-01-01`)
    dayOfWeek = firstDateOfYear.getDay()
    diff = (givenDay - dayOfWeek) 
    if(diff < 0) {diff = 7 + diff}
    firstDateOfYear.setDate(firstDateOfYear.getDate() + diff)
    return firstDateOfYear
}

function binWeeks(bins) {
    yeart = 2025;
    date = new Date(Date.UTC(yeart,0,1))
    numDays = 7
    count = 0

    while(date.getFullYear() == yeart) {
        count ++ 
        for(bin in bins) {
            if(bins[bin]['nextBinWeek'] == count && (bins[bin]['lastWeek'] == null || bins[bin]['lastWeek'] > count)){
                bins[bin]['nextBinWeek'] += bins[bin]['everyWeeks']
                bins[bin]['weeks'].push(count)
            }
        }
        date.setDate(date.getDate()+numDays)
    }
}

function getBinsForCurrWeek(currWeek, bins) {
    binList = []
    console.log(currWeek)
    for(bin in bins){
        if(bins[bin]['weeks'].includes(currWeek)) {
            binList.push(bin)
        }
    }
    return binList
}
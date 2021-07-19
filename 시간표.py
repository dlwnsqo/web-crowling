import requests
from bs4 import BeautifulSoup

def get_lectures(divs):
    lectures = []

    for i in range(len(divs)):
        links1 = divs[i].findAll('td', {'class': 'th5'})

        for link in links1:
            lecture = link.text
            lectures.append(lecture)

    return lectures

def get_times(divs):
    times = []

    for i in range(len(divs)):
        links = divs[i].findAll('td', {'class': 'th10'})

        for link in links:
            time = link.text
            times.append(time)

    return times

def get_rooms(divs):
    rooms = []

    for i in range(len(divs)):
        links = divs[i].findAll('td', {'class': 'th11'})

        for link in links:
            room = link.text
            rooms.append(room)

    return rooms

arr = [[0 for i in range(19)]for j in range(30)]
arr[0] = ['11','1108','1101','110B','1104','110J','1103','1106','1102','1109','1105','1107','110A']#인문대학
arr[1] = ['12','120B','120A','1204','1209','120902','120901','1202','1207','120C','1205','1201','1203']#사회과학대학
arr[2] = ['13','130A','130705','130701','1301','130Q','130Q01','130Q02','130Q03','1304','1302']#자연과학대학
arr[3] = ['14','1403','1403001','1403002','1403003','1404','1407']#경상대학
arr[4] = ['15','1508','1502']#법학대학
arr[5] = ['16','160I01','160I02','1605','16','1601001','1601002','1601003','160101','160102','1607','1609001','1609002','160903','160904','1611','161101','161102','1612001','1612002','161201','161202','160E','1606']#공과대학
arr[6] = ['17','170R','170A','170T','170T01','170T02','170Q','170X','170S','170S02','170S01','170S03','170V','170U','170P','170P01','170P02','170P03','170O','170W','170B','170B01','170B05','170B04']#농업생명과학대학
arr[7] = ['19','191G','191H','190A','190B','1901','1902','190H','19','190J','1908','190E','1903','190D01','190D02','1907','190G','190K','190F','190C','190I']#사범대학
arr[8] = ['18','1803','1806','1804','1801']#예술대학
arr[9] = ['1F','1F04','1F01']#의과대학
arr[10] = ['1G','1G02','1G01']#치과대학
arr[11] = ['1A','1A02','1A01']#수의과대학
arr[12] = ['1B','IB04','IB07','IB0701','1B0702','1B03']#생명과학대학
arr[13] = ['1E','IE01','IE02']#자율전공부
arr[14] = ['1C','1C01']#간호대학
arr[15] = ['1O','1O07','1O09','IO06','1O03','1O01','1O01001','1O01002','1O01003','1O01004','1O01005','1O01006','1O01007','1O0101','1O02','1O0204','1O0206','1O0205','1O08']#IT대학
arr[16] = ['1Q','1Q01']#약학대학
arr[17] = ['1S','1S01', '1S0101','1S0102']#행정학부
arr[18] = ['1T','1T0103','1T0104','1T0102','1T0101']#융합학부

for i in range(19):
    for j in range(len(arr[i])):
        req = requests.get('http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_open_crse_cde=' + arr[i][j] + '&sub=' + arr[i][0] + '&search_open_yr_trm=20212')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.findAll('table', {'class': 'courTable'})

        lectures = get_lectures(divs)  
        times = get_times(divs)
        rooms = get_rooms(divs)

        for k in range(len(rooms)):
            print(lectures[k]+ ' ' + times[k] + ' ' + rooms[k])
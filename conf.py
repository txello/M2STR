def word():
    words_EN = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26', 'a':'27','b':'28','c':'29','d':'30','e':'31','f':'32','g':'33','h':'34','i':'35','j':'36','k':'37','l':'38','m':'39','n':'40','o':'41','p':'42','q':'43','r':'44','s':'45','t':'46','u':'47','v':'48','w':'49','x':'50','y':'51','z':'52'}
    words_1 = {'1':'53','2':'54','3':'55','4':'56','5':'57','6':'58','7':'59','8':'60','9':'61','0':'62'}
    words_RU = {'А':'63','Б':'64','В':'65','Г':'66','Д':'67','Е':'68','Ё':'69','Ж':'70','З':'71','И':'72','Й':'73','К':'74','Л':'75','М':'76','Н':'77','О':'78','П':'79','Р':'80','С':'81','Т':'82','У':'83','Ф':'84','Х':'85','Ц':'86','Ч':'87','Ш':'88','Щ':'89','Ъ':'90','Ы':'91','Ь':'92','Э':'93','Ю':'94','Я':'95','а':'96','б':'97','в':'98','г':'99','д':'100','е':'101','ё':'102','ж':'103','з':'104','и':'105','й':'106','к':'107','л':'108','м':'109','н':'110','о':'111','п':'112','р':'113','с':'114','т':'115','у':'116','ф':'117','х':'118','ц':'119','ч':'120','ш':'121','щ':'122','ъ':'123','ы':'124','ь':'125','э':'126','ю':'127','я':'128'}
    words_sp = {'!':'129', ' ':'130', "\'":'132', '.':'133',',':'134', ':':'135', '?':'136',"\"":'137', '@':'138','#':'139','$':'140','%':'141','^':'142','&':'143','*':'144','(':'145',')':'146','-':'147','+':'148','=':'149','_':'150',';':'151','№':'152','\\':'153','/':'154','|':'155','~':'156','`':'157','[':'158',']':'159','{':'160','}':'161','<':'162','>':'163'}
    words_EN.update(words_1)
    words_EN.update(words_RU)
    words_EN.update(words_sp)
    return words_EN
def salt():
    salt = "change me"
    return salt
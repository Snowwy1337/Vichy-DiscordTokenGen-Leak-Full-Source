# please hcap patch this, match every curse moove to ban the same..

import datetime, toml

__config__ = toml.loads(open('../config/config.toml', 'r+').read())

def get_motion_data():
    st = round(datetime.datetime.now().timestamp())

    if __config__['browser']['browser_id'] == 1:
        return "{\"st\":1657336724477,\"dct\":1657336724477,\"mm\":[[43,381,1657336724668],[91,332,1657336724692],[114,293,1657336724708],[132,261,1657336724725],[141,248,1657336724742],[136,244,1657336725009],[129,240,1657336725025],[124,235,1657336725042],[122,232,1657336725059],[122,229,1657336725075],[123,226,1657336725092],[123,220,1657336725109],[123,211,1657336725125],[119,199,1657336725142],[114,187,1657336725159],[111,177,1657336725175],[110,169,1657336725192],[110,163,1657336725208],[110,157,1657336725226],[110,153,1657336725242],[111,151,1657336725259],[112,151,1657336725275],[118,253,1657336725859],[128,253,1657336725875],[139,253,1657336725892],[152,251,1657336725908],[171,245,1657336725926],[192,237,1657336725942],[205,231,1657336725959],[216,225,1657336725976],[219,221,1657336725992],[220,218,1657336726009],[219,215,1657336726025],[214,210,1657336726043],[205,203,1657336726076],[205,202,1657336726092],[204,202,1657336726109],[205,202,1657336726242],[212,205,1657336726259],[225,208,1657336726275],[242,209,1657336726292],[258,210,1657336726309],[275,210,1657336726325],[291,210,1657336726342],[306,209,1657336726358],[320,206,1657336726375],[331,203,1657336726392],[338,199,1657336726408],[342,197,1657336726425],[343,196,1657336726442],[344,195,1657336726458],[344,194,1657336726476],[339,196,1657336726625],[328,203,1657336726642],[313,211,1657336726658],[292,223,1657336726675],[263,238,1657336726692],[235,254,1657336726709],[201,273,1657336726725],[168,288,1657336726742],[138,298,1657336726759],[115,305,1657336726775],[95,312,1657336726792],[85,316,1657336726809],[81,319,1657336726826],[81,321,1657336727109],[86,325,1657336727126],[94,331,1657336727142],[102,338,1657336727159],[113,348,1657336727175],[127,357,1657336727192],[146,365,1657336727209],[168,372,1657336727225],[194,378,1657336727242],[218,382,1657336727259],[241,387,1657336727276],[257,391,1657336727292],[268,394,1657336727308],[274,396,1657336727325],[276,396,1657336727342],[278,397,1657336727359],[277,398,1657336727576],[276,398,1657336727592],[273,398,1657336727609],[268,398,1657336727626],[259,393,1657336727642],[246,383,1657336727659],[227,366,1657336727675],[205,341,1657336727692],[187,315,1657336727709],[173,290,1657336727725],[161,267,1657336727742],[153,248,1657336727758],[145,229,1657336727776],[137,215,1657336727792],[130,204,1657336727809],[125,198,1657336727825],[124,197,1657336727842],[122,197,1657336727959],[120,197,1657336727975],[117,197,1657336727992],[111,198,1657336728008],[105,201,1657336728026],[100,205,1657336728042],[96,210,1657336728058],[93,217,1657336728076],[92,231,1657336728092],[94,253,1657336728108],[103,282,1657336728126],[117,309,1657336728142],[133,330,1657336728158],[155,347,1657336728175],[178,356,1657336728192],[198,358,1657336728209],[213,360,1657336728225],[222,360,1657336728242],[224,360,1657336728259],[225,360,1657336728276],[221,362,1657336728375],[214,365,1657336728392],[205,369,1657336728408],[192,375,1657336728425],[173,386,1657336728442],[153,400,1657336728459],[132,421,1657336728476],[111,444,1657336728492],[95,460,1657336728508],[85,474,1657336728525],[83,486,1657336728542],[86,494,1657336728559],[95,500,1657336728575],[111,504,1657336728592],[129,508,1657336728609],[151,510,1657336728625],[177,511,1657336728642],[203,511,1657336728658],[231,507,1657336728676],[255,502,1657336728692],[273,499,1657336728709],[286,495,1657336728725],[294,494,1657336728742],[299,493,1657336728759],[302,493,1657336728776],[303,493,1657336728858],[305,494,1657336728875],[308,495,1657336728892],[311,496,1657336728909],[313,497,1657336728925],[314,497,1657336728942],[315,498,1657336728959],[316,499,1657336728992],[319,500,1657336729009],[321,503,1657336729026],[324,506,1657336729042],[328,510,1657336729059],[332,515,1657336729076],[334,520,1657336729092],[335,524,1657336729109],[336,529,1657336729125],[336,535,1657336729142],[335,540,1657336729159],[333,544,1657336729175],[332,548,1657336729192],[330,551,1657336729209],[330,554,1657336729225],[329,557,1657336729242],[329,559,1657336729259],[329,562,1657336729275],[329,563,1657336729292],[328,566,1657336729309],[328,567,1657336729325],[328,568,1657336729358],[328,567,1657336729559],[326,562,1657336729575],[326,551,1657336729592],[327,534,1657336729608],[330,509,1657336729625],[335,483,1657336729642],[341,460,1657336729659],[348,444,1657336729675],[353,430,1657336729692],[357,419,1657336729709],[357,406,1657336729726],[357,390,1657336729742],[353,370,1657336729759],[344,337,1657336729776],[330,303,1657336729792],[313,270,1657336729808],[293,239,1657336729825],[273,217,1657336729842],[252,201,1657336729859],[228,191,1657336729876],[200,185,1657336729892],[173,185,1657336729908],[142,185,1657336729926],[112,188,1657336729942],[89,192,1657336729959],[68,199,1657336729975],[52,206,1657336729992],[44,211,1657336730009],[41,215,1657336730025],[41,222,1657336730042],[50,233,1657336730059],[68,252,1657336730075],[89,273,1657336730092],[108,293,1657336730109],[127,314,1657336730126],[150,339,1657336730142],[175,364,1657336730158],[203,387,1657336730175],[230,403,1657336730192],[253,410,1657336730208],[271,413,1657336730225],[280,414,1657336730242],[287,415,1657336730258],[291,416,1657336730276],[295,418,1657336730292],[298,420,1657336730309],[301,424,1657336730325],[304,431,1657336730342],[306,440,1657336730359],[309,453,1657336730376],[317,489,1657336730409],[322,506,1657336730425],[325,518,1657336730443],[332,530,1657336730475],[335,534,1657336730492],[338,537,1657336730508],[341,539,1657336730526],[345,539,1657336730542],[350,539,1657336730558],[354,537,1657336730575],[357,530,1657336730592],[358,518,1657336730609],[358,496,1657336730625],[353,462,1657336730642],[345,420,1657336730658],[330,380,1657336730675],[315,348,1657336730692],[305,327,1657336730709],[301,317,1657336730725],[301,316,1657336730742],[302,320,1657336730808],[306,332,1657336730826],[314,352,1657336730842],[325,376,1657336730859],[337,403,1657336730875],[347,426,1657336730892],[352,442,1657336730908],[353,455,1657336730925],[353,469,1657336730942],[353,483,1657336730959],[350,494,1657336730975],[346,501,1657336730992],[342,507,1657336731009],[339,513,1657336731026],[338,519,1657336731042],[337,525,1657336731058],[337,530,1657336731075],[337,534,1657336731092],[338,538,1657336731109],[338,540,1657336731126],[339,541,1657336731142],[339,542,1657336731159],[340,542,1657336731176],[340,543,1657336731192],[341,546,1657336731209],[341,549,1657336731225],[343,553,1657336731242],[344,557,1657336731259],[345,560,1657336731275],[345,561,1657336731292],[346,561,1657336731309],[346,562,1657336731342]],\"mm-mp\":24.09386281588448,\"md\":[[204,202,1657336726125],[344,194,1657336726552],[81,319,1657336726962],[346,562,1657336731365]],\"md-mp\":1746.6666666666667,\"mu\":[[204,202,1657336726199],[344,194,1657336726600],[81,319,1657336727035],[346,562,1657336731420]],\"mu-mp\":1740.3333333333333,\"topLevel\":{\"st\":1657336722184,\"sc\":{\"availWidth\":1920,\"availHeight\":1040,\"width\":1920,\"height\":1080,\"colorDepth\":24,\"pixelDepth\":24,\"top\":0,\"left\":0,\"availTop\":0,\"availLeft\":0,\"mozOrientation\":\"landscape-primary\",\"onmozorientationchange\":null},\"nv\":{\"permissions\":{},\"pdfViewerEnabled\":true,\"doNotTrack\":\"1\",\"maxTouchPoints\":0,\"mediaCapabilities\":{},\"oscpu\":\"Windows NT 10.0; Win64; x64\",\"vendor\":\"\",\"vendorSub\":\"\",\"productSub\":\"20100101\",\"cookieEnabled\":true,\"buildID\":\"20181001000000\",\"mediaDevices\":{},\"serviceWorker\":{},\"credentials\":{},\"clipboard\":{},\"mediaSession\":{},\"webdriver\":false,\"hardwareConcurrency\":16,\"geolocation\":{},\"appCodeName\":\"Mozilla\",\"appName\":\"Netscape\",\"appVersion\":\"5.0 (Windows)\",\"platform\":\"Win32\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0\",\"product\":\"Gecko\",\"language\":\"fr\",\"languages\":[\"fr\",\"fr-FR\",\"en-US\",\"en\"],\"locks\":{},\"onLine\":true,\"storage\":{},\"plugins\":[\"internal-pdf-viewer\",\"internal-pdf-viewer\",\"internal-pdf-viewer\",\"internal-pdf-viewer\",\"internal-pdf-viewer\"]},\"dr\":\"\",\"inv\":false,\"exec\":false,\"wn\":[[1446,741,1,1657336722185]],\"wn-mp\":0,\"xy\":[[0,0,1,1657336722185],[0,92,1,1657336724525],[0,91,1,1657336724542],[0,92,1,1657336725526],[0,93,1,1657336725542],[0,99,1,1657336725559],[0,109,1,1657336725575],[0,121,1,1657336725594],[0,146,1,1657336725626],[0,158,1,1657336725642],[0,169,1,1657336725660],[0,186,1,1657336725693],[0,191,1,1657336725709],[0,193,1,1657336725726]],\"xy-mp\":236.0666666666667,\"mm\":[[1102,331,1657336723458],[1030,373,1657336723476],[970,402,1657336723492],[924,417,1657336723509],[882,426,1657336723525],[846,431,1657336723542],[822,432,1657336723558],[801,429,1657336723575],[787,422,1657336723592],[775,415,1657336723609],[767,407,1657336723625],[761,404,1657336723642],[760,403,1657336723659],[752,408,1657336723792],[743,415,1657336723809],[733,426,1657336723825],[720,436,1657336723842],[704,449,1657336723859],[686,464,1657336723875],[669,479,1657336723892],[656,490,1657336723908],[648,499,1657336723925],[641,505,1657336723942],[589,653,1657336724609],[602,654,1657336724625],[622,652,1657336724642]],\"mm-mp\":44,\"md\":[[760,403,1657336723683]],\"md-mp\":0,\"mu\":[[760,403,1657336723752]],\"mu-mp\":0},\"v\":1}".replace('1657336', str(st)[:7]) if __config__['advanced']['firefox_motion_data'] == "" else __config__['advanced']['firefox_motion_data'].replace(__config__['advanced']['motion_data_unix_time'], str(st)[:7])
    else:
        return "{\"st\":1657447885282,\"dct\":1657447885282,\"mm\":[[20,231,1657447885350],[18,230,1657447885473],[15,229,1657447885530],[16,229,1657447886071],[21,225,1657447886089],[33,220,1657447886105],[53,214,1657447886121],[83,208,1657447886137],[125,207,1657447886153],[174,209,1657447886169],[224,217,1657447886185],[275,230,1657447886201],[316,247,1657447886217],[343,266,1657447886233],[353,281,1657447886249],[352,293,1657447886265],[340,304,1657447886281],[314,315,1657447886297],[279,323,1657447886313],[236,326,1657447886329],[187,324,1657447886345],[139,315,1657447886361],[97,305,1657447886377],[64,292,1657447886393],[42,281,1657447886409],[29,269,1657447886425],[25,260,1657447886441],[24,250,1657447886457],[25,242,1657447886474],[26,236,1657447886491],[27,231,1657447886508],[29,226,1657447886524],[30,219,1657447886542],[30,212,1657447886561],[31,206,1657447886580],[32,202,1657447886600],[33,199,1657447886625],[35,198,1657447886645],[37,194,1657447886665],[39,191,1657447886683],[41,189,1657447886702],[42,190,1657447886819],[39,197,1657447886835],[34,211,1657447886852],[33,227,1657447886868],[37,244,1657447886884],[48,259,1657447886901],[66,270,1657447886917],[94,276,1657447886933],[129,280,1657447886949],[171,281,1657447886965],[214,277,1657447886981],[258,271,1657447886997],[292,263,1657447887013],[316,254,1657447887030],[329,246,1657447887046],[333,238,1657447887064],[334,232,1657447887081],[334,227,1657447887099],[334,222,1657447887119],[335,219,1657447887135],[335,216,1657447887152],[336,214,1657447887169],[337,211,1657447887189],[338,208,1657447887209],[339,205,1657447887226],[341,202,1657447887242],[343,199,1657447887261],[343,195,1657447887278],[344,192,1657447887297],[345,190,1657447887322],[345,191,1657447887453],[341,200,1657447887469],[336,213,1657447887485],[330,232,1657447887501],[324,249,1657447887517],[321,263,1657447887533],[319,275,1657447887549],[319,282,1657447887565],[320,288,1657447887581],[323,293,1657447887597],[326,297,1657447887614],[328,300,1657447887631],[330,303,1657447887650],[334,304,1657447887673],[337,306,1657447887692],[340,306,1657447887710],[342,306,1657447887728],[342,307,1657447887839],[337,308,1657447887855],[326,312,1657447887872],[313,314,1657447887888],[297,317,1657447887904],[283,318,1657447887920],[270,321,1657447887937],[259,323,1657447887954],[249,325,1657447887970],[240,326,1657447887987],[231,327,1657447888003],[222,328,1657447888019],[213,328,1657447888035],[204,328,1657447888051],[197,328,1657447888067],[188,328,1657447888085],[179,328,1657447888101],[169,327,1657447888117],[158,327,1657447888134],[147,327,1657447888150],[137,326,1657447888166],[125,325,1657447888183],[113,323,1657447888200],[102,321,1657447888216],[92,318,1657447888232],[84,315,1657447888249],[77,313,1657447888267],[72,312,1657447888287],[73,313,1657447888480],[79,317,1657447888496],[89,320,1657447888513],[103,322,1657447888529],[120,324,1657447888545],[138,326,1657447888561],[153,326,1657447888577],[166,326,1657447888593],[176,326,1657447888609],[183,325,1657447888626],[187,323,1657447888645],[189,321,1657447888661],[191,318,1657447888677],[192,315,1657447888694],[193,313,1657447888713],[192,313,1657447888901],[188,317,1657447888917],[183,322,1657447888933],[179,333,1657447888950],[176,344,1657447888967],[175,356,1657447888983],[179,368,1657447889000],[186,379,1657447889016],[197,389,1657447889032],[211,398,1657447889048],[226,406,1657447889064],[237,411,1657447889080],[247,416,1657447889097],[254,420,1657447889114],[258,423,1657447889130],[260,425,1657447889146],[260,427,1657447889169],[257,430,1657447889188],[251,433,1657447889204],[243,436,1657447889220],[231,439,1657447889237],[216,444,1657447889253],[195,449,1657447889269],[174,452,1657447889285],[155,454,1657447889301],[138,455,1657447889317],[125,455,1657447889333],[116,456,1657447889350],[112,456,1657447889407],[109,456,1657447889424],[104,456,1657447889440],[98,455,1657447889456],[91,453,1657447889474],[87,452,1657447889493],[87,451,1657447889656],[92,451,1657447889672],[106,451,1657447889689],[125,451,1657447889705],[147,451,1657447889721],[171,452,1657447889738],[192,454,1657447889754],[208,455,1657447889770],[220,455,1657447889787],[225,455,1657447889803],[226,454,1657447889845],[226,455,1657447890206],[227,458,1657447890222],[228,464,1657447890238],[233,472,1657447890254],[242,483,1657447890270],[255,494,1657447890286],[270,505,1657447890302],[283,512,1657447890318],[293,518,1657447890334],[300,521,1657447890351],[305,522,1657447890409],[306,523,1657447890425],[309,525,1657447890442],[312,527,1657447890459],[315,530,1657447890478],[317,533,1657447890494],[320,536,1657447890512],[323,539,1657447890528],[324,543,1657447890546],[327,546,1657447890564],[328,550,1657447890580],[329,552,1657447890596],[332,554,1657447890614],[333,557,1657447890647]],\"mm-mp\":2.939511653718089,\"md\":[[42,189,1657447886745],[345,190,1657447887364],[342,306,1657447887754],[72,312,1657447888366],[193,312,1657447888802],[86,451,1657447889535],[226,454,1657447890121],[333,557,1657447890656]],\"md-mp\":558.7142857142857,\"mu\":[[42,190,1657447886819],[345,190,1657447887444],[342,306,1657447887822],[72,312,1657447888435],[193,312,1657447888864],[86,451,1657447889603],[226,454,1657447890182],[333,557,1657447890720]],\"mu-mp\":557.2857142857143,\"topLevel\":{\"st\":1657447570100,\"sc\":{\"availWidth\":1920,\"availHeight\":1040,\"width\":1920,\"height\":1080,\"colorDepth\":24,\"pixelDepth\":24,\"availLeft\":0,\"availTop\":0},\"nv\":{\"vendorSub\":\"\",\"productSub\":\"20030107\",\"vendor\":\"Google Inc.\",\"maxTouchPoints\":0,\"userActivation\":{},\"doNotTrack\":null,\"geolocation\":{},\"connection\":{},\"webkitTemporaryStorage\":{},\"webkitPersistentStorage\":{},\"hardwareConcurrency\":16,\"cookieEnabled\":true,\"appCodeName\":\"Mozilla\",\"appName\":\"Netscape\",\"appVersion\":\"5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9005 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36\",\"platform\":\"Win32\",\"product\":\"Gecko\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9005 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36\",\"language\":\"fr\",\"languages\":[\"fr\",\"fr-FR\"],\"onLine\":true,\"webdriver\":false,\"serial\":{},\"scheduling\":{},\"mediaCapabilities\":{},\"permissions\":{},\"locks\":{},\"usb\":{},\"mediaSession\":{},\"clipboard\":{},\"credentials\":{},\"keyboard\":{},\"mediaDevices\":{},\"storage\":{},\"serviceWorker\":{},\"wakeLock\":{},\"deviceMemory\":8,\"hid\":{},\"presentation\":{},\"xr\":{},\"userAgentData\":{},\"bluetooth\":{},\"managed\":{},\"plugins\":[\"internal-pdf-viewer\",\"mhjfbmdgcfjbbpaeojofohoefgiehjai\"]},\"dr\":\"\",\"inv\":false,\"exec\":false,\"wn\":[],\"wn-mp\":0,\"xy\":[],\"xy-mp\":0,\"mm\":[[914,1038,1657447879251],[928,607,1657447882358],[879,606,1657447882374],[837,605,1657447882390],[793,605,1657447882406],[752,605,1657447882422],[719,605,1657447882438],[688,607,1657447882454],[660,612,1657447882470],[633,619,1657447882486],[616,626,1657447882613],[638,624,1657447882629],[676,621,1657447882645],[723,619,1657447882661],[774,615,1657447882677],[830,610,1657447882693],[884,602,1657447882709],[927,565,1657447883199],[876,567,1657447883215],[816,569,1657447883231],[748,569,1657447883247],[687,569,1657447883263],[626,569,1657447883279],[574,569,1657447883295],[526,576,1657447883311],[488,585,1657447883327],[464,592,1657447883344],[452,598,1657447883361],[445,600,1657447883378],[442,603,1657447883394],[441,604,1657447883412],[390,682,1657447883897],[425,701,1657447883913],[465,719,1657447883929],[514,741,1657447883945],[561,758,1657447883961],[601,769,1657447883977],[637,776,1657447883993],[661,778,1657447884009],[674,778,1657447884025],[677,778,1657447884527],[672,778,1657447884543],[662,781,1657447884559],[649,784,1657447884575],[631,788,1657447884591],[609,789,1657447884608],[585,790,1657447884624],[558,790,1657447884640],[525,788,1657447884656],[493,783,1657447884672],[455,774,1657447884688],[418,760,1657447884704],[384,740,1657447884720],[351,709,1657447884736],[312,650,1657447884764],[307,624,1657447884780],[313,606,1657447884796],[336,591,1657447884812],[369,584,1657447884828],[388,582,1657447885071],[388,581,1657447885091],[391,581,1657447885113],[393,581,1657447885192],[392,580,1657447885275],[391,580,1657447885297],[391,579,1657447885349]],\"mm-mp\":7.429422066549915,\"md\":[],\"md-mp\":1811,\"mu\":[],\"mu-mp\":1769,\"lpt\":1657447696950},\"v\":1}".replace('1657447', str(st)[:7]) if __config__['advanced']['chrome_motion_data'] == "" else __config__['advanced']['chrome_motion_data'].replace(__config__['advanced']['motion_data_unix_time'], str(st)[:7])
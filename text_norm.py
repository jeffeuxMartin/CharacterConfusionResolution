import time
import unicodedata

def string_checker(string: str):
    for char in string:
        print_msg = (char, 
            "%7d" % ord(char), 
            "-->",
            (ok_char := unicodedata.normalize(
                "NFKD", char)), 
            "%7d" % (ok_ord := ord(ok_char)))
        # 非常用字範圍
        COLOR_begin, COLOR_termi = (("", "") 
            if 19968 <= ok_ord <= 40943 else
            ("\033[01;33m", "\033[0m"))
        print(
            f"{COLOR_begin}{print_msg}{COLOR_termi}")
            
def normalizer(char, standard="NFKD"):
    norm = unicodedata.normalize(standard, char)
    
    return (
        char != norm,
        (char, ord(char), 19968 <= ord(char) <= 40943),
        (norm, ord(norm), 19968 <= ord(norm) <= 40943),
    )


def string_checker__v2(string: str):
    for char in string:
        status, before, after = normalizer(char)
    
        bc, bo, br = before
        ac, ao, ar = after
        assert not ((br == True) and (ar == False))
        
        if br == False:
            print_msg = f"{bc} {bo:7d} --> {ac} {ao:7d}"
            # 非常用字範圍
            COLOR_begin, COLOR_termi = (
                ("\033[01;33m", "\033[0m")
                if ((br == False) and (ar == False)) else
                ("", ""))
            print(
                f"{COLOR_begin}{print_msg}{COLOR_termi}")
     
print("check col 1...")

string_checker__v2(col1 := "廾韮呀哇嗮葱俾啵裡尐檯菰咯囡荳蕃㩒鷄綫峯羣脉牀笋麪臺滙啓恒茘耻栢覇桿菓濶尅强烟厰厦竪鵰鉤刦册駡閑凼豔粧确唉姪脣劵喐潷㧾涷瓹拑箝䄛摟鮓爲岀卟歳増樖舖窑窰碍掀揾黄鲩説踭敎痹㖩减喞戏幢㒼妳瀄週吋呎紮迹摷脱哂顔鬰噜麽内䔨杮櫈蕌藠拮炳抦税温卐寛甙躰帰戦藴稲眞専郷駄険靭瑠吡栐歩圑絶舗冨鮎渋脇浜雑瀞塩苄権扌桜恵発寜吿絵込乗啉覻亜撃処处晄栃辧醖掦姉産竜姸図薫沢蔵徳紥晳腈兪妸誔喆抜転辺楽昰飈滝歴団鬪蝽踳柾隠裵貎曺勑莾竈暦廻曯矚戸户晩毎髪剣実兎臓県吲翆焼爕売瀬邉涙斎槇覧遡奬殻犠糭躱麺黒湼晧顕艶鉄凖観擕徴気頴嶋抺硏篭廏亁犇怇姫駅閲鎭鎹擤凑篋揜銊抰戙愩屘睺熝錑更不利料聯行立年來")

print("\ncheck col 2?")
time.sleep(1)

string_checker__v2(col2 := "廿韭啊嘩晒蔥畀噃裏啲枱菇囉女豆番撳雞線峰群脈床筍麵台匯啟恆荔恥柏霸杆果闊剋強煙廠廈豎雕鈎劫冊罵閒氹艷妝確哎侄唇券郁𢳂𢳂凍捐鉗鉗褸褸渣為出吓歲增棵鋪窯窯礙㨴搵黃鯇說㬹教痺噉減唧戲棟萌你擳周寸尺扎跡耖脫晒顏鬱嚕麼內蕹柿凳蕎蕎㓤丙丙稅溫卍寬䣧體歸戰蘊稻真專鄉馱險韌琉諀柡步團絕舖富鯰涉脅濱雜淨鹽芐權手櫻惠發寧告繪迂乘婪覷亞擊處處晃櫔辦醞揚姊產龍妍圖薰澤藏德紮晰睛俞婀誕哲拔轉邊樂是飆瀧歷團鬥椿蝽柩隱裴貌曹敕莽灶曆迴囑囑戶戶晚每髮劍實兔臟縣哂翠燒燮賣瀨邊淚齋槙覽溯獎殼犧粽躲麵黑涅皓顯艷鐵準觀㩦徵氣穎島抹研籠廄乾奔佢姬驛閱鎮餸呻湊喼揞戌揚棟貢尾吼淥𨀤更不利料聯行立年來")

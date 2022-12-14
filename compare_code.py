import editdistance
# editdistance.eval('banana', 'bahama')
import json
with open('full_zh_charset.json') as f:
    lookup = json.load(f)

def mean(s):
    return sum(s) / len(s)

def compare_proto(v1, v2):
    v1 = repr(v1) if isinstance(v1, str) else v1
    v2 = repr(v2) if isinstance(v2, str) else v2
    return (
        f'compare({v1}, {v2})'
    )

def compare(v1, v2):
    v1 = [v1] if isinstance(v1, str) else v1
    v2 = [v2] if isinstance(v2, str) else v2
    distances = ([editdistance.eval(vv1, vv2)
        for vv1 in v1 for vv2 in v2])
    return min(distances)

def compare_samples(sample1, sample2, verbose=False):
    verbolizer = print if verbose else lambda *x: None
    
    verbolizer('\033[01;32m'
        f"Compare {sample1} and {sample2}..."'\033[0m')
    code1 = lookup.get(sample1)
    code2 = lookup.get(sample2)
    if code1 is not None and code2 is not None:
        verbolizer('\033[01;31m'"Compare in Audio..."'\033[0m')
        audio1 = code1['audio']
        audio2 = code2['audio']

        audio_distance_coding = [
            compare(audio1[k], audio2[k]) 
            for k in audio1 if k in audio2]
        audio_distance = mean(audio_distance_coding)
        verbolizer(f"Audio distance = {audio_distance}")

        verbolizer('\033[01;31m'"Compare in Visual..."'\033[0m')
        visual1 = code1['visual']
        visual2 = code2['visual']

        visual_distance_coding = [
            compare(visual1[k], visual2[k]) 
            for k in visual1 if k in visual2]
        visual_distance = mean(visual_distance_coding)        
        verbolizer(f"Visual distance = {visual_distance}")
        return dict(audio=audio_distance, visual=visual_distance)
    return dict(audio=99999, visual=99999)

# compare_samples('妳', '你')



f = open('compared_different_writing.tsv', 'w')
def compare_samples_better(a, b):
    compare_samples_res = compare_samples(a, b)
    print(a, b, 
        compare_samples_res['audio'],
        compare_samples_res['visual'],
    sep='\t', file=f)
compare_samples_better("廾", "廿")
compare_samples_better("韮", "韭")
compare_samples_better("呀", "啊")
compare_samples_better("哇", "嘩")
compare_samples_better("嗮", "晒")
compare_samples_better("葱", "蔥")
compare_samples_better("俾", "畀")
compare_samples_better("啵", "噃")
compare_samples_better("裡", "裏")
compare_samples_better("尐", "啲")
compare_samples_better("檯", "枱")
compare_samples_better("菰", "菇")
compare_samples_better("咯", "囉")
compare_samples_better("囡", "女")
compare_samples_better("荳", "豆")
compare_samples_better("蕃", "番")
compare_samples_better("㩒", "撳")
compare_samples_better("鷄", "雞")
compare_samples_better("綫", "線")
compare_samples_better("峯", "峰")
compare_samples_better("羣", "群")
compare_samples_better("脉", "脈")
compare_samples_better("牀", "床")
compare_samples_better("笋", "筍")
compare_samples_better("麪", "麵")
compare_samples_better("臺", "台")
compare_samples_better("滙", "匯")
compare_samples_better("啓", "啟")
compare_samples_better("恒", "恆")
compare_samples_better("茘", "荔")
compare_samples_better("耻", "恥")
compare_samples_better("栢", "柏")
compare_samples_better("覇", "霸")
compare_samples_better("桿", "杆")
compare_samples_better("菓", "果")
compare_samples_better("濶", "闊")
compare_samples_better("尅", "剋")
compare_samples_better("强", "強")
compare_samples_better("烟", "煙")
compare_samples_better("厰", "廠")
compare_samples_better("厦", "廈")
compare_samples_better("竪", "豎")
compare_samples_better("鵰", "雕")
compare_samples_better("鉤", "鈎")
compare_samples_better("刦", "劫")
compare_samples_better("册", "冊")
compare_samples_better("駡", "罵")
compare_samples_better("閑", "閒")
compare_samples_better("凼", "氹")
compare_samples_better("豔", "艷")
compare_samples_better("粧", "妝")
compare_samples_better("确", "確")
compare_samples_better("唉", "哎")
compare_samples_better("姪", "侄")
compare_samples_better("脣", "唇")
compare_samples_better("劵", "券")
compare_samples_better("喐", "郁")
compare_samples_better("潷", "𢳂")
compare_samples_better("㧾", "𢳂")
compare_samples_better("涷", "凍")
compare_samples_better("瓹", "捐")
compare_samples_better("拑", "鉗")
compare_samples_better("箝", "鉗")
compare_samples_better("䄛", "褸")
compare_samples_better("摟", "褸")
compare_samples_better("鮓", "渣")
compare_samples_better("爲", "為")
compare_samples_better("岀", "出")
compare_samples_better("卟", "吓")
compare_samples_better("歳", "歲")
compare_samples_better("増", "增")
compare_samples_better("樖", "棵")
compare_samples_better("舖", "鋪")
compare_samples_better("窑", "窯")
compare_samples_better("窰", "窯")
compare_samples_better("碍", "礙")
compare_samples_better("掀", "㨴")
compare_samples_better("揾", "搵")
compare_samples_better("黄", "黃")
compare_samples_better("鲩", "鯇")
compare_samples_better("説", "說")
compare_samples_better("踭", "㬹")
compare_samples_better("敎", "教")
compare_samples_better("痹", "痺")
compare_samples_better("㖩", "噉")
compare_samples_better("减", "減")
compare_samples_better("喞", "唧")
compare_samples_better("戏", "戲")
compare_samples_better("幢", "棟")
compare_samples_better("㒼", "萌")
compare_samples_better("妳", "你")
compare_samples_better("瀄", "擳")
compare_samples_better("週", "周")
compare_samples_better("吋", "寸")
compare_samples_better("呎", "尺")
compare_samples_better("紮", "扎")
compare_samples_better("迹", "跡")
compare_samples_better("摷", "耖")
compare_samples_better("脱", "脫")
compare_samples_better("哂", "晒")
compare_samples_better("顔", "顏")
compare_samples_better("鬰", "鬱")
compare_samples_better("噜", "嚕")
compare_samples_better("麽", "麼")
compare_samples_better("内", "內")
compare_samples_better("䔨", "蕹")
compare_samples_better("杮", "柿")
compare_samples_better("櫈", "凳")
compare_samples_better("蕌", "蕎")
compare_samples_better("藠", "蕎")
compare_samples_better("拮", "㓤")
compare_samples_better("炳", "丙")
compare_samples_better("抦", "丙")
compare_samples_better("税", "稅")
compare_samples_better("温", "溫")
compare_samples_better("卐", "卍")
compare_samples_better("寛", "寬")
compare_samples_better("甙", "䣧")
compare_samples_better("躰", "體")
compare_samples_better("帰", "歸")
compare_samples_better("戦", "戰")
compare_samples_better("藴", "蘊")
compare_samples_better("稲", "稻")
compare_samples_better("眞", "真")
compare_samples_better("専", "專")
compare_samples_better("郷", "鄉")
compare_samples_better("駄", "馱")
compare_samples_better("険", "險")
compare_samples_better("靭", "韌")
compare_samples_better("瑠", "琉")
compare_samples_better("吡", "諀")
compare_samples_better("栐", "柡")
compare_samples_better("歩", "步")
compare_samples_better("圑", "團")
compare_samples_better("絶", "絕")
compare_samples_better("舗", "舖")
compare_samples_better("冨", "富")
compare_samples_better("鮎", "鯰")
compare_samples_better("渋", "涉")
compare_samples_better("脇", "脅")
compare_samples_better("浜", "濱")
compare_samples_better("雑", "雜")
compare_samples_better("瀞", "淨")
compare_samples_better("塩", "鹽")
compare_samples_better("苄", "芐")
compare_samples_better("権", "權")
compare_samples_better("扌", "手")
compare_samples_better("桜", "櫻")
compare_samples_better("恵", "惠")
compare_samples_better("発", "發")
compare_samples_better("寜", "寧")
compare_samples_better("吿", "告")
compare_samples_better("絵", "繪")
compare_samples_better("込", "迂")
compare_samples_better("乗", "乘")
compare_samples_better("啉", "婪")
compare_samples_better("覻", "覷")
compare_samples_better("亜", "亞")
compare_samples_better("撃", "擊")
compare_samples_better("処", "處")
compare_samples_better("处", "處")
compare_samples_better("晄", "晃")
compare_samples_better("栃", "櫔")
compare_samples_better("辧", "辦")
compare_samples_better("醖", "醞")
compare_samples_better("掦", "揚")
compare_samples_better("姉", "姊")
compare_samples_better("産", "產")
compare_samples_better("竜", "龍")
compare_samples_better("姸", "妍")
compare_samples_better("図", "圖")
compare_samples_better("薫", "薰")
compare_samples_better("沢", "澤")
compare_samples_better("蔵", "藏")
compare_samples_better("徳", "德")
compare_samples_better("紥", "紮")
compare_samples_better("晳", "晰")
compare_samples_better("腈", "睛")
compare_samples_better("兪", "俞")
compare_samples_better("妸", "婀")
compare_samples_better("誔", "誕")
compare_samples_better("喆", "哲")
compare_samples_better("抜", "拔")
compare_samples_better("転", "轉")
compare_samples_better("辺", "邊")
compare_samples_better("楽", "樂")
compare_samples_better("昰", "是")
compare_samples_better("飈", "飆")
compare_samples_better("滝", "瀧")
compare_samples_better("歴", "歷")
compare_samples_better("団", "團")
compare_samples_better("鬪", "鬥")
compare_samples_better("蝽", "椿")
compare_samples_better("踳", "蝽")
compare_samples_better("柾", "柩")
compare_samples_better("隠", "隱")
compare_samples_better("裵", "裴")
compare_samples_better("貎", "貌")
compare_samples_better("曺", "曹")
compare_samples_better("勑", "敕")
compare_samples_better("莾", "莽")
compare_samples_better("竈", "灶")
compare_samples_better("暦", "曆")
compare_samples_better("廻", "迴")
compare_samples_better("曯", "囑")
compare_samples_better("矚", "囑")
compare_samples_better("戸", "戶")
compare_samples_better("户", "戶")
compare_samples_better("晩", "晚")
compare_samples_better("毎", "每")
compare_samples_better("髪", "髮")
compare_samples_better("剣", "劍")
compare_samples_better("実", "實")
compare_samples_better("兎", "兔")
compare_samples_better("臓", "臟")
compare_samples_better("県", "縣")
compare_samples_better("吲", "哂")
compare_samples_better("翆", "翠")
compare_samples_better("焼", "燒")
compare_samples_better("爕", "燮")
compare_samples_better("売", "賣")
compare_samples_better("瀬", "瀨")
compare_samples_better("邉", "邊")
compare_samples_better("涙", "淚")
compare_samples_better("斎", "齋")
compare_samples_better("槇", "槙")
compare_samples_better("覧", "覽")
compare_samples_better("遡", "溯")
compare_samples_better("奬", "獎")
compare_samples_better("殻", "殼")
compare_samples_better("犠", "犧")
compare_samples_better("糭", "粽")
compare_samples_better("躱", "躲")
compare_samples_better("麺", "麵")
compare_samples_better("黒", "黑")
compare_samples_better("湼", "涅")
compare_samples_better("晧", "皓")
compare_samples_better("顕", "顯")
compare_samples_better("艶", "艷")
compare_samples_better("鉄", "鐵")
compare_samples_better("凖", "準")
compare_samples_better("観", "觀")
compare_samples_better("擕", "㩦")
compare_samples_better("徴", "徵")
compare_samples_better("気", "氣")
compare_samples_better("頴", "穎")
compare_samples_better("嶋", "島")
compare_samples_better("抺", "抹")
compare_samples_better("硏", "研")
compare_samples_better("篭", "籠")
compare_samples_better("廏", "廄")
compare_samples_better("亁", "乾")
compare_samples_better("犇", "奔")
compare_samples_better("怇", "佢")
compare_samples_better("姫", "姬")
compare_samples_better("駅", "驛")
compare_samples_better("閲", "閱")
compare_samples_better("鎭", "鎮")
compare_samples_better("鎹", "餸")
compare_samples_better("擤", "呻")
compare_samples_better("凑", "湊")
compare_samples_better("篋", "喼")
compare_samples_better("揜", "揞")
compare_samples_better("銊", "戌")
compare_samples_better("抰", "揚")
compare_samples_better("戙", "棟")
compare_samples_better("愩", "貢")
compare_samples_better("屘", "尾")
compare_samples_better("睺", "吼")
compare_samples_better("熝", "淥")
compare_samples_better("錑", "𨀤")
compare_samples_better("更", "更")
compare_samples_better("不", "不")
compare_samples_better("利", "利")
compare_samples_better("料", "料")
compare_samples_better("聯", "聯")
compare_samples_better("行", "行")
compare_samples_better("立", "立")
compare_samples_better("年", "年")
compare_samples_better("來", "來")
f.close()

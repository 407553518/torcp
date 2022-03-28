import pytest
import tortitle
from torcategory import TorCategory


@pytest.mark.parametrize("test_input, e1, e2, e3, e4", [
    ('权力的游戏.第S01-S08.Game.Of.Thrones.S01-S08.1080p.Blu-Ray.AC3.x265.10bit-Yumi',
     'Game Of Thrones', '', 'S01-S08', ''),
    ('辅佐官：改变世界的人们S01-S02.Chief.of.Staff.2019.1080p.WEB-DL.x265.AC3￡cXcY@FRDS',
     'Chief of Staff', '2019', 'S01-S02', ''),
    ('半暖时光.The.Memory.About.You.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB',
     'The Memory About You', '2021', 'S01', ''),
    ('不惑之旅.To.the.Oak.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB', 'To the Oak',
     '2021', 'S01', ''),
    ('不惑之旅.To.the.Oak.S01.2021.V2.2160p.WEB-DL.AAC.H265-HDSWEB', 'To the Oak',
     '2021', 'S01', ''),
    ('六十一号的恐怖 ：The.Scary.of.Sixty-First.2021.1080p.Blu-ray.AVC.DTS-HD.MA.5.1-GeekArt@CHDBits', 'The Scary of Sixty First', '2021', '', ''),
    ('当家主母.Marvelous.Women.S01.2021.V3.2160p.WEB-DL.AAC.H265-HDSWEB',
     'Marvelous Women', '2021', 'S01', ''),
    ('彩虹宝宝第三季.Rainbow.Ruby.S03.2020.WEB-DL.4k.H265.AAC-HDSWEB', 'Rainbow Ruby', '2020', 'S03', ''),
    ('民警老林的幸福生活.The.Happy.Life.of.People\'s.Policeman.Lao.Lin.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB',
     'The Happy Life of People\'s Policeman Lao Lin', '2021', 'S01', ''),
    ('千古风流人物.Qian.Gu.Feng.Liu.Ren.Wu.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB',
     'Qian Gu Feng Liu Ren Wu', '2021', 'S01', ''),
    ('太平间闹鬼事件 The Haunting in Connecticut 2009 Blu-ray 1080p AVC DTS-HD MA 7.1-Pete@HDSky',
     'The Haunting in Connecticut', '2009', '', ''),
    ('一片冰心在玉壶.Heart.of.Loyalty.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB',
     'Heart of Loyalty', '2021', 'S01', ''),
    ('住在我隔壁的甲方.Party.A.Who.Lives.Beside.Me.S01.2021.1080p.WEB-DL.AAC.H264-HDSWEB',
     'Party A Who Lives Beside Me', '2021', 'S01', ''),
    ('铸匠.The.Builders.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB', 'The Builders',
     '2021', 'S01', ''),
    ('Dinotrux S03E02 1080p Netflix WEB-DL DD 5.1 H.264-AJP69.mkv', 'Dinotrux', '', 'S03', 'E02'),
    ('排球女将.Moero.Attack.1979.Complete.WEB-DL.1080p.H264.DDP.MP3.Mandarin&Japanese-OPS', 'Moero Attack', '1979', '', ''),
    ('CCTV1.Yuan.Meng.Zhong.Guo.De.Yao.Zhong.Hua.20211129.HDTV.1080i.H264-HDSTV.ts',
     'Yuan Meng Zhong Guo De Yao Zhong Hua 20211129', '', '', ''),
    ('CCTV5+.2021.Snooker.UK.Championship.20211129.HDTV.1080i.H264-HDSTV.ts',
     'Snooker UK Championship 20211129', '2021', '', ''),
    ('CCTV5+.2021.World.Table.Tennis.Championship.20211130.HDTV.1080i.H264-HDSTV.ts',
     'World Table Tennis Championship 20211130', '2021', '', ''),
    ('CCTV5.Total.Soccer.20211129.HDTV.1080i.H264-HDSTV.ts',
     'Total Soccer 20211129', '', '', ''),
    ('CCTV9.The.Legend.Of.Film.Ep01-Ep06.HDTV.1080i.H264-HDSTV',
     'The Legend Of Film', '', 'S01', 'Ep01-Ep06'),
    ('The.Boys.S02.2020.1080p.BluRay.DTS.x265-10bit-HDS', 'The Boys', '2020',
     'S02', ''),
    ('X档案.第一季.1993.中英字幕￡CMCT梦幻', 'X档案', '1993', 'S01', ''),
    ('射雕英雄传1983.双语中字(LITV)', '射雕英雄传', '1983', '', ''),
    ('Taxi.4.2007.Director\'s.Cut.2007.Bluray.1080p.x264.DD5.1-wwhhyy@Pter.mkv', 'Taxi 4', '2007', '', ''),
    ('CCTV8HD My Own Swordsman E01-E80 1396x866p H10bits HDTV H264-sammy', 'My Own Swordsman', '', 'S01', 'E01-E80'),
    ('Californication.S01-07.1080p.BluRay.DD5.1.x264-NTb', 'Californication', '', 'S01-07', ''),
    ('Fan.Ren.Xiu.Xian.Zhuan.E32.1080p.WEB-DL.H264.AAC-CHDWEB.mp4', 'Fan Ren Xiu Xian Zhuan', '', 'S01', 'E32'),
    ('Indiana Jones The Complete Adventures 1981-2008 UHD Blu-Ray 2160p&1080p HEVC&AVC Atmos TrueHD 7 1&DTS-HD MA 5 1-CHDBits', 'Indiana Jones The Complete Adventures', '1981-2008', '', ''),
    ('Doctor.X.Surgeon.Michiko.Daimon.S06.1080p.BluRay.x265.10bit.FLAC.MNHD-FRDS',
     'Doctor X Surgeon Michiko Daimon', '', 'S06', ''),
    ('逆世界.Upside.Down.2012.BluRay.1080p.x265.10bit.2Audio.MNHD-FRDS',
     'Upside Down', '2012', '', ''),
    ('野战排.Platoon.1986.BluRay.1080p.x265.10bit.2Audio.MNHD-FRDS', 'Platoon',
     '1986', '', ''),
    ('Stargate.Atlantis.S04.Multi.1080p.BluRay.DTS-HDMA.5.1.H.264-CELESTIS',
     'Stargate Atlantis', '', 'S04', ''),
    ('谍影重重1-5.The.Bourne.2002-2016.1080p.Blu-ray.x265.DTS￡cXcY@FRDS',
     'The Bourne', '2002-2016', '', ''),
    ('豹.1963.JPN.1080p.意大利语中字￡CMCT风潇潇', '豹', '1963', '', ''),
    # ('[迪士尼]2009.飞屋环游记.天外奇迹.冲天救兵.冲天奇兵.3D版.国粤英.原盘中字.BD.Iso', '飞屋环游记', '2009', ''),
    ('过界男女.2013.国粤双语.简繁中字￡CMCT紫卿醺', '过界男女', '2013', '', ''),
    ('Maleficent Mistress of Evil V2 2019 ULTRAHD Blu-ray 2160p HEVC Atmos TrueHD 7.1-sGnb@CHDBits', 'Maleficent Mistress of Evil V2', '2019', '', ''),
    ('金刚狼3殊死一战.Logan.2017.BluRay.1080p.x265.10bit.MNHD-FRDS', 'Logan', '2017',
     '', ''),
    ('托马斯和他的朋友们第18季 第4集_3840x2160_H265_10.51_285.91MB.mp4', '托马斯和他的朋友们', '', 'S18', 'E4'),
    ('(BDMV)Anneke Gronloh - De Regenboog Serie (2009) FLAC-CD] {NL,Telstar B.V,TCD 70316-2}',
     'Anneke Gronloh De Regenboog Serie', '2009', '', ''),
    ('Foundation.2021.S01.2160p.ATVP.WEB-DL.DDP5.1.DV.HEVC-CasStudio',
     'Foundation', '2021', 'S01', ''),
    ('War for the Planet of the Apes 2017 ULTRAHD BluRay 2160p HEVC Atmos TrueHD 7.1-sGnb@CHDBits', 'War for the Planet of the Apes', '2017', '', ''),
    ('我是你的眼.I\'m.Your.Eyes.2016.S01.2160p.WEB-DL.H265.AAC-LeagueWEB',
     'I\'m Your Eyes', '2016', 'S01', ''),
    ('The Fixies Ⅲ 2017 EP01-EP52 1080P WEB-DL AAC x264-GTQing', 'The Fixies Ⅲ', '2017', 'S01', 'EP01-EP52'),
    ('人类星球 Human Planet(1080P)', 'Human Planet', '', '', ''),
    ('The.Owl.House.S01.1080p.DSNP.WEBRip.AAC2.0.x264-LAZY[rartv]', 'The Owl House', '', 'S01', ''),
    ('The.Owl.House.S02E02.Escaping.Expulsion.1080p.HULU.WEBRip.AAC2.0.H264-LAZY[rarbg]', 'The Owl House', '', 'S02', 'E02'),
    ('Guard.Jie.Fang.Xi.2022.S03.1080p.WEB-DL.H264.AAC-TJUPT', 'Guard Jie Fang Xi', '2022', 'S03', ''),
    ('[不能只有我看到的-便利店追女神食谱].Fast&Delicious.2021.1080i.HDTV.H264.DD-PTerTV', 'Fast&Delicious', '2021', '', ''),
    ('Ms.45.1981.720p.BluRay.FLAC1.0.x264-PTer', 'Ms 45', '1981', '', ''),
    ('BTV.The.Forbidden.City.Ep11-Ep12.HDTV.1080i.H264-HDSTV', 'The Forbidden City', '', 'S01', 'Ep11-Ep12'),
    ('HunanTV.Da.Wan.Zai.De.Ye.20211201.HDTV.1080i.H264-HDSTV.ts', 'Da Wan Zai De Ye 20211201', '', '', ''),
    ('2021.FIVB.VNL.CHN.vs.BRA.20210608.1080p.REPACK.WEB-DL.x264.AAC-TJUPT.mp4', 'FIVB VNL CHN vs BRA 20210608', '2021', '', ''),
    ('失落的秘符.第1季', '失落的秘符', '', 'S1', ''),
    ('最后的决斗.The.Last.Duel.2021.1080p.Blu-ray.x265.DTS￡cXcY@FRDS', 'The Last Duel', '2021', '', ''),
    ('现代爱情S02.Modern.Love.2021.1080p.WEB-DL.x265.AC3￡cXcY@FRDS', 'Modern Love', '2021', 'S02', ''),
    # ('สิ่งเล็กเล็กที่เรียกว่า...รัก.A.Little.Thing.Called.Love.AKA.First.Love.2010.WEB-DL.1080p.x264.AAC-PTHome.mp4', 'A Little Thing Called Love', '2010', '', ''),
    ('Top138.英雄本色(4K修复版).A.Better.Tomorrow.1986.REMASTERED.Bluray.1080p.x265.AAC(5.1).2Audios.GREENOTEA', 'A Better Tomorrow', '1986', '', ''),
    ('Weathering.With.You.2019.1080p.NLD.AVC.DTS-HD.MA.5.1-NeoVision', 'Weathering With You', '2019', '', ''),
    ('[BDMV][Bokutachi no Remake][Vol.01-02]', 'Bokutachi no Remake', '', '', ''),
    ('[吸血鬼同盟][Dance In The Vampire Bund][ダンスインザヴァンパイアバンド][BDMV][1080p][DISC×2][GER]', 'Dance In The Vampire Bund', '', '', ''),
    ('1917 2019 V2 ULTRAHD BluRay 2160p HEVC Atmos TrueHD7.1-sGnb@CHDBits', '1917', '2019', '', ''),
    ('[和楽器バンド (Wagakki Band) – TOKYO SINGING [初回限定映像盤 2Blu-ray]][BDMV][1080P][MPEG-4 AVC / LPCM]', '和楽器バンド Wagakki Band TOKYO SINGING', '', '', ''),
    ('[酷爱电影的庞波小姐][Eiga Daisuki Pompo-san][映画大好きポンポさん][BDRip][1920x1040][Movie][x264 Hi10P TrueHD MKV][TTGA]', 'Eiga Daisuki Pompo san', '', '', ''),
    ('[柳林风声][The Wind in the Willows][BDMV][1080p][MOVIE][AVC LPCM][UK]', 'The Wind in the Willows', '', '', ''),
    ('[BanG Dream! Episode of Roselia][劇場版 BanG Dream! Episode of Roselia][BDRip][1920x1080][Movie 01-02 Fin+SP][H264 FLAC DTS-HDMA MKV][自壓]', 'BanG Dream! Episode of Roselia', '', '', ''),
    ('[持续狩猎史莱姆三百年, 不知不觉就练到LV MAX][Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita][スライム倒して300年、知らないうちにレベルMAXになってました][外挂结构][日英简]', 'Slime Taoshite 300 nen, Shiranai Uchi ni Level Max ni Nattemashita', '', '', ''),
    ('[贾希大人不气馁][The Great Jahy Will Not Be Defeated! / Jahy-sama wa Kujikenai!][ジャヒー様はくじけない!][BDMV][1080p][Vol.1]', 'The Great Jahy Will Not Be Defeated!', '', '', ''),
    ('[银河英雄传说 Die Neue These (2019)][Ginga Eiyuu Densetsu: Die Neue These (2019) / Legend of the Galactic Heroes: Die Neue These (2019)][銀河英雄伝説 Die Neue These (2019)][BDMV][1080p][Vol.4-6 BDx3 + DVDx3 Fin][JP]', 'Ginga Eiyuu Densetsu: Die Neue These 2019', '2019', '', ''),
    ('[堀與宮村][Horimiya][ホリミヤ][加流重灌 (Modded Blu-rays)][1080P][Vol.1-Vol.7 Fin][SweetDreamDay]', 'Horimiya', '', '', ''),
    ('[剧场版 Healin\' Good 光之美少女 梦想的小镇心动不已! GoGo! 大变身!!][Eiga Healin\' Good Precure Yume no Machi de Kyun! Tto Go Go! Dai Henshin!!][映画ヒーリングっど プリキュア ゆめのまちでキュン!っとGoGo!大変身!!/(短編)映画トロピカル~ジュ!プリキュアとびこめ!コラボダンスパーティ!][BDMV][MOVIE][U2娘@Share]', 'Eiga Healin\' Good Precure Yume no Machi de Kyun! Tto Go Go! Dai Henshin!!', '', '', ''),
    ('[鲁邦三世VS名侦探柯南 THE MOVIE]Lupin the 3rd vs Detective Conan THE MOVIE / Lupin Sansei vs. Meitantei Conan The Movie[ルパン三世vs名探偵コナン THE MOVIE][BDMV][1080p][MOVIE][AVC][ITA]', 'Lupin the 3rd vs Detective Conan THE MOVIE', '', '', ''),
    ('Metal Gear Solid 3D - Snake Eater (USA) (En,Fr,Es).zip', 'Metal Gear Solid 3D Snake Eater USA En Fr Es', '', '', ''),
    ('[Moozzi2] Assassins Pride [ x265-10Bit Ver. ] - TV + SP', 'Assassins Pride', '', '', ''),
    ('CC_(1960-1964)_The Kennedy Films of Robert Drew & Associates', 'The Kennedy Films of Robert Drew & Associates', '1960-1964', '', ''),
    ('[TV][NPMS][Cocomelon 第三季][CoComelon.S03.1080p.NF.WEB-DL.DDP2.0.H.264-NPMS][MKV]', 'CoComelon', '', 'S03', ''),
    ('[WARP276] Danny Brown - Atrocity Exhibition (2016) [FLAC]', 'Danny Brown Atrocity Exhibition 2016', '2016', '', ''),
    ('The Beatles - Rubber Soul (Remastered) 1965 - FLAC 16bit 44.1khz', 'The Beatles Rubber Soul', '1965', '', ''),
    ('Marina - Ancient Dreams In A Modern Land (2021) - WEB FLAC', 'Marina Ancient Dreams In A Modern Land', '2021', '', ''),
    ('郁可唯 - 蓝短裤 2010 FLAC', '郁可唯 蓝短裤', '2010', '', ''),
    ('[皇后高品质音乐]陈慧琳-微光[分轨FLAC]', '陈慧琳 微光', '', '', ''),
    ('Stefanie Sun (孫燕姿) - Against the Light (逆光) (2007) - FLAC', 'Stefanie Sun 孫燕姿 Against the Light 逆光', '2007', '', ''),
    ('Pink Floyd - The Final Cut (1983) [FLAC] {72435-76734-2-6}', 'Pink Floyd The Final Cut', '1983', '', ''),
    ('[2021.05.28] にじさんじ - PALETTE 003 - Virtual Strike (フル・シングル) [FLAC]', 'にじさんじ PALETTE 003 Virtual Strike フル・シングル', '2021', '', ''),
    ('Peggy_Lee-The_Legendary_Peggy_Lee-3CD-FLAC-1999-FLACME', 'Peggy Lee The Legendary Peggy Lee', '1999', '', ''),
    ('Bob Dylan - Bringing It All Back Home (1965) [FLAC] {2013 MFSL}', 'Bob Dylan Bringing It All Back Home', '1965', '', ''),
    ('张国荣 - H₂O 1984 480i MPEG AC3-PTerMV.VOB', '张国荣 H₂O', '1984', '', ''),
    ('WINNER - EVERYD4Y (FLAC)', 'WINNER EVERYD4Y', '', '', ''),
    ('Dee-Mack-Doin_It_My_Way-CD-FLAC-1995-AUDiOFiLE', 'Dee Mack Doin It My Way', '1995', '', ''),
    ('Andrea Bocelli-Super Hits-2CD-WEB-2004-playMUSIC', 'Andrea Bocelli Super Hits', '2004', '', ''),
    ('范玮琪 - 我们的纪念日 FLAC', '范玮琪 我们的纪念日', '', '', ''),
    ('[EAC][180613][SINGLE][藍井エイル][流星／約束][VVCL-1252~4][FLAC+CUE+LOG+PNG+ISO]', '藍井エイル', '', '', ''), 
    ('[EAC][170927][SINGLE][V.A.][SWORD ART ONLINE THE MOVIE ORDINAL SCALE CHARACTER SONGS][ANZX-14002][FLAC+CUE+LOG]', 'SWORD ART ONLINE THE MOVIE ORDINAL SCALE CHARACTER SONGS', '', '', ''),
    ('[EAC][170927][ALBUM][能登麻美子][地獄少女 ENDING SONG COLLECTION][SBCV-80273][FLAC+CUE+LOG+PNG]', '地獄少女 ENDING SONG COLLECTION', '', '', ''),
    ('[银魂°(第3期)][Gintama Season3][銀魂°][BDrip][1920x1080][TV 01-51(266-316)Fin+SP][H264 FLAC MKV][自壓(付相關專輯)]', 'Gintama Season3', '', '', ''),
    ('[银魂./银魂 第四期/银魂 烙阳决战篇][Gintama./Gintama Season 4][銀魂./銀魂. 烙陽決戦篇][BDMV][Vol.03][JPN][MAL]', 'Gintama.', '', '', ''),
    ('[銀魂°][Gintama][銀魂゜][BDMV][1080p][Season 3 Parts 1+2 Fin][USA][自抓]', 'Gintama', '', '', ''),
    ('Megazone 23 1985 BD', 'Megazone 23', '1985', '', ''), 
    ('BD-50_A_PORTRAIT_OF_SHUNKIN_1976_BC', 'A PORTRAIT OF SHUNKIN', '1976', '', ''),
    ('Dave (1993) BD25', 'Dave', '1993', '', ''),
    ('SHES_FUNNY_THAT_WAY', 'SHES FUNNY THAT WAY', '', '', ''),
    ('Sabotage [BD25] (1939)', 'Sabotage', '1939', '', ''),
    ('A Raisin in the Sun (1961) NTSC DVD9+DVD5', 'A Raisin in the Sun', '1961', '', ''),
    ('Little Nikita [1988] by Richard Benjamin [R2]', 'Little Nikita', '1988', '', ''),
    ('1991.2018.BluRay.Remux.1080p.AVC.DTS-HD.MA.5.1-HDH', '1991', '2018', '', ''),
    ('[备长炭][Binchou-tan][びんちょうタン][DVDISO][720x480][Vol.1-Vol.3 Fin][R2J]', 'Binchou tan', '', '', ''),
    ('[龙珠Z剧场版 01-13][Dragonball Z – The Movies –][ドラゴンボールZ 劇場版][BDMV][1080p][BD-BOX 1-3 Disc*6 Fin][MPEG-4 AVC][GER][iFPD]', 'Dragonball Z The Movies', '', '', ''),
    ('[EAC][合集][菅野洋子作曲专辑合集][Vol.5][17张]', '菅野洋子作曲专辑合集', '', '', ''),
    ('[To LOVEる][To LOVERu][HDTVrip][1280x720][01-26FIN][MKV][澄空学园字幕组内嵌]', 'To LOVERu', '', '', ''),
    ('Ikumi Ogasawara - Tears Of Joy (2019) [DSF] DSD512', 'Ikumi Ogasawara Tears Of Joy', '2019', '', ''),
    ('VA-The_Best_80s_Album_In_The_World_Ever-3CD-FLAC-2020-ERP', 'VA The Best 80s Album In The World Ever', '2020', '', ''),
    ('Chihayafuru Part 3 2018 JPN Blu-ray 1080p AVC DTS-HD MA 5.1-UserExperience-Raws', 'Chihayafuru Part 3', '2018', '', ''),
    ('[Hi-Res] Evan Call - VIOLET EVERGARDEN_Echo Through Eternity [FLAC 96kHz-24bit]', 'Evan Call VIOLET EVERGARDEN Echo Through Eternity', '', '', ''),
    ('10000 Chopin, Liszt, Debussy Piano Peaces (Miyuji Kaneko)', '10000 Chopin Liszt Debussy Piano Peaces Miyuji Kaneko', '', '', ''),
    ('2004-原来我爱你那么多 新歌+精选 2CD[引进版][WAV]', '原来我爱你那么多 新歌 精选', '2004', '', ''),
    ('滅火器 (Fire EX.) - On Fire Day 2020 - Fire Next 新篇章：滅火器20 週年演唱會 (2021)', '滅火器 Fire EX On Fire Day 2020 Fire Next 新篇章：滅火器20 週年演唱會', '2021', '', ''),
    ('(2012.12.21) Kenichiro Nishihara - Iluminus (flac)', 'Kenichiro Nishihara Iluminus', '2012', '', ''),
    ('Twice - #TWICE (CD-FLAC)', 'Twice #TWICE', '', '', ''),
    ('风潮唱片-《马修.连恩系列-驯鹿宣言》(Caribou Commons)专辑[APE整轨]', '风潮唱片 《马修 连恩系列 驯鹿宣言》 Caribou Commons 专辑', '', '', ''),
    ('Bach - Vionlin Concertos - Isabelle Faust {HMM 902335.36} (2019) [FLAC]', 'Bach Vionlin Concertos Isabelle Faust', '2019', '', ''),
    ('[迪士尼]2015.恐龙当家.恐龙大时代.美好的恐龙世界.善良的恐龙.恐龙管家.3D港版.国语简繁中字.BD.ISO', '恐龙当家 恐龙大时代 美好的恐龙世界 善良的恐龙 恐龙管家', '2015', '', ''),
    # ('E3.2018.Press.Conference.WEB-DL.1080p.H264.AAC-CMCTV', 'E3', '2018', 'S01', 'E3'),
    ('踢馆秘笈（第六季）—测试样片', '踢馆秘笈', '', 'S06', ''),
    ('海绵宝宝 国语 12季', '海绵宝宝', '', 'S12', ''),
    ('[阿涅斯论瓦尔达].Varda.by.Agnès.2019.CC.BluRay.1080p.x264.DTS-CMCT', 'Varda by Agnès', '2019', '', ''), 
    ('[艾娃].Ava.2020.AUS.BluRay.1080p.x264.DTS-CMCT', 'Ava', '2020', '', ''),
    ('[Jose与虎与鱼们].josee.the.tiger.and.the.fish.2003.KOR.BluRay.1080p.x264.FLAC-CMCT.mkv', 'josee the tiger and the fish', '2003', '', ''),
    ('No.33_指环王3.魔戒三部曲：国王归来.TLOTR.The.Return.of.the.King.EE.2003.加长版.x265.BD1080P.国英双语.特效中英字幕.mp4', 'TLOTR The Return of the King EE', '2003', '', ''),
    ('No.238_千钧一发(变种异煞) Gattaca (1997).BD720P.国英双语.中英双 字.mp4', 'Gattaca', '1997', '', ''),
    ('胜者即是正义SP.2013.720p.日语.简体中字￡WiKi(feat.CMCT)', '胜者即是正义SP', '2013', '', ''),
    ('七个世界，一个星球.全7集.2019.1080p.国英双语.双国配.中英字幕￡CMCT小鱼', '七个世界，一个星球', '2019', '', ''),
    ('音乐之声.五十周年纪念版.1965.1080p.国英双语.中英字幕￡CMCT风潇潇', '音乐之声', '1965', '', ''),
    ('The Borgias Disc2', 'The Borgias', '', '', ''),
    ('[故宫].全12集.简繁特效.2005.AVC.1080p.HDTV.H264.AC-3.DD2.0-@szdqwx', '故宫', '2005', '', ''),
    ('花仙子 全50集+剧场版.1080p.国日双语.中文字幕', '花仙子', '', '', ''),
    ('守夜号S01.Vigil.E01-E06.2021.1080p.Blu-ray.x265.AC3￡cXcY@FRDS', 'Vigil', '2021', 'S01', ''),
    ('黄石前传S01.1883.2021.1080p.WEB-DL.x265.AC3￡cXcY@FRDS', '1883', '2021', 'S01', ''),
    ('Who\'s.the.Murderer.2022.S07E05A.PartA.1080p.WEB-DL.H264.AAC-TJUPT', 'Who\'s the Murderer', '2022', 'S07', 'E05'),
    ('[二十五，二十一].Twenty.Five.Twenty.One.2022.1080p.S01E03.WEB-DL.H264.AAC-PTerWEB.mp4', 'Twenty Five Twenty One', '2022', 'S01', 'E03'),
    # ('[劫与罪].Heist.2021.S01.S01E03.NF.WEB-DL.1080p.H264.DDP.5.1-CMCTV.mp4', 'Heist', '2021', 'S01', 'E03'),
    # ('Grateful Dead - Listen to the River：St. Louis \'71 \'72 \'73 (Live) (2021) (24-192)', 'Grateful Dead - Listen to the River：St. Louis', '2021', '', ''),
    # ('32.迪卡唱片.-.《极致：勃拉姆斯选集》.(5CDs.Box-set)', '32 迪卡唱片 《极致：勃拉姆斯选集》', '', '', ''),
])
def test_parseTorName(test_input, e1, e2, e3, e4):
    tt = tortitle.TorTitle(test_input)
    assert e1 == tt.title and e2 == tt.yearstr and e3 == tt.season and e4 == tt.episode


@pytest.mark.parametrize("test_input, e1, e2", [
    ('权力的游戏.第S01-S08.Game.Of.Thrones.S01-S08.1080p.Blu-Ray.AC3.x265.10bit-Yumi',
     'TV', 'Yumi'),
    ('辅佐官：改变世界的人们S01-S02.Chief.of.Staff.2019.1080p.WEB-DL.x265.AC3￡cXcY@FRDS',
     'TV', 'FRDS'),
    ('半暖时光.The.Memory.About.You.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB', 'TV',
     'HDSWEB'),
    ('排球女将.Moero.Attack.1979.Complete.WEB-DL.1080p.H264.DDP.MP3.Mandarin&Japanese-OPS', 'TV', 'OPS'),
    ('The.Smurfs.2.2013.3Audio.DTS-HD.MA5.1.x265.10bit-BeiTai.mkv', 'MovieEncode', 'BeiTai'),
    ('Death.on.the.Nile.1978.1080p.BluRay.FLAC.2.0.x264-PTer.mkv', 'MovieEncode', 'PTer'),    
    ('不惑之旅.To.the.Oak.S01.2021.2160p.WEB-DL.AAC.H265-HDSWEB', 'TV', 'HDSWEB'),
    ('BDRemux+Hakumei+to+Mikochi+JP+7³ACG@OurBits', 'Other', 'OurBits'),
    ('FIFA.WORLD.CUP.QUALIFIERS.ENG.VS.ALB.20211113.1080i.HDTV.H264.DD-PTerTV.ts', 'HDTV', 'PTerTV'),
    ('Babymother.1998.1080p.BluRay.REMUX.AVC.FLAC.2.0-BLURANiUM.mkv', 'MovieRemux', 'BLURANiUM'),
    ('春花秋月未了情.Breezy.1973.1080p.BluRay.x265.10bit.FLAC.MNHD-FRDS', 'MovieEncode', 'FRDS'),
    ('Michael Jackson - The Mystery Of HIStory (1997) [FLAC]', 'Music', None),
    ('New_Order-(The_Rest_Of)_New_Order-CD-FLAC-1995-WREMiX', 'Music', 'WREMiX'),
    ('VA-Kill_Bill_Vol_2-(9362-48676-2)-CD-FLAC-2004', 'Music', '2004'),
    ('The Blue Diamonds - Het Beste Van (1988) [FLAC-CD] {WG,RM,Philips,834 484-2}', 'Music', None),
    ('Commodores - Caught In The Act (1975) [FLAC] {24-192 HDTracks}', 'Music', None),
    ('BTV.The.Forbidden.City.Ep11-Ep12.HDTV.1080i.H264-HDSTV', 'TV', 'HDSTV'),
    ('[漫游·张靓颖沉浸式虚拟音乐会·完整版].Roaming·Jane Zhang Immersive Virtual Concert.2021.1080p.WEB-DL.AVC.AAC-QHstudIo', 'MV', 'QHstudIo'),
    ('OOOPS2.2020.BluRay.1080p.2Audio.TrueHD.5.1.x265.10bit-BeiTai', 'MovieEncode', 'BeiTai'),
    ('现代爱情S02.Modern.Love.2021.1080p.WEB-DL.x265.AC3￡cXcY@FRDS', 'TV', 'FRDS'),
    ('The.Green.Planet.S01E01.Tropical.Worlds.2160p.iP.WEB-DL.AAC2.0.H.265-NTb.mkv', 'TV', 'NTb'),
    ('Adele.-.[Live.At.The.Royal.Albert.Hall].2011.Blu-Ray.1080I.H264.DTS-HDMA.-TTG', 'MV', 'TTG'),
    ('Aimer - DAWN (2015) {24bit, WEB} [FLAC]', 'Music', None),
    ('Bad Boys for Life 2020 V2 ULTRAHD BluRay 2160p HEVC DTS-X 7.1-sGnb@CHDBits', 'MovieBDMV4K', 'CHDBits'),
    ('The Fixies Ⅲ 2017 EP01-EP52 1080P WEB-DL AAC x264-GTQing', 'TV', 'GTQing'),
    ('[故宫].全12集.简繁特效.2005.AVC.1080p.HDTV.H264.AC-3.DD2.0-@szdqwx', 'HDTV', 'szdqwx'),
    ('Fiksik 螺丝钉1-3季 1080P 国语中字', 'TV', None),
    ('花仙子全50集+剧场版.1080p.国日双语.中文字幕', 'TV', None),
    ('[猫和老鼠1992电影版].Tom.and.Jerry.The.Movie.1992.WEB-DL.1080p.HEVC.AAC-CMCTV.mp4', 'MovieWebdl', 'CMCTV'),
    ('Lucile Boulanger - Bach & Abel_ Solo [FLAC 192kHz-24bit]', 'Music', None),
    ('Dana Zemtsov & Anna Fedorova - Silhouettes 2020 DSF', 'Music', None),
    ('Sabotage [BD25] (1939)', 'MovieBDMV', None),
    ('QUINTET 1979 DVD9 NTSC', 'MovieDVD', None),
    ('RETURN_TO_NEVER_LAND DVD', 'MovieDVD', None),
    ('My.Blueberry.Nights.2007.NTSC.DVD9', 'MovieDVD', None),
    ('Megazone 23 1985 BD', 'MovieBDMV', None),
    ('Metal Gear Solid 3D - Snake Eater (USA) (En,Fr,Es).zip', 'Archive', None),
    ('To.Sir.With.Love.II.1996.DVD.NTSC-CL8', 'MovieDVD', 'CL8'),
    ('Babka_Yozhka_i_drugiye_2008_BD', 'MovieBDMV', None),
    ('别有用心的单身女.Cunning.Single.Lady.S01E05.1080p.NF.WEB-DL.DDP2.0.x264-Ao.mkv', 'TV', 'Ao'),
    ('The.Ice.Age.Adventures.of.Buck.Wild.2022.2160p.DSNP.WEB-DL.DDP5.1.Atmos.DV.H.265-Lee@CHDWEB.mp4', 'MovieWebdl', 'CHDWEB'),
    ('我爱冒牌机器女友.I.Love.Fake.Robot.Girlfriends.2021.1080p.WEB-DL.H264.AAC-CHDWEB.mp4', 'MovieWebdl', 'CHDWEB'),
    ('譚詠麟 - 情人 1994 480i DVD MPEG AC3-PTerMV.vob', 'MV', 'PTerMV'),
    ('[局内人].Inside.Men.2015.BluRay.1080p.x264.DTS-CMCT.mkv', 'MovieEncode', 'CMCT'),
    ('Megazone 23 1985 BD', 'MovieBDMV', None), 
    ('BD-50_A_PORTRAIT_OF_SHUNKIN_1976_BC', 'MovieBDMV', None),
    ('Dave (1993) BD25', 'MovieBDMV', None),
    ('Sabotage [BD25] (1939)', 'MovieBDMV', None),
    ('The Great Australian Bake Off S02 WEB 720p', 'TV', None),
    ('Moses.Storm.Trash.White.2022.720p.WEB.h264-OPUS.mkv', 'MovieWebdl', 'OPUS'),
    ('Choose Your Own Adventure- Abominable Snowman 2006 DVD9', 'MovieDVD', None),
    ('Tron (DVD9)', 'MovieDVD', None),
    ('A Raisin in the Sun (1961) NTSC DVD9+DVD5', 'MovieDVD', None),
    ('Little Nikita [1988] by Richard Benjamin [R2]', 'Other', None),
    ('Shooting Party, The (1984) (PAL DVDR)', 'MovieDVD', None),
    ('The Hillside Strangler.2004.Dvd9-CG', 'MovieDVD', 'CG'),
    ('2002 - In Violet Light - \'15 Hi-Res @ 24~96 (flac)', 'Music', None),
    ('谭咏麟94纯金曲演唱会.Alan.Tan.live.in.HongKong.1994.D9&LD.HEVC.10bit.2Audio.MiniSD-XPcl@PTer', 'MV', 'PTer'),
    ('人类星球 Human Planet(1080P)', 'Movie', None),
    ('BoA.-.Camo.1080p.Bugs.AVC.AAC-HDHome.mp4', 'Movie', 'HDHome'),
    ('米老鼠2013.Mickey.Mouse.2013.S02E17.HR-HDTV.x264.AAC.Chs.Eng-Deefun迪幻字幕组.mkv', 'TV', 'Deefun迪幻字幕组'),
    # ('[AI-Raws] HELLO WORLD (BD HEVC 3840x2160 yuv444p10le Atmos／FLAC／FLAC[バリアフリー] 日本語字幕)[52F61BDB].mkv', 'MovieBDMV', None),
    # ('Sonata Arctica - Acoustic Adventures  - Volume One (2022)', 'Music', None),
    # ('Sara K.-No Cover-Chesky-0196', 'Music', None),
])
def test_categoryByName(test_input, e1, e2):
    tc = TorCategory(test_input)
    assert tc.ccfcat == e1 and tc.group == e2

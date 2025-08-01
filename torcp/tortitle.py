import re
import sys
import json
import string
import argparse
from pprint import pprint
from torcp.torcategory import cutExt


def isFullAscii(str):
    return re.fullmatch(r'[\x00-\x7F]*', str, re.A)


def containsCJK(str):
    return re.search(r'[\u4e00-\u9fa5\u3041-\u30fc]', str)


def containdCJKKeyword(str):
    return re.search(r'^(.迪士尼\b)', str)


def notTitle(str):
    return re.search(r'^(BDMV|1080[pi]|MOVIE|DISC|Vol)', str, re.A | re.I)


def cutAKA(titlestr):
    m = re.search(r'\s(/|AKA)\s', titlestr, re.I)
    if m:
        titlestr = titlestr.split(m.group(0))[0]
    return titlestr.strip()


def cutAKAJP(titlestr):
    m = re.search(r'(/|\bAKA\b)', titlestr, re.I)
    if m:
        titlestr = titlestr.split(m.group(0))[0]
    return titlestr.strip()


def getIndexItem(items, index):
    if index >= 0 and index < len(items):
        return items[index]
    else:
        return ''


def is0DayName(itemstr):
    # CoComelon.S03.1080p.NF.WEB-DL.DDP2.0.H.264-NPMS
    m = re.match(r'^\w+.*\b(BluRay|Blu-?ray|720p|1080[pi]|[xh].?26\d|2160p|576i|WEB-DL|DVD|WEBRip|HDTV)\b.*', itemstr, flags=re.A | re.I)
    return m


def getNoBracketedStr(torName, items):
    ss = torName
    for s in items:
        ss = ss.replace('[' + s + ']', '')
    ss = ss.replace('[', '')
    ss = ss.replace(']', '')
    ss = ss.strip()

    return ss


def cutBracketedTail(sstr):
    m = re.search(r'^\w+.*(\[[^]]*\]?)', sstr)
    if m:
        sstr = sstr[:m.span(1)[0]]
    return sstr


def bracketToBlank(sstr):
    dilimers = ['(', ')', '-', '–', '_', '+']
    for dchar in dilimers:
        sstr = sstr.replace(dchar, ' ')
    return re.sub(r' +', ' ', sstr).strip()


def delimerToBlank(sstr):
    dilimers = ['[', ']', '.', '{', '}', '_', ',']
    for dchar in dilimers:
        sstr = sstr.replace(dchar, ' ')
    return sstr


def cutspan(sstr, ifrom, ito):
    if (ifrom >= 0) and (len(sstr) > ito):
        sstr = sstr[0:ifrom:] + sstr[ito::]
    return sstr


def subEpisodeChar(partStr):
    partOrder = string.ascii_uppercase.find(partStr[0].upper()) + 1
    return ('Part %d' % partOrder) if partOrder > 0 else ''


def subEpisodePart(partStr):
    partOrder = string.digits.find(partStr[0])
    if partOrder < 0:
        partOrder = string.ascii_uppercase.find(partStr[0].upper()) + 1
    return ('Part %d' % partOrder) if partOrder > 0 else ''


class TorTitle:

    def parseSeason(self, sstr):
        seasonstr = ''
        seasonspan = [-1, -1]
        episodestr = ''

        # m1 = None
        # for m1 in re.finditer(r'(\bS\d+(-S\d+)?)\b', sstr, flags=re.A | re.I):
        #     pass
        m1 = re.search(r'(\bS\d+(-S?\d+))\s(?!.*\bS\d+)', sstr, flags=re.A | re.I)
        if m1:
            seasonstr = m1.group(1).strip()
            seasonspan = m1.span(1)
            sstr = sstr.replace(seasonstr, '')
            return seasonstr, seasonspan, episodestr

        # m2 = re.search(r'(\b(S\d+)([\. ]?(\d{4}[\s\.])?Ep?\d+)?)\b(?!.*S\d+)', sstr, flags=re.A | re.I)
        m2 = re.search(r'(\b(S\d+)([\. ]?(\d{4}[\s\.])?Ep?\d+(-Ep?\d+)?)?)([A-Z]?)\b', sstr, flags=re.A | re.I)
        if m2:
            seasonstr = m2.group(1)
            seasonspan = m2.span(1)
            if m2.group(3):
                seasonstr = m2.group(2).strip()
                episodestr = m2.group(3).strip()
            if m2.group(5):
                self.subEpisode  = subEpisodeChar(m2.group(5).strip())
            return seasonstr, seasonspan, episodestr

            # seasonsapn = mcns.span(1)
            # sstr = sstr.replace(mcns.group(1), '')
        mep = re.search(r'(Ep?\d+(-Ep?\d+)?)\b', sstr, flags=re.A | re.I)
        if mep:
            seasonstr = 'S01'
            episodestr = mep.group(1).strip()
            seasonspan = mep.span(1)
            # if mep.group(2):
            #     seasonstr = mep.group(2)
            #     seasonspan = mep.span(2)
            return seasonstr, seasonspan, episodestr

        mcns = re.search(r'(第?\s*((\d+)|([一二三四五六七八九十]))(-\d+)?季)(\s*第\s*((\d+)|([一二三四五六七八九十]))集)?', sstr, flags=re.I)
        if mcns:
            # origin_seasonstr = mcns.group(1)
            seasonspan = mcns.span(1)
            ssi = mcns.group(2)
            iss = '一二三四五六七八九'.find(ssi)
            if iss >= 0:
                ssi = str(iss+1).zfill(2)
            seasonstr = 'S' + ssi
            if mcns.group(6):
                episodestr = 'E' + mcns.group(7).strip()
            return seasonstr, seasonspan, episodestr
        return seasonstr, seasonspan, episodestr


    def parseYear(self, sstr):
        yearstr = ''
        yearspan = [-1, -1]
        m2 = re.search(
            r'\b((19\d{2}\b|20\d{2})(-19\d{2}|-20\d{2})?)\b(?!.*\b\d{4}\b.*)',
            sstr,
            flags=re.A | re.I)
        if m2:
            yearstr = m2.group(1).strip()
            yearspan = m2.span(1)
            if re.search(r'[\(\[\{]' + yearstr+r'\b', sstr):
                # sstr = sstr[:yearspan[0] - 1]
                yearspan = [yearspan[0]-1, yearspan[1]+1]
            # elif re.search(r'\w.*' + yearstr+r'\b', sstr):
            #     sstr = sstr[:yearspan[0]]
        return yearstr, yearspan


    def parseJpAniName(self, torName):
        yearstr, yearspan = self.parseYear(torName)

        items = re.findall(r'\[([^]]*[^[]*)\]', torName)

        if len(items) < 2:
            return self.parse0DayMovieName(torName)

        for s in items:
            if is0DayName(s):
                return self.parse0DayMovieName(s)

        strLeft = getNoBracketedStr(torName, items)
        if len(strLeft) > 0:
            # yearstr, titlestr = getYearStr(torName)
            titlestr = bracketToBlank(strLeft)
            return cutAKAJP(titlestr), yearstr, '', '', ''

        jptitles = []
        titlestrs = []
        jptitle = ''
        titlestr = ''
        for item in items:
            if re.match(r'^(BDMV|EAC|XLD|1080[pi]|MOVIE|DISC|Vol\.?\d+|MPEG|合集|ALBUM|SBCV|FLAC|SINGLE|V\.A|VVCL)\b', item, re.A | re.I):
                continue
            if re.match(r'^\d+$', item):
                continue

            if containsCJK(item):
                jptitles.append(item)
            else:
                titlestrs.append(item)

        if len(titlestrs) > 0:
            titlestr = titlestrs[0]
            # titlestr = max(titlestrs, key=len)
            if jptitles:
                jptitle = max(jptitles, key=len)
        else:
            if jptitles:
                # jptitle = jptitles[0]
                jptitle = max(jptitles, key=len)
                titlestr = jptitle
            else:
                pass
                # raise 'Some thing Wrong'

        titlestr = cutBracketedTail(titlestr)
        titlestr = bracketToBlank(titlestr)

        return cutAKAJP(titlestr), yearstr, '', '', jptitle

    def checkAfterSeason(self, sstr, seasonspan):
        if self.subEpisode:
            return sstr
        afterStr = sstr[seasonspan[1]:]
        m = re.search(r'part\s*(\d+|[A-Z])', afterStr, flags=re.I)
        if m:
            self.subEpisode = subEpisodePart(m.group(1))
            return cutspan(sstr, seasonspan[0], seasonspan[1]+m.span(0)[1])
        else:
            return sstr

    def parse0DayMovieName(self, torName):
        sstr = cutExt(torName.strip())

        failsafeTitle = sstr
        sstr = re.sub(r'^【.*】', '', sstr, flags=re.I)
        sstr = re.sub(r'\W(Disney|DSNP|Hami|ATVP|Netflix|NF|KKTV|Amazon|AMZN|HMAX|Friday|\d+fps)\W*WEB-?DL.*$', '', sstr, flags=re.I)
        sstr = re.sub(
            r'\b((UHD)?\s+BluRay|Blu-?ray|720p|1080[pi]|2160p|576i|WEB-DL|\.DVD\.|UHD|WEBRip|HDTV|Director(\'s)?[ .]Cut|REMASTERED|LIMITED|Complete(?=[. -]\d+)|SUBBED|TV Series).*$',
            '',
            sstr,
            flags=re.I)
        sstr = re.sub(r'\bComplete[\s\.]+(Series|HDTV|4K|1080p|WEB-?DL)\b', '', sstr, flags=re.I)
        sstr = re.sub(r'\[Vol.*\]$', '', sstr, flags=re.I)

        sstr = re.sub(r'\W?(IMAX|Extended Cut|Unrated Cut|\d+CD|APE整轨)\b.*$', '', sstr, flags=re.I)
        sstr = re.sub(r'[\[\(](BD\d+|WAV\d*|(CD\-)?FLAC|Live|DSD\s?\d*)\b.*$', '', sstr, flags=re.I)
        sstr = re.sub(r'^\W?(BDMV|\BDRemux|\bCCTV-4K|\bCCTV\d+(HD|K)?|BD\-?\d*|[A-Z]{1,5}TV)\W*', '', sstr, flags=re.I)

        sstr = re.sub(r'\{[^\}]*\}.*$', '', sstr, flags=re.I)
        sstr = re.sub(r'([\s\.-](\d+)?CD[\.-]WEB|[\s\.-](\d+)?CD[\.-]FLAC|[\s\.-][\[\(\{]FLAC[\]\)\}]).*$', '', sstr, flags=re.I)
        sstr = re.sub(r'\bFLAC\b.*$', '', sstr, flags=re.I)
        sstr = re.sub(r'^[\[\(]\d+[^\)\]]*[\)\]]', '', sstr, flags=re.I)
        sstr = re.sub(r'^Jade\b', '', sstr, flags=re.I)
        sstr = re.sub(r'^\(\w+\)', '', sstr, flags=re.I)

        sstr = re.sub(r'^\W?CC_?\b', '', sstr, flags=re.I)
        if sstr and sstr[-1] in ['(', '[', '{']:
            sstr = sstr[:-1]
        sstr = delimerToBlank(sstr)
        if sstr:
            failsafeTitle = sstr

        seasonstr, seasonspan, episodestr = self.parseSeason(sstr)
        if not seasonstr:
            seasonstr, seasonspan2, episodestr = self.parseSeason(torName)
        self.seasonstr = seasonstr
        sstr = self.checkAfterSeason(sstr, seasonspan)
        
        yearstr, yearspan = self.parseYear(sstr)
        if not yearstr:
            yearstr, yearspan = self.parseYear(torName)
            yearspan = [-1, -1]

        if seasonspan[0] > yearspan[0]:
            syspan = seasonspan
            systr = seasonstr
        else:
            syspan = yearspan
            systr = yearstr

        skipcut = False
        if syspan and syspan[0] > 1 :
            spanstrs = sstr.split(systr)
            if containdCJKKeyword(sstr[:syspan[0]]):
                sstr = sstr[syspan[1]:]
                skipcut = True
            else:
                sstr = sstr[:syspan[0]]

        if not skipcut:
            # sstr = cutspan(sstr, seasonspan[0], seasonspan[1])
            sstr = cutspan(sstr, yearspan[0], yearspan[1])
            sypos = seasonspan[0] if seasonspan[0] < yearspan[0] else yearspan[0]
            if sypos > 0:
                sstr = sstr[0:sypos].strip()
        if sstr:
            failsafeTitle = sstr
        sstr = re.sub(r'\b(Theatrical|Extended)\s+Version', '', sstr, flags=re.I)
        sstr = re.sub(r'\b(Classic|Unrated)\s*$', '', sstr, flags=re.I)
        sstr = re.sub(r'\b\w+(影|场|念|港|修复)版', '', sstr, flags=re.I)
        sstr = re.sub(r'(\b剧集|\b全\d+集|\b\d+集全|\b\w+(影|场|念|港)版|\b国语|\bDis[kc]\s*\d*|\bBD\d*).*$', '', sstr, flags=re.I)
        sstr = re.sub(r'(粤语|DIY|中字)[\u4e00-\u9fa5\u3041-\u30fc ]*$', '', sstr, flags=re.I)
        if sstr and sstr[-1] in ['(', '[', '{', '（', '【']:
            sstr = sstr[:-1]

        sstr = re.sub(r'(?<!^)(Ep?\d+(-Ep?\d+)?)\s*$', '', sstr, flags=re.A | re.I)

        # if titlestr.endswith(')'):
        #     titlestr = re.sub(r'\(.*$', '', sstr).strip()
        cntitle = ''
        if containsCJK(sstr):
            cntitle = sstr
            # m = re.search(r'^.*[^\x00-\x7F](S\d+|\s|\.|\d|-|\))*\b(?=[a-zA-Z])', sstr, flags=re.A)
            # m = re.search( r'^.*[^a-zA-Z_\- &0-9](S\d+|\s|\.|\d|-)*\b(?=[A-Z])', titlestr, flags=re.A)
            m = re.search(r'^.*[一-鿆\?？]\s*(S\d+(-S\d+)?|\([^(]*\)|\d+-\d+)?[： ]*(?=[0-9a-zA-Z])',
                            sstr, flags=re.A)
            if m:
                # ['(', ')', '-', '–', '_', '+']
                cntitle = m.group(0)
                if not re.search(r'\s[\-\+]\s', cntitle):
                    # if len(sstr)-len(cntitle) > 4:
                    sstr = sstr.replace(cntitle, '')
            else:
                m = re.search(r'^([\w\s]+)\s([一-鿆\?？]+)\s*$', sstr, flags=re.A)
                if m:
                    cntitle = m.group(1)
                    if not re.search(r'\s[\-\+]\s', cntitle):
                        sstr = sstr.replace(cntitle, '')
            # 连续空格只留 一个
            cntitle = re.sub(r' +', ' ', cntitle).strip()
            # 取第1个空格之前的部分
            cntitle = re.match(r'^[^ \(\[]*', cntitle).group()

        titlestr = bracketToBlank(sstr)
        titlestr = cutAKA(titlestr)
        if len(titlestr) > 5:
            titlestr = re.sub(r'part\s?\d+$', '', titlestr, flags=re.I).strip()
        if not containsCJK(titlestr) and len(titlestr) < 3:
            titlestr = bracketToBlank(failsafeTitle)

        return titlestr, yearstr, seasonstr, episodestr, cntitle

    def parseTorNameMore(self, torName):
        mediaSource, video, audio = '', '', ''
        if m := re.search(r"(?<=(1080p|2160p)\s)(((\w+)\s+)?WEB(-DL)?)|\bWEB(-DL)?\b|\bHDTV\b|((UHD )?(BluRay|Blu-ray))", torName, re.I):
            m0 = m[0].strip()
            if re.search(r'WEB[-]?(DL)?', m0, re.I):
                mediaSource = 'webdl'
            elif re.search(r'BLURAY|BLU-RAY', m0, re.I):
                if re.search(r'x26[45]', torName, re.I):
                    mediaSource = 'encode'
                elif re.search(r'remux', torName, re.I):
                    mediaSource = 'remux'
                else:
                    mediaSource = 'bluray'
            else:
                mediaSource = m0
        if m := re.search(r"AVC|HEVC(\s(DV|HDR))?|H\.?26[456](\s(HDR|DV))?|x26[45]\s?(10bit)?(HDR)?|DoVi (HDR(10)?)? (HEVC)?", torName, re.I):
            video = m[0].strip()
        if m := re.search(r"DTS-HD MA \d.\d|LPCM\s?\d.\d|TrueHD\s?\d\.\d( Atmos)?|DDP[\s\.]*\d\.\d( Atmos)?|(AAC|FLAC)(\s*\d\.\d)?( Atmos)?|DTS(?!-\w+)|DD\+? \d\.\d", torName, re.I):
            audio = m[0].strip()
        return mediaSource, video, audio

    def parseMovieName(self, torName):
        if torName.startswith('[') and torName.endswith('SP'):
            m = re.search(r'\]([^]]*\+.?SP)$', torName, flags=re.I)
            if m:
                namestr = torName[:m.span(1)[0]]
                return self.parseJpAniName(namestr)

        if torName.startswith('[') and torName.endswith(']'):
            return self.parseJpAniName(torName)
        else:
            return self.parse0DayMovieName(torName)

    def to_json(self):
        return {
            'title': self.title,
            'year': self.yearstr,
            'season': self.season,
            'episode': self.episode,
            'cntitle': self.cntitle
        }
    
    def to_csv(self, delimiter=','):
        return delimiter.join([self.title, self.yearstr, self.season, self.episode, self.cntitle])

    def __init__(self, torName):
        self.subEpisode = ''
        self.seasonstr = ''
        self.title, self.yearstr, self.season, self.episode, self.cntitle = self.parseMovieName(torName)


def main():
    parser = argparse.ArgumentParser(
        description='torcp: a script to parse torrent name.'
    )
    parser.add_argument('TORRENT_NAME', nargs="+", help='The torrent name.')
    parser.add_argument('-f', '--format', default='json', help='Output format, accept json,csv')
    parser.add_argument('-P', '--pretty-print', default=False, help='Pretty print json output')

    args = parser.parse_args()
    tortitles = [TorTitle(t) for t in args.TORRENT_NAME]
    if tortitles and args.format == 'csv':
        print(','.join(tortitles[0].to_json().keys()))
        for t in tortitles:
            print(t.to_csv())
    else:
        if args.pretty_print:
            pprint([t.to_json() for t in tortitles])
        else:
            print(json.dumps([t.to_json() for t in tortitles], ensure_ascii=False))
    
if __name__ == '__main__':
    main()
